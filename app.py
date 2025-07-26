from flask import Flask, render_template, session, redirect, url_for, flash, request, send_from_directory
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
import os
from connect import getCursor
from functools import wraps

app = Flask(__name__)
app.secret_key = 'internlink_secure_key'  # Change this in production

# Configure upload folders
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PROFILE_IMAGE_UPLOADS'] = os.path.join(app.config['UPLOAD_FOLDER'], 'images')
app.config['RESUME_UPLOADS'] = os.path.join(app.config['UPLOAD_FOLDER'], 'resumes')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directories if they don't exist
os.makedirs(app.config['PROFILE_IMAGE_UPLOADS'], exist_ok=True)
os.makedirs(app.config['RESUME_UPLOADS'], exist_ok=True)

# Allow only certain file types
ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
ALLOWED_RESUME_EXTENSIONS = ['pdf']

bcrypt = Bcrypt(app)

def allowed_file(filename, allowed_extensions):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# ========== AUTH DECORATOR ==========
def login_required(role=None):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash("Please log in first.")
                return redirect(url_for('login'))
            if role and session.get('role') != role:
                flash("Unauthorized access.")
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

# ========== ROUTES ==========

@app.route('/favicon.ico')
def favicon():
    return '', 204



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    cursor, db = getCursor()

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        full_name = first_name+' '+last_name
        university = request.form['university']
        course = request.form['course']
        
        if password != confirm:
            flash("Passwords do not match.")
            return render_template('register.html')

        if len(password) < 8 or password.isalpha() or password.isnumeric():
            flash("Password must include both letters and numbers.")
            return render_template('register.html')

        # Check uniqueness
        cursor.execute("SELECT * FROM user WHERE username=%s", (username,))
        if cursor.fetchone():
            flash("Username already exists.")
            return render_template('register.html')

        cursor.execute("SELECT * FROM user WHERE email=%s", (email,))
        if cursor.fetchone():
            flash("Email already exists.")
            return render_template('register.html')

        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        
        
         # Handle file uploads
        profile_pic = request.files['profile_pic']
        resume = request.files['resume']

        def allowed_file(filename, allowed_exts):
            return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_exts

        if not (allowed_file(profile_pic.filename, ALLOWED_IMAGE_EXTENSIONS) and allowed_file(resume.filename, ALLOWED_RESUME_EXTENSIONS)):
            flash("Invalid file format for profile picture or resume.")
            return render_template("register.html")

        # Save files securely
        profile_filename = secure_filename(username + "_pic_" + profile_pic.filename)
        resume_filename = secure_filename(username + "_resume_" + resume.filename)

        profile_pic.save(os.path.join(app.config['PROFILE_IMAGE_UPLOADS'], profile_filename))
        resume.save(os.path.join(app.config['RESUME_UPLOADS'], resume_filename))
        
        # Insert into user table
        cursor.execute("""INSERT INTO user (username, full_name, first_name, last_name, email, password_hash,profile_image, role, status)
                          VALUES (%s, %s, %s, %s,%s, %s,%s, %s,%s)""",
                       (username, full_name,first_name,last_name, email, hashed_pw, profile_filename,'student', 'active'))
        db.commit()

        # Get new user_id
        cursor.execute("SELECT LAST_INSERT_ID()")
        user_id = cursor.fetchone()[0]
        
               
        # Insert into student table
        cursor.execute("""INSERT INTO student (user_id, university, course, resume_path)
                          VALUES (%s, %s, %s, %s)""",
                       (user_id, university, course,  resume_filename))

        db.commit()

        # flash("Registration successful. Please log in.")
        # return redirect(url_for('login'))
        
        cursor.execute("SELECT user_id, role FROM user WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        session['user_id'] = user_data[0]
        session['username'] = username
        session['role'] = user_data[1]

        flash("Registration successful. You are now logged in.")
        return redirect(url_for('student_dashboard'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    cursor, db = getCursor()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Fixed table name consistency - using 'user' instead of 'users'
        cursor.execute("SELECT user_id, username, password_hash, role, status FROM user WHERE username=%s", (username,))
        user = cursor.fetchone()

        if user and user[4] == 'active' and bcrypt.check_password_hash(user[2], password):
            #print(user[2],password ,'-------------------------->')
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['role'] = user[3]

            if user[3] == 'student':
                return redirect(url_for('student_dashboard'))
            elif user[3] == 'employer':
                return redirect(url_for('employer_dashboard'))
            else:
                return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid credentials or inactive account.")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('index'))

# ========== STUDENT ROUTES ==========

@app.route('/student')
@login_required('student')
def student_dashboard():
    return render_template('student_dashboard.html')

@app.route('/student/internships')
@login_required('student')
def view_internships():
    cursor, db = getCursor()
    cursor.execute("SELECT * FROM internship WHERE status = 'active'")
    internships = cursor.fetchall()
    return render_template('view_internships.html', internships=internships)

@app.route('/student/applications')
@login_required('student')
def track_applications():
    cursor, db = getCursor()
    
    # Get student ID
    cursor.execute("SELECT student_id FROM student WHERE user_id = %s", (session['user_id'],))
    student_row = cursor.fetchone()
    
    if not student_row:
        flash("Student profile not found.")
        return redirect(url_for('student_dashboard'))
    
    student_id = student_row[0]
    
    cursor.execute("""
        SELECT a.*, i.title, i.company_name, i.location
        FROM application a
        JOIN internship i ON a.internship_id = i.internship_id
        WHERE a.student_id = %s
        ORDER BY a.applied_date DESC
    """, (student_id,))
    applications = cursor.fetchall()
    
    return render_template('track_applications.html', applications=applications)

@app.route('/student/apply/<int:internship_id>', methods=['GET', 'POST'])
@login_required('student')
def apply_internship(internship_id):
    cursor, db = getCursor()

    # Get internship details
    cursor.execute("SELECT * FROM internship WHERE internship_id=%s", (internship_id,))
    internship = cursor.fetchone()
    
    if not internship:
        flash("Internship not found.")
        return redirect(url_for('view_internships'))

    # Get student ID and details
    cursor.execute("""
        SELECT s.student_id, u.full_name, u.email, s.university, s.course
        FROM student s
        JOIN user u ON s.user_id = u.user_id
        WHERE s.user_id = %s
    """, (session['user_id'],))
    row = cursor.fetchone()
    
    if not row:
        flash("Student profile not found.")
        return redirect(url_for('student_dashboard'))
    
    student_id, full_name, email, university, course = row

    if request.method == 'POST':
        cover_letter = request.form['cover_letter']
        resume_file = None

        # Handle resume upload
        if 'resume' in request.files:
            resume = request.files['resume']
            if resume and resume.filename and allowed_file(resume.filename, ALLOWED_RESUME_EXTENSIONS):
                filename = secure_filename(f"resume_{student_id}_{internship_id}_{resume.filename}")
                filepath = os.path.join(app.config['RESUME_UPLOADS'], filename)
                resume.save(filepath)
                resume_file = filename
            elif resume and resume.filename:
                flash("Invalid file type. Only PDF files are allowed for resumes.")
                return render_template('apply_internship.html', internship=internship,
                                     student=(full_name, email, university, course))

        # Check for duplicate applications
        cursor.execute("SELECT * FROM application WHERE student_id=%s AND internship_id=%s", (student_id, internship_id))
        if cursor.fetchone():
            flash("You have already applied for this internship.")
            return redirect(url_for('track_applications'))

        cursor.execute("""INSERT INTO application (student_id, internship_id, cover_letter, resume_path, status)
                          VALUES (%s, %s, %s, %s, 'pending')""",
                       (student_id, internship_id, cover_letter, resume_file))
        db.commit()

        flash("Application submitted successfully.")
        return redirect(url_for('track_applications'))

    return render_template('apply_internship.html', internship=internship,
                           student=(full_name, email, university, course))

# ========== EMPLOYER ROUTES ==========

@app.route('/employer')
@login_required('employer')
def employer_dashboard():
    cursor, db = getCursor()

    # Get employer ID from logged-in user
    cursor.execute("SELECT emp_id FROM employer WHERE user_id = %s", (session['user_id'],))
    emp_row = cursor.fetchone()
    if not emp_row:
        flash("Employer profile not found.")
        return redirect(url_for('index'))
    emp_id = emp_row[0]

    cursor.execute("SELECT * FROM internship WHERE company_id = %s ORDER BY posted_date DESC", (emp_id,))
    internships = cursor.fetchall()

    return render_template('employer_dashboard.html', internships=internships)

@app.route('/employer/post', methods=['GET', 'POST'])
@login_required('employer')
def post_internship():
    cursor, db = getCursor()
    
    if request.method == 'POST':
        # Get employer ID
        cursor.execute("SELECT emp_id FROM employer WHERE user_id = %s", (session['user_id'],))
        emp_row = cursor.fetchone()
        if not emp_row:
            flash("Employer profile not found.")
            return redirect(url_for('employer_dashboard'))
        
        emp_id = emp_row[0]
        
        title = request.form['title']
        description = request.form['description']
        requirements = request.form['requirements']
        location = request.form['location']
        duration = request.form['duration']
        stipend = request.form.get('stipend', 0)
        
        cursor.execute("""
            INSERT INTO internship (company_id, title, description, requirements, location, duration, stipend, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, 'active')
        """, (emp_id, title, description, requirements, location, duration, stipend))
        db.commit()
        
        flash("Internship posted successfully!")
        return redirect(url_for('employer_dashboard'))
    
    return render_template('post_internship.html')

@app.route('/employer/applicants/<int:internship_id>')
@login_required('employer')
def view_applicants(internship_id):
    cursor, db = getCursor()

    # Verify internship belongs to current employer
    cursor.execute("SELECT emp_id FROM employer WHERE user_id = %s", (session['user_id'],))
    emp_row = cursor.fetchone()
    if not emp_row:
        flash("Employer profile not found.")
        return redirect(url_for('employer_dashboard'))
    
    emp_id = emp_row[0]
    
    cursor.execute("SELECT * FROM internship WHERE internship_id = %s AND company_id = %s", (internship_id, emp_id))
    internship = cursor.fetchone()
    if not internship:
        flash("Internship not found or unauthorized access.")
        return redirect(url_for('employer_dashboard'))

    # Get student applications for the internship
    cursor.execute("""
        SELECT a.student_id, u.full_name, u.email, s.university, s.course, 
               a.status, a.feedback, a.cover_letter, a.resume_path, a.application_date
        FROM application a
        JOIN student s ON a.student_id = s.student_id
        JOIN user u ON s.user_id = u.user_id
        WHERE a.internship_id = %s
        ORDER BY a.application_date DESC
    """, (internship_id,))
    applicants = cursor.fetchall()

    return render_template('employer_applicants.html', applicants=applicants, 
                         internship_id=internship_id, internship=internship)

@app.route('/employer/update/<int:internship_id>/<int:student_id>', methods=['POST'])
@login_required('employer')
def update_application_status(internship_id, student_id):
    cursor, db = getCursor()
    
    # Verify internship belongs to current employer
    cursor.execute("SELECT emp_id FROM employer WHERE user_id = %s", (session['user_id'],))
    emp_row = cursor.fetchone()
    if not emp_row:
        flash("Employer profile not found.")
        return redirect(url_for('employer_dashboard'))
    
    emp_id = emp_row[0]
    
    cursor.execute("SELECT * FROM internship WHERE internship_id = %s AND company_id = %s", (internship_id, emp_id))
    if not cursor.fetchone():
        flash("Unauthorized access.")
        return redirect(url_for('employer_dashboard'))
    
    new_status = request.form['status']
    feedback = request.form.get('feedback', '')

    cursor.execute("""UPDATE application 
                      SET status=%s, feedback=%s 
                      WHERE student_id=%s AND internship_id=%s""",
                   (new_status, feedback, student_id, internship_id))
    db.commit()
    
    flash("Application status updated successfully.")
    return redirect(url_for('view_applicants', internship_id=internship_id))

@app.route('/employer/edit/<int:internship_id>', methods=['GET', 'POST'])
@login_required('employer')
def edit_internship(internship_id):
    cursor, db = getCursor()
    
    # Verify internship belongs to current employer
    cursor.execute("SELECT emp_id FROM employer WHERE user_id = %s", (session['user_id'],))
    emp_row = cursor.fetchone()
    if not emp_row:
        flash("Employer profile not found.")
        return redirect(url_for('employer_dashboard'))
    
    emp_id = emp_row[0]
    
    cursor.execute("SELECT * FROM internship WHERE internship_id = %s AND company_id = %s", (internship_id, emp_id))
    internship = cursor.fetchone()
    if not internship:
        flash("Internship not found or unauthorized access.")
        return redirect(url_for('employer_dashboard'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        requirements = request.form['requirements']
        location = request.form['location']
        duration = request.form['duration']
        stipend = request.form.get('stipend', 0)
        status = request.form['status']
        
        cursor.execute("""
            UPDATE internship 
            SET title=%s, description=%s, requirements=%s, location=%s, 
                duration=%s, stipend=%s, status=%s
            WHERE internship_id=%s
        """, (title, description, requirements, location, duration, stipend, status, internship_id))
        db.commit()
        
        flash("Internship updated successfully!")
        return redirect(url_for('employer_dashboard'))
    
    return render_template('edit_internship.html', internship=internship)

# ========== ADMIN ROUTES ==========

# @app.route('/admin')
# @login_required('admin')
# def admin_dashboard():
#     cursor, db = getCursor()
    
#     # Get some statistics
#     cursor.execute("SELECT COUNT(*) FROM user WHERE role='student'")
#     student_count = cursor.fetchone()[0]
    
#     cursor.execute("SELECT COUNT(*) FROM user WHERE role='employer'")
#     employer_count = cursor.fetchone()[0]
    
#     cursor.execute("SELECT COUNT(*) FROM internship")
#     internship_count = cursor.fetchone()[0]
    
#     cursor.execute("SELECT COUNT(*) FROM application")
#     application_count = cursor.fetchone()[0]
    
#     stats = {
#         'students': student_count,
#         'employers': employer_count,
#         'internships': internship_count,
#         'applications': application_count
#     }
    
#     return render_template('admin_dashboard.html', stats=stats)

@app.route('/admin')
@login_required('admin')
def admin_dashboard():
    cursor,db = getCursor()

    # Stats
    cursor.execute("SELECT COUNT(*) FROM student")
    total_students = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM employer")
    total_employers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM internship")
    total_internships = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM application")
    total_applications = cursor.fetchone()[0]

    return render_template("admin_dashboard.html",
                           total_students=total_students,
                           total_employers=total_employers,
                           total_internships=total_internships,
                           total_applications=total_applications)




@app.route('/admin/users', methods=['GET', 'POST'])
@login_required('admin')
def manage_users():
    cursor, db = getCursor()

    # Get filter values from query parameters
    fname = request.args.get('fname', '').strip()
    lname = request.args.get('lname', '').strip()
    role = request.args.get('role', '')
    status = request.args.get('status', '')

    # Base query
    query = "SELECT user_id, username, role, status, first_name,last_name FROM user WHERE role != 'admin'"
    params = []

    # Dynamically add filters
    if fname:
        query += " AND first_name LIKE %s"
        params.append(f"%{fname}%")
    if lname:
        query += " AND last_name LIKE %s"
        params.append(f"%{lname}%")
    if role:
        query += " AND role = %s"
        params.append(role)
    if status:
        query += " AND status = %s"
        params.append(status)

    query += " ORDER BY user_id"

    cursor.execute(query, tuple(params))
    users = cursor.fetchall()

    return render_template('manage_users.html', users=users,
                           filters={'fname': fname, 'lname': lname, 'role': role, 'status': status})


@app.route('/admin/users/toggle/<int:user_id>')
@login_required('admin')
def toggle_user_status(user_id):
    cursor, db = getCursor()

    # Get current status
    cursor.execute("SELECT status FROM user WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()

    if result:
        current_status = result[0]
        new_status = 'inactive' if current_status == 'active' else 'active'

        cursor.execute("UPDATE user SET status = %s WHERE user_id = %s", (new_status, user_id))
        db.commit()

    return redirect(url_for('manage_users'))




# ============= Profile management ======
def get_user_profile(user_id, role):
    cursor, db = getCursor()

    # Start with base user info
    cursor.execute("SELECT username, email, full_name, first_name, last_name, profile_image FROM user WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()

    if not user:
        return {}

    profile = {
        'username': user[0],
        'email': user[1],
        'full_name': user[2],
        'first_name': user[3],
        'last_name': user[4],
        'profile_image': user[5],
    }

    if role == 'student':
        cursor.execute("SELECT university, course, resume_path FROM student WHERE user_id = %s", (user_id,))
        student = cursor.fetchone()
        if student:
            profile['university'] = student[0]
            profile['course'] = student[1]
            profile['resume_path'] = student[2]

    elif role == 'employer':
        cursor.execute("SELECT company_name, website, company_description FROM employer WHERE user_id = %s", (user_id,))
        emp = cursor.fetchone()
        if emp:
            profile['company_name'] = emp[0]
            profile['website'] = emp[1]
            profile['company_description'] = emp[2]

    return profile

@app.route('/profile', methods=['GET', 'POST'])
@login_required()  # or use your own role-based decorator
def profile():
    cursor, db = getCursor()
    user_id = session['user_id']
    role = session['role']

    # Get common user info
    cursor.execute("SELECT username, full_name, first_name, last_name, email, profile_image FROM user WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()

    if not user:
        flash("User not found.")
        return redirect(url_for('login'))

    # Prepare editable fields
    profile_data = {
        "username": user[0],
        "full_name": user[1],
        "first_name": user[2],
        "last_name": user[3],
        "email": user[4],
        "profile_image": user[5]
    }

    if role == 'student':
        cursor.execute("SELECT university, course, resume_path FROM student WHERE user_id = %s", (user_id,))
        student = cursor.fetchone()
        profile_data.update({
            "university": student[0],
            "course": student[1],
            "resume_path": student[2]
        })

    elif role == 'employer':
        cursor.execute("SELECT company_name, website, company_description FROM employer WHERE user_id = %s", (user_id,))
        employer = cursor.fetchone()
        profile_data.update({
            "company_name": employer[0],
            "website": employer[1],
            "company_description": employer[2]
        })

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        full_name = first_name + ' ' + last_name

        # Update profile image if uploaded
        profile_pic = request.files.get('profile_pic')
        if profile_pic and profile_pic.filename != '':
            if allowed_file(profile_pic.filename, ALLOWED_IMAGE_EXTENSIONS):
                filename = secure_filename(session['username'] + "_profile." + profile_pic.filename.rsplit('.', 1)[1])
                profile_pic.save(os.path.join(app.config['PROFILE_IMAGE_UPLOADS'], filename))
                cursor.execute("UPDATE user SET profile_image=%s WHERE user_id=%s", (filename, user_id))
                db.commit()

        # Update common fields
        cursor.execute("UPDATE user SET first_name=%s, last_name=%s, full_name=%s WHERE user_id=%s",
                       (first_name, last_name, full_name, user_id))
        db.commit()

        # Update student-specific fields
        if role == 'student':
            university = request.form['university']
            course = request.form['course']
            cursor.execute("UPDATE student SET university=%s, course=%s WHERE user_id=%s",
                           (university, course, user_id))

            resume = request.files.get('resume')
            if resume and resume.filename != '':
                if allowed_file(resume.filename, ALLOWED_RESUME_EXTENSIONS):
                    resumefile = secure_filename(session['username'] + "_resume.pdf")
                    resume.save(os.path.join(app.config['RESUME_UPLOADS'], resumefile))
                    cursor.execute("UPDATE student SET resume_path=%s WHERE user_id=%s", (resumefile, user_id))

        elif role == 'employer':
            company = request.form['company_name']
            website = request.form['website']
            company_description = request.form['company_description']
            cursor.execute("UPDATE employer SET company_name=%s, website=%s, company_description=%s WHERE user_id=%s",
                           (company, website, company_description, user_id))

        db.commit()
        flash("Profile updated successfully.")
        return redirect(url_for('profile'))

    return render_template('profile.html', profile=profile_data, role=role)



@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required()
def edit_profile():
    cursor, db = getCursor()
    user_id = session['user_id']
    role = session['role']

    if request.method == 'POST':
        # Common fields
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        full_name = first_name + " " + last_name

        # Handle new profile pic (optional)
        profile_pic = request.files.get('profile_pic')
        if profile_pic and profile_pic.filename != "":
            if allowed_file(profile_pic.filename, ALLOWED_IMAGE_EXTENSIONS):
                profile_filename = secure_filename(session['username'] + "_pic_" + profile_pic.filename)
                profile_pic.save(os.path.join(app.config['PROFILE_IMAGE_UPLOADS'], profile_filename))
                cursor.execute("UPDATE user SET profile_image=%s WHERE user_id=%s", (profile_filename, user_id))
            else:
                flash("Invalid profile picture format.")
                return redirect(url_for('edit_profile'))

        # Update basic user info
        cursor.execute("""
            UPDATE user SET first_name=%s, last_name=%s, full_name=%s WHERE user_id=%s
        """, (first_name, last_name, full_name, user_id))

        # Role-specific fields
        if role == 'student':
            university = request.form['university']
            course = request.form['course']

            # Handle new resume (optional)
            resume = request.files.get('resume')
            if resume and resume.filename != "":
                if allowed_file(resume.filename, ALLOWED_RESUME_EXTENSIONS):
                    resume_filename = secure_filename(session['username'] + "_resume_" + resume.filename)
                    resume.save(os.path.join(app.config['RESUME_UPLOADS'], resume_filename))
                    cursor.execute("UPDATE student SET resume_path=%s WHERE user_id=%s", (resume_filename, user_id))
                else:
                    flash("Invalid resume format.")
                    return redirect(url_for('edit_profile'))

            # Update other student info
            cursor.execute("""
                UPDATE student SET university=%s, course=%s WHERE user_id=%s
            """, (university, course, user_id))

        elif role == 'employer':
            company_name = request.form['company_name']
            website = request.form['website']
            company_description = request.form['company_description']

            cursor.execute("""
                UPDATE employer SET company_name=%s, website=%s, company_description=%s WHERE user_id=%s
            """, (company_name, website, company_description, user_id))

        db.commit()
        flash("Profile updated successfully.")
        return redirect(url_for('profile'))

    # GET: Show current profile info
    profile = get_user_profile(user_id, role)
    return render_template("edit_profile.html", profile=profile, role=role)





# ========== ERROR HANDLERS ==========

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# ========== UTILITY ROUTES ==========

@app.route('/download/resume/<filename>')
@login_required()
def download_resume(filename):
    """Allow employers to download student resumes"""
    if session.get('role') not in ['employer', 'admin']:
        flash("Unauthorized access.")
        return redirect(url_for('index'))
    
    try:
        return send_from_directory(app.config['RESUME_UPLOADS'], filename, as_attachment=True)
    except FileNotFoundError:
        flash("Resume file not found.")
        return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
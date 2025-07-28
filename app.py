
#import statements 
from flask import Flask, render_template, session, redirect, url_for, flash, request, send_from_directory
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
import os
from connect import getCursor
from functools import wraps
from datetime import datetime , date
import re



# App defined
app = Flask(__name__)
app.jinja_env.globals.update(now=datetime.now) # To get current date in templates
app.secret_key = 'internlink_secure_key'  #will Change  in production

# Configure upload folders
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PROFILE_IMAGE_UPLOADS'] = os.path.join(app.config['UPLOAD_FOLDER'], 'images') # profile pics and company logos go here
app.config['RESUME_UPLOADS'] = os.path.join(app.config['UPLOAD_FOLDER'], 'resumes')  # resume go here
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directories if they don't exist
os.makedirs(app.config['PROFILE_IMAGE_UPLOADS'], exist_ok=True)
os.makedirs(app.config['RESUME_UPLOADS'], exist_ok=True)

# Allow only certain file types
ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
ALLOWED_RESUME_EXTENSIONS = ['pdf']

#hashing password
bcrypt = Bcrypt(app)

def allowed_file(filename, allowed_extensions):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# ========== AUTH DECORATOR ==========
def login_required(role=None):
    """ Decorator - for login required task"""
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

# Home Page -> will have Dashboard button (Initial commit)
@app.route('/')
def index():
    """
    Home page - Just as a placeholder
    """
    return render_template('index.html')

    # 1.c Registration - Students (Initial commit)
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
        Registration 
        Handles student user registration with optional profile picture and resume upload.

            - Validates form inputs (username, email, password, etc.)
            - Verifies uniqueness of username and email
            - Hashes password securely using bcrypt
            - Saves uploaded profile picture and resume if provided
            - Inserts user into `user` and `student` tables
            - Starts session and redirects to student dashboard upon success
    """
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
        
        # Registration validation 
        if not first_name:
            flash("First name is required.")
            return render_template('register.html')
        if not last_name:
            flash("Last Name is required.")
            return render_template('register.html')
        if not email:
            flash("Email needed.")
            return render_template('register.html')
        
        email_pattern = r'^[^@]+@[^@]+\.[^@]+$'
        if not re.match(email_pattern, email):
            flash("Invalid email format.")
            return render_template('register.html')

        if not username:
            flash("Username needed.")
            return render_template('register.html')
        if not university or not course:
            flash("University and Course are required.")
            return render_template('register.html')
        if not password:
            flash("Password is required")
            return render_template('register.html')
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
        profile_pic = request.files.get('profile_pic')
        resume = request.files.get('resume')


        def allowed_file(filename, allowed_exts):
            return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_exts

        # Validate files only if they were uploaded
        if profile_pic and profile_pic.filename:
            if not allowed_file(profile_pic.filename, ALLOWED_IMAGE_EXTENSIONS):
                flash("Invalid profile picture format.")
                return render_template("register.html")
            profile_filename = secure_filename(username + "_pic_" + profile_pic.filename)
            profile_pic.save(os.path.join(app.config['PROFILE_IMAGE_UPLOADS'], profile_filename))
        else:
            profile_filename = None  # No file uploaded

        if resume and resume.filename:
            if not allowed_file(resume.filename, ALLOWED_RESUME_EXTENSIONS):
                flash("Invalid resume format.")
                return render_template("register.html")
            resume_filename = secure_filename(username + "_resume_" + resume.filename)
            resume.save(os.path.join(app.config['RESUME_UPLOADS'], resume_filename))
        else:
            resume_filename = None

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
        
        cursor.execute("SELECT user_id, role FROM user WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        session['user_id'] = user_data[0]
        session['username'] = username
        session['role'] = user_data[1]

        flash("Registration successful. You are now logged in.")
        return redirect(url_for('student_dashboard'))

    return render_template('register.html')


    # 1.a Login - All users (initial commit)
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
        Login for all users:
            - Same UI for all users
            - USername and password no extra steps
    """
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


    # 1.b Logout - All users (Initial commit)
@app.route('/logout')
def logout():
    """
        Logout 
            - Same for all user
    """
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('index'))

# ========== Internship application ==================


    # 2.a Browsing Internship Function - Admin and Students (2nd task commit)
def get_filtered_internships():
    '''
        Listing and Filtering internships for Student and Admin
            - Same filtering based on title , category,skill , duration , location
            - Same function for both admin and student 
    '''
    cursor, db = getCursor()
    location = request.args.get('location', '')
    title = request.args.get('title', '')
    duration = request.args.get('duration', '')

    query = """
        SELECT i.internship_id, i.company_id, i.title, i.description, i.location,
               i.duration, i.skills_required, i.deadline, i.stipend,
               i.number_of_openings, i.additional_req, i.posted_date,
               e.company_name
        FROM internship i
        JOIN employer e ON i.company_id = e.emp_id
        WHERE 1=1
    """
    params = []

    if location:
        query += " AND i.location LIKE %s"
        params.append(f"%{location}%")
    if title:
        query += " AND (i.title LIKE %s OR i.skills_required LIKE %s)"
        params.extend([f"%{title}%", f"%{title}%"])
    if duration:
        query += " AND i.duration = %s "
        params.append(duration)

    query += " ORDER BY i.posted_date DESC"

    cursor.execute(query, tuple(params))
    results = cursor.fetchall()

    internships = []
    for r in results:
        internships.append({
            'internship_id': r[0],
            'company_id': r[1],
            'title': r[2],
            'description': r[3],
            'location': r[4],
            'duration': r[5],
            'skills_required': r[6],
            'deadline': r[7],
            'stipend': r[8],
            'number_of_openings': r[9],
            'additional_req': r[10],
            'posted_date': r[11],
            'company_name': r[12]
        })

    return internships, {
        'location': location,
        'title': title,
        'duration': duration
    }


# ========== STUDENT ROUTES ==========

    # Student Dashboard not specific task
@app.route('/student')
@login_required('student')
def student_dashboard():
    """
        Introducing Internlink - with all features button to navigate
            - UI 
            - Buttons
    """
    return render_template('student_dashboard.html')

    # 2.a Internship Application - Browse Intership - Student  (2nd commit)
@app.route('/student/internships')
@login_required('student')
def student_browse_internships():
    """
        Listing of Internship with Apply button for Students 
            - uses get_filtered_internship() function
    """
    cursor, db = getCursor()

    internships, filters = get_filtered_internships()

    # Get student ID
    cursor.execute("SELECT student_id FROM student WHERE user_id = %s", (session['user_id'],))
    student_row = cursor.fetchone()

    applied_ids = []
    if student_row:
        student_id = student_row[0]
        cursor.execute("SELECT internship_id FROM application WHERE student_id = %s", (student_id,))
        applied_ids = [row[0] for row in cursor.fetchall()]

    return render_template(
        'view_internships.html',
        internships=internships,
        filters=filters,
        role='student',
        applied_ids=applied_ids,
        student_id=student_id,
        today=date.today()
    )

    #2.c Internship Application - Student - View list of application of that student
@app.route('/student/applications')
@login_required('student')
def track_applications():
    """
        Listing all application till now by that user
            - Status (Accept,Pending , Reject)
            - View Reason/feedback for Accepting or Rejecting as a card
            - Track or See Full details of the internship by clicking View Details Button there
            - More Detail Page - Button
    """
    cursor, db = getCursor()

    # Get student_id
    cursor.execute("SELECT student_id FROM student WHERE user_id = %s", (session['user_id'],))
    row = cursor.fetchone()
    if not row:
        flash("Student profile not found.")
        return redirect(url_for('student_dashboard'))
    student_id = row[0]

    # Fetch enriched application data
    cursor.execute("""
    SELECT 
        i.title, e.company_name, i.location,
        a.status, a.feedback, a.cover_letter, a.resume_path,
        a.application_date, e.website, e.company_description ,i.internship_id,a.student_id
    FROM application a
    JOIN internship i ON a.internship_id = i.internship_id
    JOIN employer e ON i.company_id = e.emp_id
    WHERE a.student_id = %s
    ORDER BY a.application_date DESC
""", (student_id,))
    applications = cursor.fetchall()

    return render_template('track_applications.html', applications=applications)

    # 2.c - Details of applied internship - Student, Admin (2nd commit)
@app.route('/application/<int:student_id>/<int:internship_id>')
@login_required()
def view_application_details(student_id, internship_id):
    """
        Shows more Details of the Applied Internship 
            - Admin, Student both
            - Will get every details of company,internship and Application status,feedback ,cover letter etc
            - For admin - extra info of applicant and employer
    """
    cursor, db = getCursor()
    role = session['role']
    user_id = session['user_id']

    # If student, validate ownership
    if role == 'student':
        cursor.execute("SELECT student_id FROM student WHERE user_id = %s", (user_id,))
        own_student = cursor.fetchone()
        if not own_student or own_student[0] != student_id:
            flash("Unauthorized access.")
            return redirect(url_for('student_dashboard'))

    # Fetch full application details
    cursor.execute("""
        SELECT 
            i.title, i.description, i.location, i.duration,
            i.skills_required, i.stipend, i.deadline, i.posted_date,
            e.company_name, e.website, e.company_description,
            a.status, a.feedback, a.cover_letter, a.resume_path, a.application_date,
            s.user_id, e.user_id
        FROM application a
        JOIN internship i ON a.internship_id = i.internship_id
        JOIN employer e ON i.company_id = e.emp_id
        JOIN student s ON a.student_id = s.student_id
        WHERE a.student_id = %s AND a.internship_id = %s
    """, (student_id, internship_id))

    row = cursor.fetchone()
    if not row:
        flash("Application not found.")
        return redirect(url_for('student_dashboard' if role == 'student' else 'admin_dashboard'))

    # Extract basic details
    (
        title, description, location, duration, skills_required, stipend, deadline, posted_date,
        company_name, website, company_description, status, feedback, cover_letter, resume_path,
        application_date, student_user_id, employer_user_id
    ) = row

    application = {
        "student_id": student_id,
        "internship_id": internship_id,
        "title": title,
        "description": description,
        "location": location,
        "duration": duration,
        "skills_required": skills_required,
        "stipend": stipend,
        "deadline": deadline,
        "posted_date": posted_date,
        "company_name": company_name,
        "website": website,
        "company_description": company_description,
        "status": status,
        "feedback": feedback,
        "cover_letter": cover_letter,
        "resume_path": resume_path,
        "application_date": application_date,
        "viewer_role": role
    }

    # If admin, fetch student + employer user info
    if role == 'admin':
        cursor.execute("SELECT full_name, username FROM user WHERE user_id = %s", (student_user_id,))
        student_user = cursor.fetchone()
        cursor.execute("SELECT full_name, username FROM user WHERE user_id = %s", (employer_user_id,))
        employer_user = cursor.fetchone()

        application["student_full_name"] = student_user[0] if student_user else "N/A"
        application["student_username"] = student_user[1] if student_user else "N/A"
        application["employer_full_name"] = employer_user[0] if employer_user else "N/A"
        application["employer_username"] = employer_user[1] if employer_user else "N/A"

    return render_template("application_details.html", application=application)


    #2.b Internship Application - Apply Internship - Student (2nd commit)
@app.route('/student/apply/<int:internship_id>', methods=['GET', 'POST'])
@login_required('student')
def apply_internship(internship_id):
    """
        Apply a specific internship
            - Moves to a prefilled info containing application form
            - Cover letter
            - Resume upload/replace
    """
    cursor, db = getCursor()

    # Fetch internship
    # Get internship details along with employer info
    cursor.execute("""
        SELECT i.*, e.company_name, e.website, e.company_description,e.logo_path
        FROM internship i
        JOIN employer e ON i.company_id = e.emp_id
        WHERE i.internship_id = %s
    """, (internship_id,))
    internship = cursor.fetchone()
    if not internship:
        flash("Internship not found.")
        return redirect(url_for('browse_internships'))

    # Fetch student info
    cursor.execute("""
SELECT s.student_id, u.full_name, u.email, s.university, s.course, s.resume_path
        FROM student s
        JOIN user u ON s.user_id = u.user_id
        WHERE u.user_id = %s
    """, (session['user_id'],))
    row = cursor.fetchone()
    if not row:
        flash("Student profile not found.")
        return redirect(url_for('student_dashboard'))

    student_id, full_name, email, university, course , existing_resume = row

    if request.method == 'POST':
        cover_letter = request.form['cover_letter']
        resume_file = None

        # Check for new resume upload
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
                                    student=(full_name, email, university, course),
                                    existing_resume=existing_resume)

        # Use existing resume if no new one uploaded
        if not resume_file:
            resume_file = existing_resume  # <- THIS FIXES THE ISSUE

        # Check for duplicate application
        cursor.execute("SELECT * FROM application WHERE student_id=%s AND internship_id=%s", (student_id, internship_id))
        if cursor.fetchone():
            flash("You have already applied for this internship.")
            return redirect(url_for('track_applications'))

        # Insert application
        cursor.execute("""
            INSERT INTO application (student_id, internship_id, cover_letter, resume_path, status)
            VALUES (%s, %s, %s, %s, 'pending')
        """, (student_id, internship_id, cover_letter, resume_file))
        db.commit()

        flash("Application submitted successfully.")
        return redirect(url_for('track_applications'))


    return render_template("apply_internship.html", internship=internship,
                       student=(full_name, email, university, course),
                       existing_resume=row[5])






# ========== EMPLOYER ROUTES ===========================================================

    # 3.a Manage Internship Applications -Employer dashboard - View Internships posted by them with filter 
    # (3rd commit)
@app.route('/employer')
@login_required('employer')
def employer_dashboard():
    """
    Listing all internships posted by that employer
        -  List of internships
        -  view applicants of each internship
        -  Filter internships by Title , no of openings etc
    """
    cursor, db = getCursor()

    # Get employer ID from logged-in user
    cursor.execute("SELECT emp_id FROM employer WHERE user_id = %s", (session['user_id'],))
    emp_row = cursor.fetchone()
    if not emp_row:
        flash("Employer profile not found.")
        return redirect(url_for('index'))
    emp_id = emp_row[0]

    # Get filters from query string
    title = request.args.get('title', '')
    duration = request.args.get('duration', '')
    openings = request.args.get('openings', '')
    stipend = request.args.get('stipend', '')

    query = "SELECT * FROM internship WHERE company_id = %s"
    params = [emp_id]

    if title:
        query += " AND title LIKE %s"
        params.append(f"%{title}%")
    if duration:
        query += " AND duration LIKE %s"
        params.append(f"%{duration}%")
    if openings:
        query += " AND number_of_openings = %s"
        params.append(openings)
    if stipend:
        query += " AND stipend LIKE %s"
        params.append(f"%{stipend}%")

    query += " ORDER BY posted_date DESC"

    cursor.execute(query, tuple(params))
    rows = cursor.fetchall()

    # Add "status" field based on openings
    internships = []
    for i in rows:
        internship = list(i)
        internship.append("Open" if i[9] > 0 else "Filled")  # i[9] = number_of_openings
        internships.append(internship)

    filters = {
        'title': title,
        'duration': duration,
        'openings': openings,
        'stipend': stipend
    }

    return render_template('employer_dashboard.html', internships=internships, filters=filters)

    # 3.b - View applications-with filter (4th commit)
@app.route('/employer/applicants/<int:internship_id>')
@login_required('employer')
def view_applicants(internship_id):
    '''
        View list of applicants of a specific internship
        Args :- Intership_id
        
            - List of applicants of a specific internship
            - Filter them based on full name , status
    '''
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

    # Filters
    name_filter = request.args.get('name', '').strip()
    status_filter = request.args.get('status', '').strip()

    query = """
        SELECT a.student_id, u.full_name, u.email, s.university, s.course, 
               a.status, a.feedback, a.cover_letter, a.resume_path, a.application_date
        FROM application a
        JOIN student s ON a.student_id = s.student_id
        JOIN user u ON s.user_id = u.user_id
        WHERE a.internship_id = %s
    """
    params = [internship_id]

    if name_filter:
        query += " AND u.full_name LIKE %s"
        params.append(f"%{name_filter}%")
    if status_filter:
        query += " AND a.status = %s"
        params.append(status_filter)

    query += " ORDER BY a.application_date DESC"

    cursor.execute(query, tuple(params))
    applicants = cursor.fetchall()

    return render_template('employer_applicants.html',
                           applicants=applicants,
                           internship_id=internship_id,
                           internship=internship,
                           filters={'name': name_filter, 'status': status_filter})

    #3.c - Change Status of Application - Admin and Employer (5th commit)
@app.route('/application/update/<int:internship_id>/<int:student_id>', methods=['POST'])
@login_required()
def update_application_status(internship_id, student_id):
    """
        Update the status of an application of a specific intership
        Args - intership id and that applicants-std-id
        
            - Change status to Accept,Reject
            - Add Optional feedback
    """
    cursor, db = getCursor()
    role = session['role']
    user_id = session['user_id']

    # Validate employer owns the internship or is admin
    if role == 'employer':
        cursor.execute("SELECT emp_id FROM employer WHERE user_id = %s", (user_id,))
        emp_row = cursor.fetchone()
        if not emp_row:
            flash("Employer profile not found.")
            return redirect(url_for('employer_dashboard'))

        emp_id = emp_row[0]
        cursor.execute("SELECT * FROM internship WHERE internship_id = %s AND company_id = %s", (internship_id, emp_id))
        if not cursor.fetchone():
            flash("Unauthorized: This internship does not belong to you.")
            return redirect(url_for('employer_dashboard'))

    elif role != 'admin':
        flash("Unauthorized access.")
        return redirect(url_for('index'))

    # Admin or valid employer proceeds
    new_status = request.form['status']
    feedback = request.form.get('feedback', '')

    # Get old status
    cursor.execute("""
        SELECT status FROM application 
        WHERE student_id = %s AND internship_id = %s
    """, (student_id, internship_id))
    row = cursor.fetchone()

    if not row:
        flash("Application not found.")
        return redirect(url_for('view_all_applications') if role == 'admin' else url_for('employer_dashboard'))

    old_status = row[0]

    # Update application status and feedback
    cursor.execute("""
        UPDATE application 
        SET status = %s, feedback = %s 
        WHERE student_id = %s AND internship_id = %s
    """, (new_status, feedback, student_id, internship_id))

    # Manage internship openings
    if old_status != 'Accepted' and new_status == 'Accepted':
        # Try to decrease only if there's an opening
        cursor.execute("""
            UPDATE internship 
            SET number_of_openings = number_of_openings - 1 
            WHERE internship_id = %s AND number_of_openings > 0
        """, (internship_id,))
        if cursor.rowcount == 0:
            db.rollback()
            flash("Cannot accept: No openings left for this internship.")
            return redirect(url_for('view_all_applications') if role == 'admin' else url_for('view_applicants', internship_id=internship_id))

    elif old_status == 'Accepted' and new_status != 'Accepted':
        # Rejected an accepted app → increase opening
        cursor.execute("""
            UPDATE internship 
            SET number_of_openings = number_of_openings + 1 
            WHERE internship_id = %s
        """, (internship_id,))

    db.commit()
    flash("Application status updated successfully.")

    if role == 'employer':
        return redirect(url_for('view_applicants', internship_id=internship_id))
    else:
        return redirect(url_for('view_all_applications'))




# ========== ADMIN ROUTES ===============================================================================


    # Admin dashboard - no specific task - showing all counts of users, etc (6th commit)
@app.route('/admin')
@login_required('admin')
def admin_dashboard():
    """
        List Count of Users,students,employers, applications, internship
        Buttons to navigate
    """
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


    #2.a Internship Application - Browse Internship Admin (2nd commit)
@app.route('/admin/internships')
@login_required('admin')
def admin_browse_internships():
    """
        View all internship and filter them based on title,duration , location
    """
    internships, filters = get_filtered_internships()
    return render_template('view_internships.html', internships=internships, filters=filters, role='admin')

    #5.a User Management - View User (6th commit)
@app.route('/admin/users', methods=['GET', 'POST'])
@login_required('admin')
def manage_users():
    """
    Admin dashboard route to manage user accounts.

    Retrieves a filtered list of users (students and employers) based on query parameters:
    - uname: partial or full match for username
    - fname: partial match for first name (starts with)
    - lname: partial match for last name (ends with)
    - role: exact match for user role ('student', 'employer', etc.)
    - status: exact match for account status ('active', 'inactive')

    The resulting list is displayed in the `manage_users.html` template.
    """
    cursor, db = getCursor()

    # Get filter values from query parameters
    uname = request.args.get('uname', '').strip()
    fname = request.args.get('fname', '').strip()
    lname = request.args.get('lname', '').strip()
    role = request.args.get('role', '')
    status = request.args.get('status', '')

    # Base query
    #query = "SELECT user_id, username, role, status, first_name,last_name FROM user WHERE role != 'admin'"
    query = "SELECT user_id, username, role, status, first_name,last_name FROM user WHERE 1=1"
    params = []

    # Dynamically add filters
    if uname:
        query += " AND username LIKE %s"
        params.append(f"%{uname}%")
    if fname:
        query += " AND first_name LIKE %s"
        params.append(f"{fname}%")
    if lname:
        query += " AND last_name LIKE %s"
        params.append(f"%{lname}")
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
                           filters={'uname':uname,'fname': fname, 'lname': lname, 'role': role, 'status': status})

    #2.c Internship Application - Admin - View Status (2nd commit / 7th commit)
@app.route('/admin/applications', methods=['GET'])
@login_required('admin')
def view_all_applications():
    '''    Admin route to view all internship applications.

    Supports filtering by:
    - student_name: partial match for student full name
    - title: partial match for internship title
    - status: exact match of application status ('Pending', 'Accepted', 'Rejected')

    Displays student details, internship info, application status, and optional feedback.
    Data is passed to `admin_applications.html` template for rendering.
    '''
    cursor, db = getCursor()

    # Filters
    student_name = request.args.get('student_name', '').strip()
    internship_title = request.args.get('title', '').strip()
    status = request.args.get('status', '').strip()

    query = """
        SELECT a.student_id, a.internship_id, a.status, a.application_date,
               u.full_name, u.email, i.title, i.location , a.feedback
        FROM application a
        JOIN student s ON a.student_id = s.student_id
        JOIN user u ON s.user_id = u.user_id
        JOIN internship i ON a.internship_id = i.internship_id
        WHERE 1=1
    """
    params = []

    if student_name:
        query += " AND u.full_name LIKE %s"
        params.append(f"%{student_name}%")
    if internship_title:
        query += " AND i.title LIKE %s"
        params.append(f"%{internship_title}%")
    if status:
        query += " AND a.status = %s"
        params.append(status)

    query += " ORDER BY a.application_date DESC"

    cursor.execute(query, tuple(params))
    applications = cursor.fetchall()

    filters = {
        'student_name': student_name,
        'title': internship_title,
        'status': status
    }

    return render_template("admin_applications.html", applications=applications, filters=filters)



    #5.b User Management - Change user status (7th commit)
@app.route('/admin/users/toggle/<int:user_id>')
@login_required('admin')
def toggle_user_status(user_id):
    """
    Toggle the status of a user between 'active' and 'inactive'.
    Args:
        user_id (int): The ID of the user whose status is to be toggled.
    This route is restricted to admin users. After updating the status,
    it redirects back to the user management page.
    """
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


    # 5.a- User Management - View user - other's profile (7th commit)
@app.route('/admin/view_user/<int:user_id>')
@login_required('admin')
def view_user_profile(user_id):
    """ Admin can view all users profile"""
    cursor, db = getCursor()

    # Get user basic info
    cursor.execute("SELECT role FROM user WHERE user_id = %s", (user_id,))
    role_row = cursor.fetchone()

    if not role_row:
        flash("User not found.")
        return redirect(url_for('manage_users'))

    role = role_row[0]

    # Load full profile using the same method as /profile route
    cursor.execute("SELECT username, full_name, first_name, last_name, email, profile_image FROM user WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    profile_data = {
        "username": user[0],
        "full_name": user[1],
        "first_name": user[2],
        "last_name": user[3],
        "email": user[4],
        "profile_image": user[5] if user[5] else "default_profile.png"
    }

    if role == 'student':
        cursor.execute("SELECT university, course, resume_path FROM student WHERE user_id = %s", (user_id,))
        s = cursor.fetchone()
        profile_data.update({
            "university": s[0],
            "course": s[1],
            "resume_path": s[2]
        })
    elif role == 'employer':
        cursor.execute("SELECT company_name, website, company_description, logo_path FROM employer WHERE user_id = %s", (user_id,))
        e = cursor.fetchone()
        profile_data.update({
            "company_name": e[0],
            "website": e[1],
            "company_description": e[2],
            "logo_path": e[3]
        })

    return render_template("profile.html", profile=profile_data, role=role ,  readonly=True)



# ============= Profile management =========================================================
    #4.a - Profile management (8th commit)
def get_user_profile(user_id, role):
    """
        Profile Helper Function for all users in edit
    """
    cursor, db = getCursor()

    cursor.execute("""
        SELECT username, email, full_name, first_name, last_name, profile_image
        FROM user WHERE user_id = %s
    """, (user_id,))
    user = cursor.fetchone()

    if not user:
        return {}

    profile = {
        'username': user[0],
        'email': user[1],
        'full_name': user[2],
        'first_name': user[3],
        'last_name': user[4],
        'profile_image': user[5] if user[5] else "default_profile.png"
    }

    if role == 'student':
        cursor.execute("""
            SELECT university, course, resume_path
            FROM student WHERE user_id = %s
        """, (user_id,))
        student = cursor.fetchone()
        if student:
            profile['university'] = student[0]
            profile['course'] = student[1]
            profile['resume_path'] = student[2]

    elif role == 'employer':
        cursor.execute("""
            SELECT company_name, company_description, website, logo_path
            FROM employer WHERE user_id = %s
        """, (user_id,))
        emp = cursor.fetchone()
        if emp:
            profile['company_name'] = emp[0]
            profile['company_description'] = emp[1]
            profile['website'] = emp[2]
            profile['logo_path'] = emp[3]

    return profile

    #4.a - Profile same for all user with add info 
@app.route('/profile', methods=['GET', 'POST'])
@login_required()  # or use your own role-based decorator
def profile():
    """
        View Profile with all info and an edit button
    """
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
        cursor.execute("SELECT company_name, website, company_description,logo_path FROM employer WHERE user_id = %s", (user_id,))
        employer = cursor.fetchone()
        profile_data.update({
            "company_name": employer[0],
            "website": employer[1],
            "company_description": employer[2],
            "logo_path":employer[3]
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

    #4.a,b,c - edit profile
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required()
def edit_profile():
    """
        Editing profile
            - Can edit all specified fields mentioned according to table 
    """
    cursor, db = getCursor()
    user_id = session['user_id']
    role = session['role']

    if request.method == 'POST':
        # Common fields
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        full_name = f"{first_name} {last_name}"
        email = request.form.get('email')  # editable for admin only
        remove_pic = request.form.get('remove_pic')  # checkbox

        # Update name
        cursor.execute("""
            UPDATE user SET first_name=%s, last_name=%s, full_name=%s
            WHERE user_id=%s
        """, (first_name, last_name, full_name, user_id))

        # If admin, update email
        if role == 'admin' and email:
            cursor.execute("UPDATE user SET email=%s WHERE user_id=%s", (email, user_id))

        # Handle profile picture
        profile_pic = request.files.get('profile_pic')
        if remove_pic:
            cursor.execute("UPDATE user SET profile_image=NULL WHERE user_id=%s", (user_id,))
        elif profile_pic and profile_pic.filename:
            if allowed_file(profile_pic.filename, ALLOWED_IMAGE_EXTENSIONS):
                filename = secure_filename(session['username'] + "_pic_" + profile_pic.filename)
                profile_pic.save(os.path.join(app.config['PROFILE_IMAGE_UPLOADS'], filename))
                cursor.execute("UPDATE user SET profile_image=%s WHERE user_id=%s", (filename, user_id))
            else:
                flash("Invalid profile picture format.")
                return redirect(url_for('edit_profile'))

        # Password change
        new_pw = request.form.get('new_password')
        confirm_pw = request.form.get('confirm_password')
        if new_pw:
            if len(new_pw) < 8:
                flash("Password must be atleast 8 characters long.")
                return redirect(url_for('edit_profile'))
            elif new_pw.isalpha():
                flash("Password must include both letters and numbers.")
                return redirect(url_for('edit_profile'))
            elif new_pw.isnumeric():
                flash("Password must include both letters and numbers.")
                return redirect(url_for('edit_profile'))
                
            if new_pw != confirm_pw:
                flash("Passwords do not match.")
                return redirect(url_for('edit_profile'))
            # Fetch current password hash
            cursor.execute("SELECT password_hash FROM user WHERE user_id = %s", (user_id,))
            current_hash = cursor.fetchone()[0]

            if bcrypt.check_password_hash(current_hash, new_pw):
                flash("New password must be different from the current password.")
                return redirect(url_for('edit_profile'))
            hashed_pw = bcrypt.generate_password_hash(new_pw).decode('utf-8')
            cursor.execute("UPDATE user SET password_hash=%s WHERE user_id=%s", (hashed_pw, user_id))

        # Role-specific updates
        if role == 'student':
            university = request.form['university']
            course = request.form['course']
            resume = request.files.get('resume')

            cursor.execute("""
                UPDATE student SET university=%s, course=%s WHERE user_id=%s
            """, (university, course, user_id))

            if resume and resume.filename:
                if allowed_file(resume.filename, ALLOWED_RESUME_EXTENSIONS):
                    resume_filename = secure_filename(session['username'] + "_resume_" + resume.filename)
                    resume.save(os.path.join(app.config['RESUME_UPLOADS'], resume_filename))
                    cursor.execute("UPDATE student SET resume_path=%s WHERE user_id=%s", (resume_filename, user_id))
                else:
                    flash("Invalid resume format.")
                    return redirect(url_for('edit_profile'))

        elif role == 'employer':
            company_name = request.form['company_name']
            description = request.form['company_description']
            website = request.form['website']
            logo = request.files.get('logo')

            cursor.execute("""
                UPDATE employer SET company_name=%s, company_description=%s, website=%s WHERE user_id=%s
            """, (company_name, description, website, user_id))

            if logo and logo.filename:
                if allowed_file(logo.filename, ALLOWED_IMAGE_EXTENSIONS):
                    logo_filename = secure_filename(session['username'] + "_logo_" + logo.filename)
                    logo.save(os.path.join(app.config['PROFILE_IMAGE_UPLOADS'], logo_filename))
                    cursor.execute("UPDATE employer SET logo_path=%s WHERE user_id=%s", (logo_filename, user_id))
                else:
                    flash("Invalid logo format.")
                    return redirect(url_for('edit_profile'))

        db.commit()
        flash("Profile updated successfully.")
        return redirect(url_for('profile'))

    # GET method
    profile = get_user_profile(user_id, role)
    return render_template("edit_profile.html", profile=profile, role=role)





# ========== ERROR HANDLERS ===================================

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.errorhandler(404)
def not_found_error(error):
    """Page not found html"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Server Error helper page"""
    return render_template('500.html'), 500

# ========== UTILITY ROUTES ========== During initial part

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
from flask import Flask, render_template, session, redirect, url_for, flash,request
from flask_bcrypt import Bcrypt
from flask_reuploaded import UploadSet, configure_uploads, IMAGES, DOCUMENTS, patch_request_class
import os
from connect import getCursor
from functools import wraps
app = Flask(__name__)
app.secret_key = 'internlink_secure_key'  # Change this in production

# Configure upload folders
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PROFILE_IMAGE_UPLOADS'] = os.path.join(app.config['UPLOAD_FOLDER'], 'images')
app.config['RESUME_UPLOADS'] = os.path.join(app.config['UPLOAD_FOLDER'], 'resumes')

# Allow only certain file types
ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
ALLOWED_RESUME_EXTENSIONS = ['pdf']

bcrypt = Bcrypt(app)





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
        full_name = request.form['full_name']
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

        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

        # Insert into user table
        cursor.execute("""INSERT INTO user (username, full_name, email, password_hash, role, status)
                          VALUES (%s, %s, %s, %s, 'student', 'active')""",
                       (username, full_name, email, hashed_pw))
        db.commit()

        # Get new user_id
        cursor.execute("SELECT LAST_INSERT_ID()")
        user_id = cursor.fetchone()[0]

        # Insert into student table
        cursor.execute("""INSERT INTO student (user_id, university, course)
                          VALUES (%s, %s, %s)""", (user_id, university, course))
        db.commit()

        flash("Registration successful. Please log in.")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    cursor, db = getCursor()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT user_id, username, password_hash, role, status FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()

        if user and user[4] == 'active' and bcrypt.check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['role'] = user[3]

            if user[3] == 'student':
                return redirect(url_for('student_dashboard'))
            elif user[3] == 'employer':
                return redirect(url_for('employer_dashboard'))
            else:
                return redirect(url_for('admin_dashboard'))
        flash("Invalid credentials or inactive account.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('index'))

@app.route('/student')
@login_required('student')
def student_dashboard():
    return render_template('student_dashboard.html')


# Add more route imports here later (login, register, dashboards, etc.)

@app.route('/student/apply/<int:internship_id>', methods=['GET', 'POST'])
@login_required('student')
def apply_internship(internship_id):
    cursor, db = getCursor()

    # Get internship details
    cursor.execute("SELECT * FROM internship WHERE internship_id=%s", (internship_id,))
    internship = cursor.fetchone()

    # Get student ID and details
    cursor.execute("""
        SELECT s.student_id, u.full_name, u.email, s.university, s.course
        FROM student s
        JOIN user u ON s.user_id = u.user_id
        WHERE s.user_id = %s
    """, (session['user_id'],))
    row = cursor.fetchone()
    student_id, full_name, email, university, course = row

    if request.method == 'POST':
        cover_letter = request.form['cover_letter']
        resume_file = None

        if 'resume' in request.files:
            resume = request.files['resume']
            if resume and resume.filename.endswith('.pdf'):
                filename = f"resume_{student_id}_{internship_id}.pdf"
                filepath = os.path.join('static/uploads/resumes', filename)
                resume.save(filepath)
                resume_file = filename

        # Prevent duplicate applications (based on PK)
        cursor.execute("SELECT * FROM application WHERE student_id=%s AND internship_id=%s", (student_id, internship_id))
        if cursor.fetchone():
            flash("You have already applied for this internship.")
            return redirect(url_for('track_applications'))

        cursor.execute("""INSERT INTO application (student_id, internship_id, cover_letter, resume_path)
                          VALUES (%s, %s, %s, %s)""",
                       (student_id, internship_id, cover_letter, resume_file))
        db.commit()

        flash("Application submitted successfully.")
        return redirect(url_for('track_applications'))

    return render_template('apply_internship.html', internship=internship,
                           student=(full_name, email, university, course))



#employer functionalities

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

    cursor.execute("SELECT * FROM internship WHERE company_id = %s", (emp_id,))
    internships = cursor.fetchall()

    return render_template('employer_dashboard.html', internships=internships)

@app.route('/employer/applicants/<int:internship_id>', methods=['GET', 'POST'])
@login_required('employer')
def view_applicants(internship_id):
    cursor, db = getCursor()

    # Get student applications for the internship
    cursor.execute("""
        SELECT a.student_id, u.full_name, u.email, a.status, a.feedback, a.cover_letter, a.resume_path
        FROM application a
        JOIN student s ON a.student_id = s.student_id
        JOIN user u ON s.user_id = u.user_id
        WHERE a.internship_id = %s
    """, (internship_id,))
    applicants = cursor.fetchall()

    return render_template('employer_applicants.html', applicants=applicants, internship_id=internship_id)


@app.route('/employer/update/<int:internship_id>/<int:student_id>', methods=['POST'])
@login_required('employer')
def update_application_status(internship_id, student_id):
    cursor, db = getCursor()
    new_status = request.form['status']
    feedback = request.form['feedback']

    cursor.execute("""UPDATE application 
                      SET status=%s, feedback=%s 
                      WHERE student_id=%s AND internship_id=%s""",
                   (new_status, feedback, student_id, internship_id))
    db.commit()
    flash("Application status updated.")
    return redirect(url_for('view_applicants', internship_id=internship_id))


if __name__ == '__main__':
    app.run(debug=True)

# InternLink - Internship Management System

InternLink is a comprehensive web-based internship management platform designed to bridge the gap between students seeking internship opportunities and employers looking to connect with emerging talent. The system provides role-based access for students, employers, and administrators, each with tailored functionality to streamline the internship application and management process.

## Features Overview

### For Students
- **Registration & Profile Management**: Create accounts with personal details, university information, and upload resumes
- **Browse Internships**: Search and filter internship opportunities by location, title, and duration
- **Application System**: Apply to internships with pre-filled forms and cover letter functionality
- **Application Tracking**: Monitor application status (Pending, Accepted, Rejected) with employer feedback

### For Employers
- **Dashboard**: View and manage internships posted by their organization
- **Application Management**: Review student applications with filtering capabilities
- **Status Updates**: Accept or reject applications with optional feedback
- **Profile Management**: Update company information and branding

### For Administrators
- **User Oversight**: View and manage all users across the platform
- **System Monitoring**: Track platform statistics and user activity
- **Application Review**: Monitor all internship applications system-wide
- **User Status Control**: Activate or deactivate user accounts

## Technology Stack

- **Backend**: Python 3.x with Flask framework
- **Frontend**: HTML5, Bootstrap CSS, JavaScript
- **Database**: MySQL
- **Security**: Flask-Bcrypt for password hashing
- **File Handling**: Werkzeug for secure file uploads

## Installation Guide

### Prerequisites

Before setting up InternLink, ensure you have the following installed:
- Python 3.7 or higher
- MySQL Server 8.0 or higher
- pip (Python package installer)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/InternLink.git
cd InternLink
```

### Step 2: Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv internlink_env

# Activate virtual environment
# On Windows:
internlink_env\Scripts\activate
# On macOS/Linux:
source internlink_env/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Database Setup

1. **Create Database**:
   - Open MySQL Workbench or command line
   - Execute the database creation script:
   ```sql
   source db/create_database.sql
   ```

2. **Populate Database**:
   - Run the population script to add sample data:
   ```sql
   source db/populate_database.sql
   ```

### Step 5: Configure Database Connection

1. Create a `connect.py` file in the root directory
2. Add your database connection details:

```python
import mysql.connector

def getCursor():
    connection = mysql.connector.connect(
        host='localhost',
        user='your_mysql_username',
        password='your_mysql_password',
        database='internlink_db',
        autocommit=True
    )
    cursor = connection.cursor()
    return cursor, connection
```

### Step 6: Create Upload Directories

The application will automatically create necessary directories, but you can manually create them:

```bash
mkdir -p static/uploads/images
mkdir -p static/uploads/resumes
```

### Step 7: Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## File Structure

```
InternLink/
├── app.py                      # Main Flask application
├── connect.py                  # Database connection configuration
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── .gitignore                  # Git ignore rules
├── db/
│   ├── create_database.sql     # Database schema creation
│   └── populate_database.sql   # Sample data insertion
├── templates/                  # HTML templates
│   ├── base.html              # Base template
│   ├── index.html             # Home page
│   ├── login.html             # Login form
│   ├── register.html          # Registration form
│   ├── student_dashboard.html # Student dashboard
│   ├── employer_dashboard.html# Employer dashboard
│   ├── admin_dashboard.html   # Admin dashboard
│   ├── view_internships.html  # Internship listings
│   ├── apply_internship.html  # Application form
│   ├── track_applications.html# Application tracking
│   ├── employer_applicants.html# Employer applicant view
│   ├── admin_applications.html# Admin application view
│   ├── profile.html           # User profile view
│   ├── edit_profile.html      # Profile editing
│   ├── manage_users.html      # User management
│   ├── application_details.html# Detailed application view
│   ├── 404.html               # Page not found
│   └── 500.html               # Server error
└── static/
    └── uploads/
        ├── images/            # Profile pictures and logos
        └── resumes/           # Resume files
```

## Usage Instructions

### Initial Setup

1. **Access the Application**: Navigate to `http://localhost:5000`
2. **Register as Student**: Click "Register" and create a student account
3. **Login**: Use the credentials to access student features

### Sample User Accounts

The database population script creates sample accounts for testing:

**Students** (Password: `student123` for all):
- Username: `sarah.chen` - Computer Science student from University of Auckland
- Username: `james.wilson` - Software Engineering student from Victoria University
- Username: `emily.martinez` - Information Systems student from University of Canterbury
- Username: `alex.thompson` - Data Science student from Massey University
- Username: `akhil.krishna` - CSE student from APJS

**Employers** (Password: `employer123` for all):
- Username: `techcorp.hr` - Jessica Martinez from TechCorp Solutions
- Username: `innovate.recruit` - Mark Thompson from Innovate Solutions
- Username: `fintech.careers` - Rachel Chen from FinTech Plus
- Username: `green.energy` - Daniel Williams from Green Energy Corp
- Username: `media.creative` - Sophie Brown from Creative Media Hub

**Administrators** (Password: `admin123` for all):
- Username: `admin.system` - Aravind S (System Administrator)
- Username: `admin.support` - Angel Thomas (Support Administrator)

### Key Workflows

#### Student Journey
1. Register account with personal and academic details
2. Upload profile picture and resume (optional)
3. Browse available internships using filters
4. Apply to desired positions with cover letters
5. Track application status and receive feedback

#### Employer Journey
1. Login with employer credentials
2. View internships posted by your organization
3. Review student applications with filtering options
4. Accept or reject applications with feedback
5. Manage company profile and information

#### Administrator Journey
1. Login with admin credentials
2. Monitor platform statistics on dashboard
3. View and filter all users across the system
4. Review all internship applications
5. Manage user account statuses

## Configuration Options

### File Upload Settings

The application supports the following file types:
- **Profile Images**: PNG, JPG, JPEG, GIF (max 16MB)
- **Resumes**: PDF only (max 16MB)
- **Company Logos**: PNG, JPG, JPEG, GIF (max 16MB)

### Security Features

- **Password Requirements**: Minimum 8 characters with letters and numbers
- **Session Management**: Secure Flask sessions with role-based access
- **File Security**: Secure filename handling and upload validation
- **Password Hashing**: Bcrypt encryption for all passwords

## Troubleshooting

### Common Issues

**Database Connection Errors**:
- Verify MySQL server is running
- Check connection credentials in `connect.py`
- Ensure database exists and is populated

**File Upload Issues**:
- Check upload directory permissions
- Verify file size limits
- Ensure allowed file extensions

**Login Problems**:
- Confirm user account exists in database
- Verify password meets requirements
- Check account status is 'active'

**Template Errors**:
- Ensure all template files are in correct directories
- Check for missing static files
- Verify Bootstrap CSS is loading properly

### Debug Mode

For development, enable debug mode by modifying the last line in `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

## Deployment Notes

### Production Considerations

1. **Security**: Change the secret key in production
2. **Database**: Use environment variables for database credentials
3. **File Storage**: Consider cloud storage for uploaded files
4. **HTTPS**: Enable SSL/TLS for secure connections
5. **Error Handling**: Implement comprehensive logging

### PythonAnywhere Deployment

1. Upload all files except `connect.py` and virtual environment
2. Create new `connect.py` with PythonAnywhere database settings
3. Set up MySQL database using provided scripts
4. Configure WSGI file to point to your Flask app
5. Set up static file mappings for uploads directory

## Support and Maintenance

### Regular Maintenance Tasks

- **Database Backups**: Regular backups of user data and applications
- **File Cleanup**: Periodic cleanup of uploaded files
- **Security Updates**: Keep dependencies updated
- **Performance Monitoring**: Monitor application performance and database queries

### Contact Information

For technical support or feature requests, please contact the development team or submit issues through the project repository.

## License

This project is developed as part of academic coursework and is intended for educational purposes. All rights reserved.
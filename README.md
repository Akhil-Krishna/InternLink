# InternLink - Internship Management System

InternLink is a web app for internship management where it provides a free platform for students to look for internship opportunities and employers who are looking for emerging talents.This web app provides role-based access for all users such as students , employers and administrators.Each of them will have various functionalities 

## Features Overview

### For Students
- **Registration & Profile Management**
- **Browse Internships with Filters**
- **Apply Internships**
- **Application Tracking**

### For Employers
- **View Internships posted by their organization**
- **View Application and filter it**
- **Manage and update applications**
- **Profile Management**

### For Administrators
- **View and Filter Users and can change their status**
- **Entire stats monitoring**
- **Application Review and status update**
- **View all the Internships**

## Technology Stack

- **Backend**: Python 3.x with Flask framework
- **Frontend**: HTML5, Bootstrap CSS, JavaScript
- **Database**: MySQL
- **Security**: Flask-Bcrypt for password hashing
- **File Handling**: Werkzeug for secure file uploads

## Installation Guide

### Prerequisites

Before setting up, install the following:
- Python 3.7 or higher
- MySQL Server 8.0 or higher
- pip (Python package installer)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/../InternLink.git
cd InternLink
```

### Step 2: Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### Step 3: Install Dependencies using requirements.txt

```bash
pip install -r requirements.txt
```

### Step 4: Database Setup

1. **Create Database**:
   - Open MySQL Workbench or cmd
    ```sql
      CREATE DATABASE internlink;
    ```
2. **Creating Tables and relations**
   - Open cmd and move to folder containg create_database.sql (db in this case)
   - Execute the database creation script:
   ```sql
   mysql -u <username> -p internlink < create_database.sql
   ```

2. **Populate Database**:
   - Move to folder containg populate_database.sql (db in this case)
   - Run the population script to add sample data:
   ```sql
   mysql -u <username> -p internlink < populate_database.sql
   ```

### Step 5: Configure Database Connection

1. Create a `connect.py` file in the root directory
2. Add the database connection details:

```python
import mysql.connector

def getCursor():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="internlink"
    )
    return db.cursor(buffered=True), db

```

### Step 6: Create Upload Directories

During cloning Directories to store profiles pics and resumes will be automatically created (if not)

```bash
mkdir -p static/uploads/images
mkdir -p static/uploads/resumes
```

### Step 7: Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`


## Deploying in PythonAnywhere

### PythonAnywhere Deployment

1. Upload all the files except -> `connect.py` and virtual env
2. Create new `connect.py` with PythonAnywhere database settings
3. Set up MySQL database in PythonAnywhere - Open Mysql console there and use the 2 sql scripts to create and populate it
4. Configure WSGI file to point to your Flask app
5. Set up static file mappings for the uploads


## Usage Instructions

### Initial Setup

1. Open `http://localhost:5000` in browser tab
2. Click Register and create a student account by providing required details + it should follow requirements
3. It will be automatically logged in (if not log in using username and password)

### Sample User Accounts

**Students** :
- Username: `sarah.chen` - Password : S@rahCh3n2025!
- Username: `james.wilson` - Password : J@mesW1ls0n#
- Username: `emily.martinez` - Password : Em1lyM@rt1nez$
- Username: `alex.thompson` -  Password : Al3xTh0mps0n%
- Username: `akhil.krishna` - CSE student from APJS - Password : Akhil@1234

**Employers** :
- Username: `techcorp.hr`  - Password : T3chC0rpHR2025!
- Username: `innovate.recruit` - Password : 1nn0v@t3R3crU1t#
- Username: `fintech.careers` - Password : F1nt3chC@r33rs$
- Username: `green.energy` - Password : Gr33nEn3rgy%
- Username: `media.creative` -  Password : M3d1@Cr3@t1v3^

**Administrators** :
- Username: `admin.system` - Aravind S (System Administrator) - Password : Adm1nSyst3m*
- Username: `admin.support` - Angel Thomas (Support Administrator) - Password : Adm1nSupp0rt&

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
- **Session Management**
- **File Security**: Secure filename handling and upload validation
- **Password Hashing**: Bcrypt encryption for all passwords
- **Email Verification**

## Troubleshooting

### Common Issues

**Database Connection Errors**:
- Verify MySQL server is okay
- Check connection info in `connect.py`
- Ensure database exist and is populated

**File Upload Issues**:
- Verify file size limits and recheck the file properties
- Ensure allowed file extensions

**Login Problems**:
- Confirm user account exists in db
- Verify password 
- Check account status is 'active' , only active accounts can login

**Template Error**:
- Ensure all html files are placed inside templates
- Verify Bootstrap CSS and Js scripts are specified in base.html
  

## License

This is a Website based on flask for academic purpose and all the data provided are samples . All rights reserved
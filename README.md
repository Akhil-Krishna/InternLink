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

## Setup Instruction

### Prerequisites

Before setting up, install the following:
- Python 3.7 or higher
- MySQL Server 8.0 or higher
- pip (Python package installer)
- Git

### Step 1: Clone the Repo

```bash
git clone https://github.com/../InternLink.git
cd InternLink
```

### Step 2: Set Up Virtual Env either using venv through command palette or cmd

```bash
python -m venv env

# Activate virtual env
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate
```

### Step 3: Install Dependencies using requirements.txt

```bash
pip install -r requirements.txt
```

### Step 4: Database Setup (2 ways)

1. **Create Database**:
   - Open cmd or mysql workbench
    ```sql
      CREATE DATABASE internlink;
    ```
2. **Creating Tables and relations**
   - Open cmd and move to folder containg create_database.sql (db in this case)
   - Execute the database creation script:
   ```sql
   mysql -u <username> -p internlink < create_database.sql
   ```

3. **Populate Database**:
   - Move to folder containg populate_database.sql (db in this case)
   - Run the population script to add sample data:
   ```sql
   mysql -u <username> -p internlink < populate_database.sql
   ```
or
1. **Open mysql in cmd and type the following command**
   ```sql
   source path\db\create_database.sql
   source path\db\populate_database.sql
   ```

### Step 5: Configure Database Connection

1. Create a `connect.py` file in the root directory
2. Add the database connection details:

```python
import mysql.connector # or pymysql

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

1. Upload all the files except -> `connect.py` and virtual env using git clone
2. Create new `connect.py` with PythonAnywhere database settings
   ```bash
   import pymysql

   def getCursor():
       db = pymysql.connect(
           host="angelthomas1165399.mysql.pythonanywhere-services.com",
           user="angelthomas1165399",
           password="pass",
           database="angelthomas1165399$internlink"
       )
       return db.cursor(), db

   ``` 
4. Set up MySQL database in PythonAnywhere - Open Mysql console there and use the 2 sql scripts to create and populate it
5. Configure WSGI file to point out the flask app 
6. Set up static file mappings for the uploads


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

#### Student
1. Register account with username , resume etc details
2. Upload profile picture and resume (which is optional)
3. Go through available internships and search based on category , duration and location
4. Apply to your interested internship by uploading specific resumes and cover letter
5. Student can then track their all applications and also can see feedbacks

#### Employer
1. Login with employer username and password
2. Can view all internships posted by that organisation
3. Can review student applications for each role and also based on filters
4. Accept or reject applications by adding extra feedback
5. View and edit profile

#### Administrator Journey
1. Login with admin username and password
2. On the dashboard : Can see all the stats of no of students, employers , internship and applications
3. See the list of users and filter them based on their details
4. Review all internship applications
5. Manage user account : ie , activate and deactivate them

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

## License

This is a Website based on flask for academic purpose and all the data provided are samples . All rights reserved
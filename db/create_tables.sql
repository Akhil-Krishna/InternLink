-- InternLink Database Creation Script
-- COMP639 Studio Project - Individual Assignment
-- Database creation script for InternLink internship management system

-- Drop database if it exists and create new one
DROP DATABASE IF EXISTS internlink;
CREATE DATABASE internlink;
USE internlink;

-- Create users table (main user table)
CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password_hash CHAR(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
    profile_image VARCHAR(255) DEFAULT 'default_profile.png',
    role ENUM('student', 'employer', 'admin') NOT NULL DEFAULT 'student',
    status ENUM('active', 'inactive') NOT NULL DEFAULT 'active',
    PRIMARY KEY (user_id)
);

-- Create student table (extends user for students)
CREATE TABLE student (
    student_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    university VARCHAR(100) NOT NULL,
    course VARCHAR(100) NOT NULL,
    resume_path VARCHAR(255) DEFAULT NULL,
    PRIMARY KEY (student_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

-- Create employer table (extends user for employers)
CREATE TABLE employer (
    emp_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    company_name VARCHAR(100) NOT NULL,
    company_description TEXT DEFAULT NULL,
    website VARCHAR(100) DEFAULT NULL,
    logo_path VARCHAR(255) DEFAULT 'default_company_logo.png',
    PRIMARY KEY (emp_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

-- Create internship table
CREATE TABLE internship (
    internship_id INT NOT NULL AUTO_INCREMENT,
    company_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    location VARCHAR(100) NOT NULL,
    duration VARCHAR(50) NOT NULL,
    skills_required TEXT DEFAULT NULL,
    deadline DATE NOT NULL,
    stipend VARCHAR(50) DEFAULT NULL,
    number_of_openings INT DEFAULT 1,
    additional_req TEXT DEFAULT NULL,
    PRIMARY KEY (internship_id),
    FOREIGN KEY (company_id) REFERENCES employer(emp_id) ON DELETE CASCADE
);

-- Create application table
CREATE TABLE application (
    student_id INT NOT NULL,
    internship_id INT NOT NULL,
    status ENUM('Pending', 'Accepted', 'Rejected') NOT NULL DEFAULT 'Pending',
    feedback TEXT DEFAULT NULL,
    cover_letter TEXT DEFAULT NULL,
    resume_path VARCHAR(255) DEFAULT NULL,
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id, internship_id),
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (internship_id) REFERENCES internship(internship_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_user_username ON user(username);
CREATE INDEX idx_user_role ON user(role);
CREATE INDEX idx_user_status ON user(status);
CREATE INDEX idx_student_user ON student(user_id);
CREATE INDEX idx_employer_user ON employer(user_id);
CREATE INDEX idx_internship_company ON internship(company_id);
CREATE INDEX idx_application_status ON application(status);
CREATE INDEX idx_application_date ON application(application_date);

-- Display table structure
SHOW TABLES;
DESCRIBE user;
DESCRIBE student;
DESCRIBE employer;
DESCRIBE internship;
DESCRIBE application;
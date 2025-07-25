-- InternLink Database Population Script
-- COMP639 Studio Project - Individual Assignment
-- Populates database with realistic test data

USE internlink;

-- Insert Users (Students, Employers, Admins)
-- Note: All passwords are hashed using bcrypt. The original passwords are listed in comments for testing

-- STUDENTS (20 students)
-- Password: student123
INSERT INTO user (username, full_name, email, password_hash, profile_image, role, status) VALUES
('sarah.chen', 'Sarah Chen', 'sarah.chen@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'sarah_chen.jpg', 'student', 'active'),
('james.wilson', 'James Wilson', 'james.wilson@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'james_wilson.jpg', 'student', 'active'),
('emily.martinez', 'Emily Martinez', 'emily.martinez@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'emily_martinez.jpg', 'student', 'active'),
('alex.thompson', 'Alex Thompson', 'alex.thompson@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'alex_thompson.jpg', 'student', 'active'),
('priya.sharma', 'Priya Sharma', 'priya.sharma@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'priya_sharma.jpg', 'student', 'active'),
('david.brown', 'David Brown', 'david.brown@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'david_brown.jpg', 'student', 'active'),
('lisa.wang', 'Lisa Wang', 'lisa.wang@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'lisa_wang.jpg', 'student', 'active'),
('michael.jones', 'Michael Jones', 'michael.jones@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'michael_jones.jpg', 'student', 'active'),
('aisha.patel', 'Aisha Patel', 'aisha.patel@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'aisha_patel.jpg', 'student', 'active'),
('ryan.garcia', 'Ryan Garcia', 'ryan.garcia@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'ryan_garcia.jpg', 'student', 'active'),
('natalie.kim', 'Natalie Kim', 'natalie.kim@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'natalie_kim.jpg', 'student', 'active'),
('tom.anderson', 'Tom Anderson', 'tom.anderson@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'tom_anderson.jpg', 'student', 'active'),
('sophia.rodriguez', 'Sophia Rodriguez', 'sophia.rodriguez@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'sophia_rodriguez.jpg', 'student', 'active'),
('ethan.lee', 'Ethan Lee', 'ethan.lee@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'ethan_lee.jpg', 'student', 'active'),
('olivia.taylor', 'Olivia Taylor', 'olivia.taylor@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'olivia_taylor.jpg', 'student', 'active'),
('lucas.moore', 'Lucas Moore', 'lucas.moore@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'lucas_moore.jpg', 'student', 'active'),
('isabella.clark', 'Isabella Clark', 'isabella.clark@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'isabella_clark.jpg', 'student', 'active'),
('noah.walker', 'Noah Walker', 'noah.walker@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'noah_walker.jpg', 'student', 'active'),
('zoe.allen', 'Zoe Allen', 'zoe.allen@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'zoe_allen.jpg', 'student', 'active'),
('jacob.hill', 'Jacob Hill', 'jacob.hill@student.uni.nz', '$2b$12$LQv3c1yX8LyaH7CjF5Y8PO4f1G5Q3n9M8KvV4J2XmZ9p7R1sT0uV3', 'jacob_hill.jpg', 'student', 'active');

-- EMPLOYERS (5 employers)
-- Password: employer123
INSERT INTO user (username, full_name, email, password_hash, profile_image, role, status) VALUES
('techcorp.hr', 'Jessica Martinez', 'jessica.martinez@techcorp.co.nz', '$2b$12$9xK2L5vY7qW3mR8nP4sZ1O6f2H4Q7n0M9KvV3J1XmZ8p6R0sT9uV2', 'jessica_martinez.jpg', 'employer', 'active'),
('innovate.recruit', 'Mark Thompson', 'mark.thompson@innovatesolutions.co.nz', '$2b$12$9xK2L5vY7qW3mR8nP4sZ1O6f2H4Q7n0M9KvV3J1XmZ8p6R0sT9uV2', 'mark_thompson.jpg', 'employer', 'active'),
('fintech.careers', 'Rachel Chen', 'rachel.chen@fintechplus.co.nz', '$2b$12$9xK2L5vY7qW3mR8nP4sZ1O6f2H4Q7n0M9KvV3J1XmZ8p6R0sT9uV2', 'rachel_chen.jpg', 'employer', 'active'),
('green.energy', 'Daniel Williams', 'daniel.williams@greenenergy.co.nz', '$2b$12$9xK2L5vY7qW3mR8nP4sZ1O6f2H4Q7n0M9KvV3J1XmZ8p6R0sT9uV2', 'daniel_williams.jpg', 'employer', 'active'),
('media.creative', 'Sophie Brown', 'sophie.brown@creativemedia.co.nz', '$2b$12$9xK2L5vY7qW3mR8nP4sZ1O6f2H4Q7n0M9KvV3J1XmZ8p6R0sT9uV2', 'sophie_brown.jpg', 'employer', 'active');

-- ADMINISTRATORS (2 admins)
-- Password: admin123
INSERT INTO user (username, full_name, email, password_hash, profile_image, role, status) VALUES
('admin.system', 'Admin System', 'admin@internlink.co.nz', '$2b$12$8zJ1K4vX6pV2lQ7mO3rY0N5e1G3P6m8L8JuU2I0WlY7o5Q9rS8tU1', 'admin_system.jpg', 'admin', 'active'),
('admin.support', 'Admin Support', 'support@internlink.co.nz', '$2b$12$8zJ1K4vX6pV2lQ7mO3rY0N5e1G3P6m8L8JuU2I0WlY7o5Q9rS8tU1', 'admin_support.jpg', 'admin', 'active');

-- Insert Student details
INSERT INTO student (user_id, university, course, resume_path) VALUES
(1, 'University of Auckland', 'Computer Science', 'resumes/sarah_chen_resume.pdf'),
(2, 'Victoria University of Wellington', 'Software Engineering', 'resumes/james_wilson_resume.pdf'),
(3, 'University of Canterbury', 'Information Systems', 'resumes/emily_martinez_resume.pdf'),
(4, 'Massey University', 'Data Science', 'resumes/alex_thompson_resume.pdf'),
(5, 'Auckland University of Technology', 'Computer Science', 'resumes/priya_sharma_resume.pdf'),
(6, 'University of Otago', 'Information Technology', 'resumes/david_brown_resume.pdf'),
(7, 'University of Waikato', 'Computer Science', 'resumes/lisa_wang_resume.pdf'),
(8, 'Victoria University of Wellington', 'Software Engineering', 'resumes/michael_jones_resume.pdf'),
(9, 'University of Auckland', 'Information Systems', 'resumes/aisha_patel_resume.pdf'),
(10, 'Auckland University of Technology', 'Data Science', 'resumes/ryan_garcia_resume.pdf'),
(11, 'University of Canterbury', 'Computer Science', 'resumes/natalie_kim_resume.pdf'),
(12, 'Massey University', 'Software Engineering', 'resumes/tom_anderson_resume.pdf'),
(13, 'University of Otago', 'Information Technology', 'resumes/sophia_rodriguez_resume.pdf'),
(14, 'University of Waikato', 'Computer Science', 'resumes/ethan_lee_resume.pdf'),
(15, 'Victoria University of Wellington', 'Data Science', 'resumes/olivia_taylor_resume.pdf'),
(16, 'University of Auckland', 'Software Engineering', 'resumes/lucas_moore_resume.pdf'),
(17, 'Auckland University of Technology', 'Information Systems', 'resumes/isabella_clark_resume.pdf'),
(18, 'University of Canterbury', 'Computer Science', 'resumes/noah_walker_resume.pdf'),
(19, 'Massey University', 'Information Technology', 'resumes/zoe_allen_resume.pdf'),
(20, 'University of Otago', 'Data Science', 'resumes/jacob_hill_resume.pdf');

-- Insert Employer details
INSERT INTO employer (user_id, company_name, company_description, website, logo_path) VALUES
(21, 'TechCorp Solutions', 'Leading technology solutions provider specializing in cloud computing and enterprise software development.', 'https://www.techcorp.co.nz', 'logos/techcorp_logo.png'),
(22, 'Innovate Solutions', 'Digital transformation consultancy helping businesses leverage cutting-edge technology for growth.', 'https://www.innovatesolutions.co.nz', 'logos/innovate_logo.png'),
(23, 'FinTech Plus', 'Financial technology startup developing innovative payment solutions and digital banking platforms.', 'https://www.fintechplus.co.nz', 'logos/fintech_logo.png'),
(24, 'Green Energy Corp', 'Renewable energy company focused on sustainable power solutions and environmental technology.', 'https://www.greenenergy.co.nz', 'logos/greenenergy_logo.png'),
(25, 'Creative Media Hub', 'Digital marketing and media production company creating engaging content for modern brands.', 'https://www.creativemedia.co.nz', 'logos/creativemedia_logo.png');

-- Insert Internships (20+ internships)
INSERT INTO internship (company_id, title, description, location, duration, skills_required, deadline, stipend, number_of_openings, additional_req) VALUES
(1, 'Software Development Intern', 'Join our development team to work on cloud-based enterprise applications using modern technologies like React, Node.js, and AWS.', 'Auckland', '3 months', 'JavaScript, React, Node.js, Git', '2025-09-15', '$400/week', 2, 'Portfolio of personal projects required'),
(1, 'Data Analytics Intern', 'Analyze large datasets to provide business insights and develop automated reporting solutions using Python and SQL.', 'Auckland', '6 months', 'Python, SQL, Data Visualization, Statistics', '2025-09-30', '$450/week', 1, 'Experience with Pandas and Matplotlib preferred'),
(1, 'DevOps Engineering Intern', 'Learn infrastructure automation, CI/CD pipelines, and cloud deployment strategies in our DevOps team.', 'Auckland', '4 months', 'Linux, Docker, AWS, Git', '2025-10-01', '$420/week', 1, 'Basic understanding of containerization'),
(2, 'Frontend Developer Intern', 'Create responsive web interfaces and user experiences for our client projects using modern frontend frameworks.', 'Wellington', '3 months', 'HTML, CSS, JavaScript, Vue.js', '2025-09-20', '$380/week', 2, 'Design portfolio showcasing UI/UX work'),
(2, 'Mobile App Development Intern', 'Develop cross-platform mobile applications using React Native for iOS and Android platforms.', 'Wellington', '4 months', 'React Native, JavaScript, Mobile Development', '2025-10-05', '$400/week', 1, 'Published app or strong mobile project portfolio'),
(2, 'Digital Marketing Intern', 'Support digital marketing campaigns, content creation, and social media management for technology clients.', 'Wellington', '3 months', 'Social Media, Content Creation, Analytics', '2025-09-25', '$320/week', 1, 'Strong written communication skills'),
(3, 'Financial Technology Intern', 'Work on fintech applications including payment processing systems and financial data analysis tools.', 'Christchurch', '6 months', 'Java, Spring Boot, Financial Systems, SQL', '2025-10-10', '$480/week', 2, 'Interest in financial markets and technology'),
(3, 'Blockchain Development Intern', 'Explore blockchain technology and develop smart contracts for financial applications.', 'Christchurch', '4 months', 'Solidity, Ethereum, JavaScript, Cryptography', '2025-09-28', '$500/week', 1, 'Basic understanding of blockchain concepts'),
(3, 'Cybersecurity Intern', 'Learn about financial system security, penetration testing, and security compliance frameworks.', 'Christchurch', '5 months', 'Network Security, Python, Ethical Hacking', '2025-10-15', '$460/week', 1, 'Security certifications or coursework preferred'),
(4, 'Renewable Energy Systems Intern', 'Support the development of smart grid technology and energy management systems.', 'Hamilton', '4 months', 'Python, IoT, Data Analysis, Engineering', '2025-09-18', '$400/week', 2, 'Engineering or environmental science background'),
(4, 'Environmental Data Analyst Intern', 'Analyze environmental impact data and create sustainability reports for renewable energy projects.', 'Hamilton', '3 months', 'R, Python, Statistics, Environmental Science', '2025-10-20', '$380/week', 1, 'Environmental studies or related field'),
(4, 'Green Tech Software Intern', 'Develop software solutions for monitoring and optimizing renewable energy systems.', 'Hamilton', '6 months', 'C++, Python, Embedded Systems, MATLAB', '2025-09-12', '$440/week', 1, 'Interest in sustainable technology'),
(5, 'Digital Content Creation Intern', 'Create engaging digital content including videos, graphics, and interactive media for brand campaigns.', 'Dunedin', '3 months', 'Adobe Creative Suite, Video Editing, Design', '2025-10-08', '$350/week', 2, 'Portfolio of creative work required'),
(5, 'Web Development Intern', 'Build modern websites and web applications for creative industry clients using latest web technologies.', 'Dunedin', '4 months', 'HTML, CSS, JavaScript, WordPress, PHP', '2025-09-22', '$380/week', 1, 'Strong portfolio of web projects'),
(5, 'Social Media Strategy Intern', 'Develop and implement social media strategies for creative brands and analyze engagement metrics.', 'Dunedin', '3 months', 'Social Media Marketing, Analytics, Content Strategy', '2025-10-12', '$320/week', 1, 'Experience with social media platforms'),
(1, 'Machine Learning Intern', 'Work on AI and machine learning projects to enhance our software products with intelligent features.', 'Auckland', '5 months', 'Python, TensorFlow, Machine Learning, Mathematics', '2025-10-25', '$480/week', 1, 'Strong mathematical background and ML coursework'),
(2, 'UX/UI Design Intern', 'Design user interfaces and conduct user research to improve the usability of our digital products.', 'Wellington', '4 months', 'Figma, Adobe XD, User Research, Prototyping', '2025-09-30', '$400/week', 1, 'Design portfolio and user research experience'),
(3, 'Quality Assurance Intern', 'Test financial software applications and develop automated testing frameworks to ensure product quality.', 'Christchurch', '3 months', 'Software Testing, Selenium, Test Automation', '2025-10-18', '$360/week', 2, 'Attention to detail and analytical mindset'),
(4, 'Project Management Intern', 'Assist project managers in coordinating renewable energy projects and client communications.', 'Hamilton', '4 months', 'Project Management, Communication, MS Office', '2025-09-14', '$380/week', 1, 'Strong organizational and communication skills'),
(5, 'Video Production Intern', 'Produce promotional videos and documentaries for creative industry clients using professional equipment.', 'Dunedin', '6 months', 'Video Production, Final Cut Pro, Cinematography', '2025-10-05', '$420/week', 1, 'Video production portfolio and equipment knowledge');

-- Insert Applications (20+ applications with varied statuses)
INSERT INTO application (student_id, internship_id, status, feedback, cover_letter, resume_path, application_date) VALUES
(1, 1, 'Accepted', 'Excellent technical skills and great portfolio. Welcome to the team!', 'I am excited to apply for the Software Development Intern position. My experience with React and Node.js through university projects makes me a strong candidate.', 'resumes/sarah_chen_resume.pdf', '2025-07-10 09:15:00'),
(2, 1, 'Rejected', 'Strong candidate but we found someone with more relevant experience.', 'I would love to contribute to your development team. My software engineering background and passion for cloud technologies align perfectly with this role.', 'resumes/james_wilson_resume.pdf', '2025-07-11 14:30:00'),
(3, 2, 'Pending', NULL, 'Data analytics has always fascinated me. I have experience with Python and SQL from my coursework and would love to apply these skills in a real-world setting.', 'resumes/emily_martinez_resume.pdf', '2025-07-12 11:45:00'),
(4, 4, 'Accepted', 'Great enthusiasm for frontend development and solid technical foundation.', 'I am passionate about creating beautiful user interfaces. My Vue.js projects demonstrate my ability to build responsive and engaging web applications.', 'resumes/alex_thompson_resume.pdf', '2025-07-08 16:20:00'),
(5, 7, 'Pending', NULL, 'FinTech represents the future of finance. My computer science background and interest in financial markets make me ideal for this position.', 'resumes/priya_sharma_resume.pdf', '2025-07-13 10:00:00'),
(6, 3, 'Rejected', 'Good technical skills but limited DevOps experience.', 'I am eager to learn about DevOps practices and cloud infrastructure. My Linux experience and understanding of containerization provide a good foundation.', 'resumes/david_brown_resume.pdf', '2025-07-09 13:15:00'),
(7, 5, 'Accepted', 'Impressive mobile development portfolio and strong React Native skills.', 'Mobile development is my passion. I have published two apps on the App Store and would love to bring my React Native expertise to your team.', 'resumes/lisa_wang_resume.pdf', '2025-07-14 08:30:00'),
(8, 6, 'Pending', NULL, 'I am interested in combining my technical skills with marketing knowledge. This internship would provide valuable experience in digital marketing strategies.', 'resumes/michael_jones_resume.pdf', '2025-07-15 12:45:00'),
(9, 8, 'Rejected', 'Interesting background but we need more blockchain-specific experience.', 'Blockchain technology fascinates me. While I am still learning about smart contracts, my programming skills and eagerness to learn make me a good candidate.', 'resumes/aisha_patel_resume.pdf', '2025-07-07 15:10:00'),
(10, 10, 'Accepted', 'Perfect match for our renewable energy projects with strong analytical skills.', 'Sustainable technology is the future. My data science background and passion for environmental issues align perfectly with your mission.', 'resumes/ryan_garcia_resume.pdf', '2025-07-16 09:25:00'),
(11, 12, 'Pending', NULL, 'I am excited about the intersection of software development and environmental sustainability. This role would allow me to contribute to meaningful green technology solutions.', 'resumes/natalie_kim_resume.pdf', '2025-07-11 17:40:00'),
(12, 13, 'Accepted', 'Creative portfolio shows excellent design skills and understanding of brand identity.', 'Creative content creation combines my technical skills with artistic passion. My portfolio demonstrates experience across various media formats.', 'resumes/tom_anderson_resume.pdf', '2025-07-18 11:20:00'),
(13, 14, 'Rejected', 'Good technical foundation but limited web development portfolio.', 'Web development allows me to create impactful digital experiences. My IT background provides the technical foundation needed for modern web applications.', 'resumes/sophia_rodriguez_resume.pdf', '2025-07-12 14:55:00'),
(14, 16, 'Pending', NULL, 'Machine learning represents the cutting edge of technology. My mathematics background and programming skills position me well for AI development work.', 'resumes/ethan_lee_resume.pdf', '2025-07-17 10:35:00'),
(15, 17, 'Accepted', 'Strong design thinking and excellent user research methodology understanding.', 'UX/UI design is where technology meets human needs. My design portfolio and user research experience demonstrate my ability to create intuitive interfaces.', 'resumes/olivia_taylor_resume.pdf', '2025-07-19 13:05:00'),
(16, 9, 'Rejected', 'Technical skills are good but we need more cybersecurity-specific knowledge.', 'Cybersecurity is crucial in todays digital world. My software engineering background provides a solid foundation for learning security principles.', 'resumes/lucas_moore_resume.pdf', '2025-07-10 16:15:00'),
(17, 11, 'Pending', NULL, 'Environmental data analysis combines my love for data science with environmental advocacy. This role would allow me to contribute to sustainability efforts.', 'resumes/isabella_clark_resume.pdf', '2025-07-20 09:50:00'),
(18, 15, 'Accepted', 'Strong social media understanding and excellent communication skills.', 'Social media strategy is about storytelling and engagement. My experience managing university social accounts demonstrates my ability to build online communities.', 'resumes/noah_walker_resume.pdf', '2025-07-14 12:10:00'),
(19, 18, 'Pending', NULL, 'Quality assurance ensures software excellence. My analytical mindset and attention to detail make me well-suited for testing and improving software quality.', 'resumes/zoe_allen_resume.pdf', '2025-07-21 15:25:00'),
(16, 10, 'Rejected', 'Lack of required skill', 'Renewable energy projects with strong analytical skills.', 'resumes/lucas_moore_resume.pdf', '2025-07-10 16:15:00'),

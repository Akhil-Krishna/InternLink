-- InternLink Database Population Script

USE internlink;

-- STUDENTS (20 students)
INSERT INTO user (username, full_name,first_name,last_name, email, password_hash, profile_image, role, status) VALUES
('sarah.chen', 'Sarah Chen','Sarah','Chen', 'sarah.chen@student.uni.nz', '$2b$12$HejQuYpYzvLpW2A5pl7.MOJmic4S3DW2T4RteQMzHjTkM8r8cJRwq', 'sarah_chen.jpg', 'student', 'active'),
('james.wilson', 'James Wilson','James','Wilson', 'james.wilson@student.uni.nz', '$2b$12$gSGAr1qOu.lDbxt2.v3J2eym5.Ic4fqI../7cQtCAcza9FkA2E/Zi', 'james_wilson.jpg', 'student', 'active'),
('emily.martinez', 'Emily Martinez','Emily','Martinez', 'emily.martinez@student.uni.nz', '$2b$12$tR0RS.uV9pJ.lzFqPOSezu81Rx/UeVLIdNIA/0mgGCZibBJi..xNW', 'emily_martinez.jpg', 'student', 'active'),
('alex.thompson', 'Alex Thompson','Alex','Thompson', 'alex.thompson@student.uni.nz', '$2b$12$crJcLBNv34x95ufIxmo4.uvRO23tXovycFYd3tLp7837XqUn6Qd3i', 'alex_thompson.jpg', 'student', 'active'),
('priya.sharma', 'Priya Sharma','Priya' ,'Sharma','priya.sharma@student.uni.nz', '$2b$12$vOqommsSUvoE3wXmBLoQA.pncS2zcXuHmr2PwSiRR0oFbM8TI3HpC', 'priya_sharma.jpg', 'student', 'active'),
('david.brown', 'David Brown','David','Brown', 'david.brown@student.uni.nz', '$2b$12$GHiTwkYrkokw58j1FYyiBuTgu4do8L5Y1UIkucQ5dOvyuP2bvMypm', 'david_brown.jpg', 'student', 'active'),
('lisa.wang', 'Lisa Wang','Lisa','Wang', 'lisa.wang@student.uni.nz', '$2b$12$1ffIT7UietAsP/yCQL1yeO8.aJAKX72DUQGRcaAYY2CVhyK.u4zK2', 'lisa_wang.jpg', 'student', 'active'),
('michael.jones', 'Michael Jones','Michael','Jones', 'michael.jones@student.uni.nz', '$2b$12$j3Ap2BvVD6vc3CZAW1lX8Of2Iy4.Bxcw6qSedABQw.d4kxQrexCwu', 'michael_jones.jpg', 'student', 'active'),
('aisha.patel', 'Aisha Patel','Aisha','Patel', 'aisha.patel@student.uni.nz', '$2b$12$/zCtHapg1B0ZI5XpSjjcE.9tPcCOtb4fquVGb2ybDpxr01CWnpJPK', 'aisha_patel.jpg', 'student', 'active'),
('ryan.garcia', 'Ryan Garcia','Ryan','Garcia','ryan.garcia@student.uni.nz', '$2b$12$4tEqKA482lv633zjNrC1he6cFv4SxlGCDQFrtqokbLUMaIjrdjGnS', 'ryan_garcia.jpg', 'student', 'active'),
('natalie.kim', 'Natalie Kim','Natalie','Kim', 'natalie.kim@student.uni.nz', '$2b$12$e087zFrxkZMe4.xtJHYiEubkkeCnY9E266/QHNGQAC96KcAgbIc/C', 'natalie_kim.jpg', 'student', 'active'),
('tom.anderson', 'Tom Anderson','Tom','Anderson', 'tom.anderson@student.uni.nz', '$2b$12$OVwPNzuZeiLkqGY7yefvBOb7vcPhhlkvQWXjFpJwyJSiDZqUi48z6', 'tom_anderson.jpg', 'student', 'active'),
('sophia.rodriguez', 'Sophia Rodriguez','Sophia','Rodriguez', 'sophia.rodriguez@student.uni.nz', '$2b$12$DX9LrFlCXKKs.7S.zlrEY.yFh/AuPvNrdLk/C3jO02iqKEqpf8cpK', 'sophia_rodriguez.jpg', 'student', 'active'),
('ethan.lee', 'Ethan Lee','Ethan','Lee', 'ethan.lee@student.uni.nz', '$2b$12$uN4Dxfg4FEazSNXAOshV8.mpDK.EafhV8nVFFWpDcC2pvHs4YPmSC', 'ethan_lee.jpg', 'student', 'active'),
('olivia.taylor', 'Olivia Taylor','Olivia','Taylor', 'olivia.taylor@student.uni.nz', '$2b$12$FJMPwhHlz6Wl1OL.hqwl5u1XA7kWta5B9qlf5skOlS18QrlNJI4fy', 'olivia_taylor.jpg', 'student', 'active'),
('lucas.moore', 'Lucas Moore','Lucas','Moore', 'lucas.moore@student.uni.nz', '$2b$12$N7aV4YLeu1TZtRGwRjwaH.BCVSG5Z2NItoBHNdSov6uqoBGnTZvkG', 'lucas_moore.jpg', 'student', 'active'),
('isabella.clark', 'Isabella Clark','Isabella','Clark', 'isabella.clark@student.uni.nz', '$2b$12$n6MTBgQTth6ydw2BCV9dXu37f08GoXY2lokol/pPRZ8dfBgXXI7su', 'isabella_clark.jpg', 'student', 'active'),
('noah.walker', 'Noah Walker','Noah','Walker', 'noah.walker@student.uni.nz', '$2b$12$mwam7B8dGMhAze8FtlVOt.xfyEisFD8nvgY5XWchpLB4fF4ufSTtG', 'noah_walker.jpg', 'student', 'active'),
('zoe.allen', 'Zoe Allen','Zoe','Allen' ,'zoe.allen@student.uni.nz', '$2b$12$C10BCYsz3wQkt7epF.uvBe3VJ4I0Df1eEn6.m8bkbMn/A0ZO3sg5q', 'zoe_allen.jpg', 'student', 'active'),
('jacob.hill', 'Jacob Hill','Jacob','Hill', 'jacob.hill@student.uni.nz', '$2b$12$CEdQuD1ixzm9qX/TpFtpJONFzdN9gzKoqb5l1jj71a4VWrQre871i', 'jacob_hill.jpg', 'student', 'active');

-- EMPLOYERS (5 employers)
INSERT INTO user (username, full_name,first_name,last_name, email, password_hash, profile_image, role, status) VALUES
('techcorp.hr', 'Jessica Martinez','Jessica','Martinez', 'jessica.martinez@techcorp.co.nz', '$2b$12$SmdXSH/FCh0xRToBgaTENuMHTUWzHyaC6PhWeAPG/920aRN92FVKa', 'jessica_martinez.jpg', 'employer', 'active'),
('innovate.recruit', 'Mark Thompson','Mark','Thompson', 'mark.thompson@innovatesolutions.co.nz', '$2b$12$BHGEEXdx/B.CrBLC/iRhue/juMB3xOagWNweEjfIljXReEt18xFcG', 'mark_thompson.jpg', 'employer', 'active'),
('fintech.careers', 'Rachel Chen','Rachel','Chen', 'rachel.chen@fintechplus.co.nz', '$2b$12$mlJLaJH6tKGI2OmHUeAc6ORqISlc633MJ3F8ZlQimkpO/3CTy/F.W', 'rachel_chen.jpg', 'employer', 'active'),
('green.energy', 'Daniel Williams','Daniel','Williams', 'daniel.williams@greenenergy.co.nz', '$2b$12$xtLueyisgHXvnhm.mZpeQu2KbstdHBuWQStRIDCAejD1ulCK1r036', 'daniel_williams.jpg', 'employer', 'active'),
('media.creative', 'Sophie Brown','Sophie','Brown', 'sophie.brown@creativemedia.co.nz', '$2b$12$bF4EdAhq3sZjzODKOXbhc.0/QHq/t5/8i9EVBeJ3PmrfKKrA8SlvW', 'sophie_brown.jpg', 'employer', 'active');

-- ADMINISTRATORS (2 admins)
INSERT INTO user (username, full_name,first_name,last_name,email, password_hash, profile_image, role, status) VALUES
('admin.system', 'Aravind S','Aravind','S', 'admin@internlink.co.nz', '$2b$12$OKZ8.3wV6geZQZJ5F076MurqrqjVVQ3WhkhcjsBpn3TkaQv9WaNWW', 'admin_system.jpg', 'admin', 'active'),
('admin.support', 'Angel Thomas','Angel','Thomas','support@internlink.co.nz', '$2b$12$E/iuyElJKmVYJt8wusnovuBZqoFn6OzW.wfqZ2jbhJaZ6tELBXi1m', 'admin_support.jpg', 'admin', 'active');
-- Insert Student details


INSERT INTO student (user_id, university, course, resume_path) VALUES
(1, 'University of Auckland', 'Computer Science', 'sarah_chen_resume.pdf'),
(2, 'Victoria University of Wellington', 'Software Engineering', 'james_wilson_resume.pdf'),
(3, 'University of Canterbury', 'Information Systems', 'emily_martinez_resume.pdf'),
(4, 'Massey University', 'Data Science', 'alex_thompson_resume.pdf'),
(5, 'Auckland University of Technology', 'Computer Science', 'priya_sharma_resume.pdf'),
(6, 'University of Otago', 'Information Technology', 'david_brown_resume.pdf'),
(7, 'University of Waikato', 'Computer Science', 'lisa_wang_resume.pdf'),
(8, 'Victoria University of Wellington', 'Software Engineering', 'michael_jones_resume.pdf'),
(9, 'University of Auckland', 'Information Systems', 'aisha_patel_resume.pdf'),
(10, 'Auckland University of Technology', 'Data Science', 'ryan_garcia_resume.pdf'),
(11, 'University of Canterbury', 'Computer Science', 'natalie_kim_resume.pdf'),
(12, 'Massey University', 'Software Engineering', 'tom_anderson_resume.pdf'),
(13, 'University of Otago', 'Information Technology', 'sophia_rodriguez_resume.pdf'),
(14, 'University of Waikato', 'Computer Science', 'ethan_lee_resume.pdf'),
(15, 'Victoria University of Wellington', 'Data Science', 'olivia_taylor_resume.pdf'),
(16, 'University of Auckland', 'Software Engineering', 'lucas_moore_resume.pdf'),
(17, 'Auckland University of Technology', 'Information Systems', 'isabella_clark_resume.pdf'),
(18, 'University of Canterbury', 'Computer Science', 'noah_walker_resume.pdf'),
(19, 'Massey University', 'Information Technology', 'zoe_allen_resume.pdf'),
(20, 'University of Otago', 'Data Science', 'jacob_hill_resume.pdf');

-- Insert Employer details
INSERT INTO employer (user_id, company_name, company_description, website, logo_path) VALUES
(21, 'TechCorp Solutions', 'Leading technology solutions provider specializing in cloud computing and enterprise software development.', 'https://www.techcorp.co.nz', 'logos/techcorp_logo.png'),
(22, 'Innovate Solutions', 'Digital transformation consultancy helping businesses leverage cutting-edge technology for growth.', 'https://www.innovatesolutions.co.nz', 'logos/innovate_logo.png'),
(23, 'FinTech Plus', 'Financial technology startup developing innovative payment solutions and digital banking platforms.', 'https://www.fintechplus.co.nz', 'logos/fintech_logo.png'),
(24, 'Green Energy Corp', 'Renewable energy company focused on sustainable power solutions and environmental technology.', 'https://www.greenenergy.co.nz', 'logos/greenenergy_logo.png'),
(25, 'Creative Media Hub', 'Digital marketing and media production company creating engaging content for modern brands.', 'https://www.creativemedia.co.nz', 'logos/creativemedia_logo.png');

-- Insert Internships (20+ internships)
INSERT INTO internship (company_id, title, description, location, duration, skills_required, deadline, stipend, number_of_openings, additional_req, posted_date) VALUES
(1, 'Software Development Intern', 'Join our development team to work on cloud-based enterprise applications using modern technologies like React, Node.js, and AWS.', 'Auckland', '3 months', 'JavaScript, React, Node.js, Git', '2025-09-15', '$400/week', 2, 'Portfolio of personal projects required', '2025-07-01'),
(1, 'Data Analytics Intern', 'Analyze large datasets to provide business insights and develop automated reporting solutions using Python and SQL.', 'Auckland', '6 months', 'Python, SQL, Data Visualization, Statistics', '2025-09-30', '$450/week', 1, 'Experience with Pandas and Matplotlib preferred', '2025-07-03'),
(1, 'DevOps Engineering Intern', 'Learn infrastructure automation, CI/CD pipelines, and cloud deployment strategies in our DevOps team.', 'Auckland', '4 months', 'Linux, Docker, AWS, Git', '2025-10-01', '$420/week', 1, 'Basic understanding of containerization', '2025-07-05'),
(2, 'Frontend Developer Intern', 'Create responsive web interfaces and user experiences for our client projects using modern frontend frameworks.', 'Wellington', '3 months', 'HTML, CSS, JavaScript, Vue.js', '2025-09-20', '$380/week', 2, 'Design portfolio showcasing UI/UX work', '2025-06-28'),
(2, 'Mobile App Development Intern', 'Develop cross-platform mobile applications using React Native for iOS and Android platforms.', 'Wellington', '4 months', 'React Native, JavaScript, Mobile Development', '2025-10-05', '$400/week', 1, 'Published app or strong mobile project portfolio', '2025-07-02'),
(2, 'Digital Marketing Intern', 'Support digital marketing campaigns, content creation, and social media management for technology clients.', 'Wellington', '3 months', 'Social Media, Content Creation, Analytics', '2025-09-25', '$320/week', 1, 'Strong written communication skills', '2025-07-04'),
(3, 'Financial Technology Intern', 'Work on fintech applications including payment processing systems and financial data analysis tools.', 'Christchurch', '6 months', 'Java, Spring Boot, Financial Systems, SQL', '2025-10-10', '$480/week', 2, 'Interest in financial markets and technology', '2025-06-30'),
(3, 'Blockchain Development Intern', 'Explore blockchain technology and develop smart contracts for financial applications.', 'Christchurch', '4 months', 'Solidity, Ethereum, JavaScript, Cryptography', '2025-09-28', '$500/week', 1, 'Basic understanding of blockchain concepts', '2025-07-06'),
(3, 'Cybersecurity Intern', 'Learn about financial system security, penetration testing, and security compliance frameworks.', 'Christchurch', '5 months', 'Network Security, Python, Ethical Hacking', '2025-10-15', '$460/week', 1, 'Security certifications or coursework preferred', '2025-07-07'),
(4, 'Renewable Energy Systems Intern', 'Support the development of smart grid technology and energy management systems.', 'Hamilton', '4 months', 'Python, IoT, Data Analysis, Engineering', '2025-09-18', '$400/week', 2, 'Engineering or environmental science background', '2025-06-25'),
(4, 'Environmental Data Analyst Intern', 'Analyze environmental impact data and create sustainability reports for renewable energy projects.', 'Hamilton', '3 months', 'R, Python, Statistics, Environmental Science', '2025-10-20', '$380/week', 1, 'Environmental studies or related field', '2025-07-08'),
(4, 'Green Tech Software Intern', 'Develop software solutions for monitoring and optimizing renewable energy systems.', 'Hamilton', '6 months', 'C++, Python, Embedded Systems, MATLAB', '2025-09-12', '$440/week', 1, 'Interest in sustainable technology', '2025-06-27'),
(5, 'Digital Content Creation Intern', 'Create engaging digital content including videos, graphics, and interactive media for brand campaigns.', 'Dunedin', '3 months', 'Adobe Creative Suite, Video Editing, Design', '2025-10-08', '$350/week', 2, 'Portfolio of creative work required', '2025-07-09'),
(5, 'Web Development Intern', 'Build modern websites and web applications for creative industry clients using latest web technologies.', 'Dunedin', '4 months', 'HTML, CSS, JavaScript, WordPress, PHP', '2025-09-22', '$380/week', 1, 'Strong portfolio of web projects', '2025-07-10'),
(5, 'Social Media Strategy Intern', 'Develop and implement social media strategies for creative brands and analyze engagement metrics.', 'Dunedin', '3 months', 'Social Media Marketing, Analytics, Content Strategy', '2025-10-12', '$320/week', 1, 'Experience with social media platforms', '2025-07-11'),
(1, 'Machine Learning Intern', 'Work on AI and machine learning projects to enhance our software products with intelligent features.', 'Auckland', '5 months', 'Python, TensorFlow, Machine Learning, Mathematics', '2025-10-25', '$480/week', 1, 'Strong mathematical background and ML coursework', '2025-07-12'),
(2, 'UX/UI Design Intern', 'Design user interfaces and conduct user research to improve the usability of our digital products.', 'Wellington', '4 months', 'Figma, Adobe XD, User Research, Prototyping', '2025-09-30', '$400/week', 1, 'Design portfolio and user research experience', '2025-07-13'),
(3, 'Quality Assurance Intern', 'Test financial software applications and develop automated testing frameworks to ensure product quality.', 'Christchurch', '3 months', 'Software Testing, Selenium, Test Automation', '2025-10-18', '$360/week', 2, 'Attention to detail and analytical mindset', '2025-07-14'),
(4, 'Project Management Intern', 'Assist project managers in coordinating renewable energy projects and client communications.', 'Hamilton', '4 months', 'Project Management, Communication, MS Office', '2025-09-14', '$380/week', 1, 'Strong organizational and communication skills', '2025-07-15'),
(5, 'Video Production Intern', 'Produce promotional videos and documentaries for creative industry clients using professional equipment.', 'Dunedin', '6 months', 'Video Production, Final Cut Pro, Cinematography', '2025-10-05', '$420/week', 1, 'Video production portfolio and equipment knowledge', '2025-07-16');


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
(16, 10, 'Rejected', 'Lack of required skill', 'Renewable energy projects with strong analytical skills.', 'resumes/lucas_moore_resume.pdf', '2025-07-10 16:15:00');

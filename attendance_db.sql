USE se;

CREATE TABLE Student ( Student_ID varchar(10) unique,
                    Fname varchar(20),
                   Lname varchar(20),
                    Age int NOT NULL,
                    DOB date,
                    Pincode int,
                    Class int,
                    Section varchar(5),
                    Parent_ph bigint,
                    primary key(Student_ID)
);
insert into student( Student_ID ,Fname,Lname ,Age ,DOB ,Pincode ,Class ,Section ,Parent_ph)
values('CS123','Manoj','pothani',20,'2002-02-21',560087,5,'A',9876453627),
('CS234','sharada','bhat',19,'2003-04-30',560087,5,'A',9874563241),
('CS456','Anil','Ram',20,'2001-05-23',560098,5,'A',9876543098),
('CS878','Roopesh','Bhat',19,'2002-12-21',560006,5,'A',8787879098),
('CS900','Roopa','Ganesh',20,'2002-09-22',560007,5,'A',7778686678),
('EC121','Vinay','Shetty',21,'2001-09-21',500005,5,'B',6667890098),
('EC098','Sheya','Shetty',20,'2002-08-20',560097,5,'B',8889990776),
('ME123','Sachin','Shamkar',21,'2001-08-26',560008,5,'D',9990008876),
('CS734','Varsha','Shenoy',21,'2001-07-23',560006,5,'A',7777768909),
('ME111','Darshan','Shetty',20,'2002-09-23',560097,5,'D',9900009870);
select * from student;
                    
CREATE TABLE Teacher ( Teacher_ID varchar(10) unique,
						Fname varchar(20),
                        Lname varchar(20),
                        Ph_no varchar(10),
                        Email varchar(30)
                        Class varchar(5),
                        primary key(Teacher_ID)
);
insert into TEACHER(Teacher_ID ,Fname ,Lname ,Ph_no ,Email, Class)
values('CS34','sachin','arya',8765498765,'sachin.arya@gmail.com'),
('CS21','anupama','bhat',7654984532,'anu.bhat@gmail.com'),
('CS11','Anil','Nagraj',8887903334,'Anil.Nag@gmail.com'),
('EC21','Anuradha','Shenoy',6667543219,'anuradha.shenoy23@gmail.com'),
('EC12','Raghu','Ram',8888976534,'Raghu.ram@gmial.com'),
('ME21','Vikas','Rajan',9000987890,'vikas.raj87@gmail.com'),
('ME11','Akash','Ranjan',8889022234,'Akash.ranjan@gmail.com');
select * from teacher;


CREATE TABLE Attendance (
						            Student_ID varchar(10),
                        Class int,
                        Section varchar(5),
                        Teacher_ID varchar(10),
						            Att_date datetime,
                        Attendance char default 'N',
                        foreign key(Teacher_ID) references Teacher(Teacher_ID),
                        foreign key(Student_ID) references Student(Student_ID)
);
insert into Attendance 
values('CS123',5,'A','CS301','CS21','2012-11-29 10:20','Y'),('CS123',5,'A','CS302','CS34','2012-11-29 11:20','N'),
('CS123',5,'A','CS303','CS11','2012-11-29 01:20','Y'),
('CS234',5,'A','CS301','CS21','2012-11-29 10:20','Y'),('CS234',5,'A','CS302','CS34','2012-11-29 11:20','Y'),
('CS234',5,'A','CS303','CS11','2012-11-29 01:20','Y'),
('CS456',5,'A','CS301','CS21','2012-11-29 10:20','N'),('CS456',5,'A','CS302','CS34','2012-11-29 11:20','Y'),
('CS456',5,'A','CS303','CS11','2012-11-29 01:20','Y'),
('CS878',5,'A','CS301','CS21','2012-11-29 10:20','N'),('CS878',5,'A','CS302','CS34','2012-11-29 11:20','N'),
('CS878',5,'A','CS303','CS11','2012-11-29 01:20','Y'),
('CS900',5,'A','CS301','CS21','2012-11-29 10:20','Y'),('CS900',5,'A','CS302','CS34','2012-11-29 11:20','Y'),
('CS900',5,'A','CS303','CS11','2012-11-29 01:20','Y');

select * from Attendance;

/Updating the attendamce/
update attendance
set attendance = 'Y'
where student_id = 'CS123'AND SUB_ID = 'CS302';

/*deleting the student
DELETE from student
where student_id = 'cs123';
select * from student;*/

/view attendance/
CREATE VIEW Attendance_report_234 AS
SELECT * FROM attendance
WHERE student_id = 'CS234';
select * from attendance_report_234;

UPDATE Student set Age = FLOOR(DATEDIFF(CURRENT_DATE,DOB)/365)
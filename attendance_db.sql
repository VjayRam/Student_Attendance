-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Dec 25, 2015 at 12:02 PM
-- Server version: 5.6.16
-- PHP Version: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `attendance_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance_table`
--

CREATE TABLE IF NOT EXISTS `attendance_table` (
  `program` varchar(64) NOT NULL,
  `semester` varchar(64) NOT NULL,
  `subject` varchar(64) NOT NULL,
  `teacher` varchar(64) NOT NULL,
  `std_roll_no` int(11) NOT NULL,
  `student_name` varchar(100) NOT NULL,
  `attendance` varchar(8) NOT NULL,
  `attd_date` date NOT NULL,
  `TeacherId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendance_table`
--

INSERT INTO `attendance_table` (`program`, `semester`, `subject`, `teacher`, `std_roll_no`, `student_name`, `attendance`, `attd_date`, `TeacherId`) VALUES
('MCS', 'Term-III', 'OOP', 'Miss Rabeal Zahra', 1, 'salma', 'P', '2015-11-11', NULL),
('MCS', 'Term-III', 'MP', 'Sir javed', 3, 'farah', 'A', '0000-00-00', NULL),
('MS', 'Term-IV', 'MP', 'Miss Sadia Khattak', 4, 'wasim', 'A', '0000-00-00', NULL),
('MCS', 'Term-III', 'OOP', 'Miss Rabeal Zahra', 6, 'fared', 'A', '0000-00-00', NULL),
('MS', 'Term-III', 'C++', 'Dr.Zubair', 9, 'salman', 'A', '0000-00-00', NULL),
('MS', 'Term-III', 'OOP', 'Others', 21, 'farhin', 'P', '0000-00-00', NULL),
('PHD', 'Term-I', 'Others', 'Dr.Zubair', 33, 'fff', 'A', '0000-00-00', NULL),
('BSSC', 'Term-I', 'C++', 'Dr.Zubair', 76, 'hhhh', 'A|', '0000-00-00', NULL),
('P.HD', 'Term-I', 'Others', 'Others', 79, 'sdsfs', 'P', '0000-00-00', NULL),
('MS', 'Term-V', 'OOP', 'Dr.Zubair', 16, 'gggg', 'A', '0000-00-00', NULL),
('MCS', 'Term-VIII', 'C++', 'Others', 55, 'uu', 'Array', '0000-00-00', NULL),
('PHD', 'Term-V', 'Others', 'Others', 66, 'qqq', 'Array', '0000-00-00', NULL),
('MS', 'Term-IV', 'MP', 'Miss Rabeal Zahra', 98, 'jj', 'A', '0000-00-00', NULL),
('MCS', 'Term-IV', 'C++', 'Dr.Zubair', 54, 'fff', 'A', '0000-00-00', NULL),
('BSSC', 'Term-IV', 'C++', 'Miss Sadia Khattak', 98, 'vv', 'P', '0000-00-00', NULL),
('P.HD', 'Term-II', 'Java', 'Miss Rabeal Zahra', 87, 'sahar', 'A', '0000-00-00', NULL),
('MS', 'Term-III', 'OOP', 'Miss Sadia Khattak', 87, 'shabir', 'A', '0000-00-00', NULL),
('BSSC', 'Term-I', 'C++', 'Dr.Zubair', 67, 'hhhh', 'P', '0000-00-00', NULL),
('BSCS', 'Term-III', 'Java', 'Sir javed', 41, 'Ahmad', 'A', '0000-00-00', NULL),
('BSSC', 'Term-III', 'C++', 'Sir javed', 88, 'sasa', 'A', '0000-00-00', NULL),
('BSCS', 'Term-I', 'C++', 'Dr.Zubair', 66, 'yuy', 'P', '0000-00-00', NULL),
('BSSC', 'Term-II', 'Java', 'Sir javed', 17, 'farahh', 'A', '0000-00-00', NULL),
('MCS', 'Term-III', 'MP', 'Miss Sadia Khattak', 30, 'wasim', 'A', '0000-00-00', NULL),
('MCS', 'Term-II', 'Java', 'Sir javed', 9, 'razaq', 'P', '0000-00-00', NULL),
('BSCS', 'Term-I', 'Java', 'Sir javed', 10, 'sardar', 'P', '0000-00-00', NULL),
('P.HD', 'Term-II', 'OOP', 'Miss Rabeal Zahra', 16, 'noor', 'A', '0000-00-00', NULL),
('MCS', 'Term-II', 'Java', 'Sir javed', 21, 'farhin', 'P', '0000-00-00', NULL),
('BSCS', 'Term-II', 'MP', 'Miss Rabeal Zahra', 1, 'j', 'A', '2015-11-11', NULL),
('MS', 'Term-V', 'OOP', 'Dr.Zubair', 123, 'dv', 'P', '0000-00-00', NULL),
('MCS', 'Term-III', 'Others', 'Others', 16, 't', 'P', '0000-00-00', NULL),
('BSCS', 'Term-VIII', 'OOP', 'Miss Rabeal Zahra', 1, 'rabia', 'P', '2015-11-11', NULL),
('BSSC', 'Term-I', 'C++', 'Dr.Zubair', 18, 'usra', 'A', '0000-00-00', NULL),
('BSCS', 'Term-V', 'MP', 'Sir javed', 1, 'hh', 'A', '2015-11-11', NULL),
('BSSC', 'Term-I', 'C++', 'Dr.Zubair', 1, 'rezwan', 'P', '2015-11-11', NULL),
('MCS', 'Term-I', 'OOP', 'Miss Rabeal Zahra', 2, 'Afsana', 'P', '2015-11-11', NULL),
('MCS', 'Term-III', 'Java', 'Dr.Zubair', 2, 'Ali', 'P', '2015-11-10', NULL),
('P.HD', 'Term-IV', 'OOP', 'Sir javed', 5, 'sajjad', 'A', '2015-11-10', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `semester_table`
--

CREATE TABLE IF NOT EXISTS `semester_table` (
  `semester_no` varchar(32) NOT NULL,
  `subject` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `semester_table`
--

INSERT INTO `semester_table` (`semester_no`, `subject`) VALUES
('Term-II', 'java');

-- --------------------------------------------------------

--
-- Table structure for table `student_table`
--

CREATE TABLE IF NOT EXISTS `student_table` (
  `std_roll_no` int(11) NOT NULL AUTO_INCREMENT,
  `student_name` varchar(32) CHARACTER SET latin1 NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(6) CHARACTER SET latin1 NOT NULL,
  `email` varchar(64) CHARACTER SET latin1 NOT NULL,
  `phone` varchar(32) CHARACTER SET latin1 DEFAULT NULL,
  `address` varchar(255) CHARACTER SET latin1 NOT NULL,
  `Session` varchar(40) COLLATE latin1_general_ci DEFAULT NULL,
  `Program` varchar(40) COLLATE latin1_general_ci DEFAULT NULL,
  `Semester` varchar(40) COLLATE latin1_general_ci DEFAULT NULL,
  PRIMARY KEY (`std_roll_no`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=5 ;

--
-- Dumping data for table `student_table`
--

INSERT INTO `student_table` (`std_roll_no`, `student_name`, `dob`, `gender`, `email`, `phone`, `address`, `Session`, `Program`, `Semester`) VALUES
(2, 'zaman', '1990-12-23', 'male', 'zohra@yahoo.com', '0345831865', 'kbkff', '2012-2015', 'Bcs', '2nd'),
(4, 'Ali', '1992-08-06', 'male', 'ali@gmail.com', '0345831067', 'kpk-pak', '2012-2015', 'Bcs', '2nd');

-- --------------------------------------------------------

--
-- Table structure for table `subject_table`
--

CREATE TABLE IF NOT EXISTS `subject_table` (
  `subject_no` int(11) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(32) NOT NULL,
  `teacher_name` varchar(64) NOT NULL,
  `field` varchar(8) NOT NULL,
  `semester` varchar(32) NOT NULL,
  PRIMARY KEY (`subject_no`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `subject_table`
--

INSERT INTO `subject_table` (`subject_no`, `subject_name`, `teacher_name`, `field`, `semester`) VALUES
(1, 'C++', 'Sir javed', 'BSCS', '4th'),
(2, 'OOP', 'Dr.Zubair', 'MCS', '3rd'),
(3, 'MP', 'Dr.Zubair', 'BSCS', '6th'),
(4, 'OOP', 'Miss Sadia Khattak', 'BSCS', '5th'),
(5, 'C++', 'Miss Rabeal Zahra', 'BSCS', '2nd'),
(6, 'C++', 'Others', 'BSCS', '2nd'),
(7, 'Java', 'Miss Sadia Khattak', 'MCS', '3rd'),
(8, 'Network', 'TEst', 'CS', '7');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_attendence`
--

CREATE TABLE IF NOT EXISTS `tbl_attendence` (
  `attID` int(11) NOT NULL AUTO_INCREMENT,
  `StudentRollNumber` int(11) NOT NULL,
  `SubjectId` int(11) NOT NULL,
  `Attendence` varchar(11) NOT NULL,
  `Date` datetime NOT NULL,
  PRIMARY KEY (`attID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Dumping data for table `tbl_attendence`
--

INSERT INTO `tbl_attendence` (`attID`, `StudentRollNumber`, `SubjectId`, `Attendence`, `Date`) VALUES
(1, 2, 1, 'P', '2015-12-01 00:00:00'),
(2, 2, 1, 'P', '2015-12-02 00:00:00'),
(3, 2, 1, 'A', '2015-12-01 00:00:00'),
(4, 2, 1, 'A', '2015-12-03 00:00:00'),
(5, 2, 1, 'P', '2015-12-04 00:00:00'),
(6, 4, 2, 'A', '2015-12-10 00:00:00'),
(7, 4, 3, 'A', '2015-12-10 00:00:00'),
(8, 4, 2, 'A', '2015-12-17 00:00:00'),
(9, 4, 3, 'A', '2015-12-15 00:00:00'),
(10, 4, 3, 'A', '2015-12-15 00:00:00'),
(11, 4, 7, 'A', '2015-12-01 00:00:00'),
(12, 2, 8, 'P', '2015-12-11 00:00:00'),
(13, 2, 8, 'A', '2015-12-18 00:00:00'),
(14, 5, 7, 'P', '2015-12-24 08:58:20'),
(15, 5, 8, 'A', '2015-12-24 08:58:45'),
(16, 4, 4, 'A', '2015-12-24 09:14:09'),
(17, 4, 4, 'A', '2015-12-24 09:14:31'),
(18, 2, 8, 'P', '2015-12-25 11:44:15');

-- --------------------------------------------------------

--
-- Table structure for table `teacher_table`
--

CREATE TABLE IF NOT EXISTS `teacher_table` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(8) NOT NULL,
  `email` varchar(64) NOT NULL,
  `phone` varchar(32) DEFAULT NULL,
  `degree` varchar(32) NOT NULL,
  `salary` varchar(64) NOT NULL,
  `address` text NOT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `teacher_table`
--

INSERT INTO `teacher_table` (`teacher_id`, `first_name`, `last_name`, `dob`, `gender`, `email`, `phone`, `degree`, `salary`, `address`) VALUES
(2, 'Ahmad', 'Javed', '1983-02-12', '-------s', 'javed@yahoo.com', '03312567814', '-------select-------', '70000', 'kohat-pakistan'),
(3, 'Sadia', 'Khattak', '1983-02-12', 'Female', 'khattak@yahoo.com', '033125678786', 'Bachelor', '1200000', 'kpk-peshawar'),
(4, 'Rabeal', ' Zahra', '2014-07-22', 'Female', 'rab@gmail.com', '------', 'MS', '40000', 'di khan'),
(5, 'Zubair', 'ahmad', '2015-12-18', 'male', 'zubair@gmai.com', '9089998', 'MS', '80000000', 'Di khan');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

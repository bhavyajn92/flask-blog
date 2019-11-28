-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2019 at 07:34 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `firstattempt`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(1, 'bhavya', '8989765456', 'hello this meesahe', '2019-11-25 12:45:24', 'bkjb@jkl.com'),
(2, 'vegerve', 'gertgege', 'geg4eg', '2019-11-25 12:45:46', 'gegeg'),
(3, 'fwrfwrf', 'fwefwe', 'fwefw', '2019-11-25 16:01:47', 'wefeew2fw'),
(4, 'fwewe', 'fwfw', 'fwefwef', '2019-11-26 10:12:45', 'fewfw'),
(5, 'dwefwefwe', 'fwfweef', 'wffwefwe', '2019-11-26 10:14:23', 'fwefwef'),
(6, 'de2dwed', 'fwefwe', 'fwefwef', '2019-11-26 10:16:01', 'dwdwef');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `subtitle` varchar(100) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `img_file` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `posted_by` varchar(50) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`sno`, `title`, `subtitle`, `slug`, `img_file`, `content`, `posted_by`, `date`) VALUES
(1, 'This', 'subtitle1', 'first-post', 'tt', 'this is my first post na di am very excited about this post', 'bhavya', '2019-11-26 15:06:14'),
(2, 'Post2', 'subtitle2', 'second-post', '', 'Post2', 'BHAVYA JAIN', '2019-11-25 15:26:26'),
(3, 'post3', 'subtitle3', 'third-post', '', 'post3', 'BHAVYA JAIN', '2019-11-25 15:26:59'),
(4, 'post4', 'subtitle4', 'forth-post', '', 'post4', 'BHAVYA JAIN', '2019-11-25 15:27:24'),
(5, 'post5', 'subtitle5', 'fifth-post', '', 'post5', 'BHAVYA JAIN', '2019-11-25 15:27:59'),
(6, 'Post6', 'Subtitle6', 'sixth-post', '', 'post', 'Bhavya Jain', '2019-11-25 17:08:45'),
(7, 'Post7', 'Subtitle7', 'seventh-post', '', 'post', 'Bhavya Jain', '2019-11-25 17:10:43'),
(8, 'Post8', 'Subtitle8', 'eigth-post', '', 'post', 'Bhavya Jain', '2019-11-25 17:10:43'),
(10, 'Post10', 'Subtitle10', 'tenth-post', '', 'post', 'Bhavya Jain', '2019-11-25 17:10:43'),
(11, 'Post11', 'Subtitle11', 'eleventh-post', 'about-bg.jpg', 'post', 'Bhavya Jain', '2019-11-25 17:10:43'),
(12, 'Post12', 'Subtitle12', 'twelth-post', 'about-bg.jpg', 'post1', 'bhavya', '2019-11-26 14:33:08');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

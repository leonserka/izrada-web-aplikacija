-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 26, 2025 at 01:10 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ducan2`
--

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `session_id` int(200) NOT NULL,
  `data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sessions`
--

INSERT INTO `sessions` (`session_id`, `data`) VALUES
(32, '{\"user_id\": 23, \"Introduction\": \"not\", \"Calculus1\": \"not\", \"Computerusage\": \"not\", \"Digitalandmicroprocessortechnology\": \"not\", \"Databases\": \"not\", \"Calculus2\": \"not\", \"Datastructuresandalghoritms\": \"not\", \"Computerarchitecture\": \"not\", \"Informationsystemsdesign\": \"not\", \"Calculus3\": \"not\", \"ServerArchitecture\": \"not\", \"Computeranddatasecurity\": \"not\"}'),
(37, '{\"user_id\": 23, \"Introduction\": \"not\", \"Calculus1\": \"not\", \"Computerusage\": \"not\", \"Digitalandmicroprocessortechnology\": \"not\"}'),
(39, '{\"user_id\": 23}');

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `subject_id` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `ects` int(200) NOT NULL,
  `year` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`subject_id`, `name`, `ects`, `year`) VALUES
(1, 'Introduction', 6, 1),
(2, 'Calculus1', 7, 1),
(3, 'Computerusage', 5, 1),
(4, 'Digitalandmicroprocessortechnology', 6, 1),
(5, 'Databases', 6, 2),
(6, 'Calculus2', 7, 2),
(7, 'Datastructuresandalghoritms', 5, 2),
(8, 'Computerarchitecture', 6, 2),
(9, 'Informationsystemsdesign', 5, 3),
(10, 'Calculus3', 7, 3),
(11, 'ServerArchitecture', 6, 3),
(12, 'Computeranddatasecurity', 6, 3);

-- --------------------------------------------------------

--
-- Table structure for table `upisni_list`
--

CREATE TABLE `upisni_list` (
  `id` int(11) NOT NULL,
  `id_studenta` int(200) NOT NULL,
  `id_predmeta` int(11) DEFAULT NULL,
  `status` enum('not','enr','pass') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `upisni_list`
--

INSERT INTO `upisni_list` (`id`, `id_studenta`, `id_predmeta`, `status`) VALUES
(170, 28, 1, 'enr'),
(171, 28, 2, 'enr'),
(172, 28, 3, 'enr'),
(173, 28, 4, 'enr'),
(178, 29, 1, 'enr'),
(179, 29, 2, 'enr'),
(180, 29, 3, 'enr'),
(181, 29, 4, 'enr'),
(182, 29, 5, 'enr'),
(183, 29, 6, 'enr'),
(184, 29, 7, 'enr'),
(185, 29, 8, 'enr');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` binary(64) NOT NULL,
  `uloga` enum('student','admin') NOT NULL DEFAULT 'student'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `email`, `password`, `uloga`) VALUES
(23, 's059741', 'leonserka4@gmail.com', 0x0c5520d33a777f4dc6837faf2eecbd503905835cfcc1775eea3194a8d65ba5baf6b3566f2218ed838e2f4a06c7268459ddd20691b87d9cad1bc1735c69ea147f, 'admin'),
(24, 'aaa', 'leonserka422@gmail.com', 0x02f6d4fb92211462f0f0376fa612fbcc892700ad1b3efaee218b3405bd41d5ef6b60791c3fa6d0dd75a0b48b6441b1c9a090b11a78e27f640c6c83ed77fe3597, 'student'),
(27, 'joelhoffm523', 'leonserka4222@gmail.com', 0x30ad6f2fc04e683f0be9b294f8a1e99d39d79cde0d0f8fe0ad7228bd296c52ef28e4facdc7ff7c4e98313963034a9fbbc770b17bde76ee83787776c985179fba, 'student'),
(28, 'aa', 'leonserkaaa4@gmail.com', 0x4ca9bfe661bb6eff4479d00c96f3a081756401e0b556ef15b5c34cb97a2b7ed4df361f85cc2d1e5a403323ca1a269c549f4a812321e8dcf5b0c2c9a735a6724d, 'student'),
(29, 'leon', 'leonserka42223@gmail.com', 0x284cee67bb23c8d35010295698795de48e4a7ae0a541b64636a7cab0852adf60daedbf66cf69a153bce108922572cb90a05c4239204d42af44ab5a06dddccab8, 'student');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`session_id`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`subject_id`);

--
-- Indexes for table `upisni_list`
--
ALTER TABLE `upisni_list`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_studenta_2` (`id_studenta`),
  ADD KEY `id_studenta_3` (`id_studenta`),
  ADD KEY `id_studenta_4` (`id_studenta`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `session_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `subject_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `upisni_list`
--
ALTER TABLE `upisni_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=186;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `upisni_list`
--
ALTER TABLE `upisni_list`
  ADD CONSTRAINT `upisni_list_ibfk_1` FOREIGN KEY (`id_studenta`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `upisni_list_ibfk_2` FOREIGN KEY (`id_predmeta`) REFERENCES `subjects` (`subject_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

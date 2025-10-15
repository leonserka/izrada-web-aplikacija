-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 24, 2025 at 12:04 AM
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
(19, '{\"user_id\": 22}'),
(20, '{\"user_id\": 22}'),
(24, '{\"user_id\": 26}'),
(29, '{\"user_id\": 26, \"Introduction\": \"enrolled\", \"Calculus1\": \"enrolled\", \"Computerusage\": \"not selected\", \"Digitalandmicroprocessortechnology\": \"enrolled\"}');

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `ects` int(11) NOT NULL,
  `year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`id`, `name`, `ects`, `year`) VALUES
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
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` binary(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES
(22, 's059741', 'leonserka4@gmail.com', 0x244d7a1cdbc6f2a0ee5cbdbba2ff5b272b783b1f5e9203a3ee64e73bc5ec78b1a9696ed6236998af07bbded6857af09f82a9a1c30c8dd10b02caa6ac8ac67806),
(23, 's059741', 'leonserka444@gmail.com', 0xc3d80ecc7424c38ab17ce76a669eaebddc90c8844d27dd620bb3ba996d968a455f5bd60a4752e7400593566fe36a1225569289972fa55c7ddd019c3085d74d39),
(24, 'chrnuillath', 'leonserka42@gmail.com', 0x61d3a2f0716d64fde2b144a70cef78333123d049918f1808782961c1590e9730c3f8c14471d281ac3744f87ceba00ce0867793ba80e63d061b6dc4edb0b367e9),
(26, 'aaa', 'leonserkaa4@gmail.com', 0xaaccf93405925856dc9732499b8663e6073e80982f194622af07bddec6c788935ab7e2fe4b25445568e63b68f43e9cffc0df33a1864c6bb7ed57d7c36307e8a9),
(27, 'joelhoffm523', 'leonserka411@gmail.com', 0x9f0558cfa6965e19d2c4d06cc561b67abd3dac6846429d5b6536b49b6c4df25fd51ff3367e074b3c84ecd3a87e8950518652a5fd191de5ef8802b1443c9e0f38),
(30, 's059741', 'leonserka4234@gmail.com', 0x59360e58deae1544aa85e831492a94c250daa4fd20c51ff06f254d03aa8f39e9d1c1b570e90eae424f380593883dbdd6190d69cba9d78e53366021bdab389dd4),
(31, 'aaa', 'leonserka114@gmail.com', 0x8f789d37e28d05c793c79de9d718547c811430394df673bf6099b72f4b220c2dfe39a5e8097354475718d48756688d76c5e776cf9f4cd87598776a664c0df98f),
(32, 'aaa', 'leonserka1114@gmail.com', 0xdfe1cc8df3d71dbf645146afa76c3810c57ea31abe52b8f0330e375589a9cea8333b608e0b2dab652fde986f800846a9d8cbdde485cbec1340779d4d299619d4);

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
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `password` (`password`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `session_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

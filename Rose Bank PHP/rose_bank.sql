-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 18, 2021 at 04:25 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rose_bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `id` int(11) NOT NULL,
  `branch` varchar(255) NOT NULL,
  `transaction_type` varchar(255) NOT NULL,
  `id_number` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `full_address` varchar(255) NOT NULL,
  `mobile_number` varchar(15) NOT NULL,
  `email` varchar(255) NOT NULL,
  `time_stamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`id`, `branch`, `transaction_type`, `id_number`, `first_name`, `last_name`, `full_address`, `mobile_number`, `email`, `time_stamp`) VALUES
(1, 'avonlea', 'teller', 'EN862348', 'simpson', 'chiwashira', '384 stand poort road twinlakes', '+263712525171', 'simcee58@gmail.com', '2020-11-28 13:59:42'),
(2, 'masvingo', 'western union', 'EN862348', 'simpson', 'chiwashira', '384 stand poort road twinlakes', '+263712525171', 'sim@gmail.com', '2020-11-28 14:00:18'),
(5, 'masvingo', 'Customer Service', 'en8673255', 'Godfrey', 'Marimbire', '2nd Floor BB House', '+263773835303', 'godfrey@crocoholdings.co.zw', '2020-12-02 10:25:54'),
(6, 'belvedere', 'Customer Service', 'en8673255', 'IRENE', 'CHIWASHIRA', '141 Eastfield Road, Louth', '+905338775472', 'irenechiwaz@hotmail.co.uk', '2020-12-14 11:50:23');

-- --------------------------------------------------------

--
-- Table structure for table `customer_users`
--

CREATE TABLE `customer_users` (
  `id` int(11) NOT NULL,
  `branch` varchar(255) NOT NULL,
  `account_type` varchar(255) NOT NULL,
  `account_number` varchar(255) NOT NULL,
  `balance` float NOT NULL,
  `idnum` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `full_address` varchar(255) NOT NULL,
  `mobile_number` varchar(15) NOT NULL,
  `email` varchar(255) NOT NULL,
  `passwordd` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer_users`
--

INSERT INTO `customer_users` (`id`, `branch`, `account_type`, `account_number`, `balance`, `idnum`, `first_name`, `last_name`, `full_address`, `mobile_number`, `email`, `passwordd`, `created_at`) VALUES
(1, 'avo', 'sav', '1000', 150, 'EN862350', 'simpson', 'chiwashira', '384 stand poort road twinlakes', '+263712525171', 'simcee@gmail.com', '$2y$10$EqFvAi7lIw3zJwAfAaV/VOSqi1gkSj.XvA5MFpqPj.X7/vAFFKKC.', '2021-01-05 13:10:07'),
(2, 'norton', 'savings', '1001', 150, 'EN862350', 'simpson', 'chiwashira', '384 stand poort road twinlakes', '+263712525171', 'simcee@gmail.com', '$2y$10$yzQfykPYM32U9U6IDn7Ew.mZbbGDUfjFRni.bMbe0yOSRN.0fHmRO', '2021-01-05 13:10:07'),
(4, 'avonlea', 'savings', '5000', 150, 'EN862348', 'shareena', 'sikander', '384 stand poort road twinlakes', '+263712525171', 'simcee@gmail.com', '$2y$10$.eYOnmhIKIfs0dL3wu35Zem/sp0eOfqIocI5gFKZwnTFkE5CXcYAW', '2021-01-05 13:10:07'),
(6, 'avonlea', 'Mastercard Account', '6', 1, 'EN862351', 'manl', 'zahid', 'cyprus', '90533', 'manza@gmail.com', '$2y$10$mgjJ16KkXkUzo9JBMyCzVu5vU.6Gc0XR7jMu154jwsuRLTifwAyEO', '2020-11-28 11:41:55'),
(7, 'avonlea', '*Account Type', '6000', 500, 'en8673253', 'farai', 'chizinga', 'Gonyeli/ Yeniikent', '+905338775472', 'sezisokut@gmail.com', '$2y$10$4ns/utol6IbncdSm.77cle1n9gjgZL2HlcBCvbA222k22StCJEct.', '2020-12-02 09:53:43'),
(8, '*Select Branch', '*Account Type', '6001', 20, 'en8673254', 'samantha', 'Gumbo', '39 POORT ROAD, TWINLAKES PARK, NORTON', '+263773835303', 'sam@crocoholdings.co.zw', '$2y$10$AV65Mvx4UNA/5.lDxzL10uNdOoTyvR9WuIET0wAw9N3lX3UZdWcUK', '2020-12-02 10:23:57'),
(9, 'gwabalanda', 'nostro', '5050', 500, 'en8673258', 'Nicole', 'Tsikai', 'st martins', '+263776022212', 'nickt@123.co.zw', '$2y$10$yY7EZFednyJhkam7fC4dKu0.SM/PuCuwFP9Rm0JouDChT2fBCmlpS', '2020-12-14 12:03:07'),
(10, 'avonlea', 'Mastercard Account', '6060', 50, 'dn86', 'tapera', 'chiwashira', '39 POORT ROAD, TWINLAKES PARK', '+905338775472', 'btchiwashira@it.co.zw', '$2y$10$lIHo/dnoaoQR56qtK1YeIOuGBPmTc7dA5n7oLzYT2nHm.PPUEZsL.', '2020-12-22 15:04:15'),
(11, 'rhodesville', 'nostro', '5000000', 500, 'dn63', 'tarrek', 'amro', 'yakin dogu ', '+905338775472', 'tamro@gmail.com', '$2y$10$sjGRdH/gyKpLvSslakjzv.Iz/6AA8NohI6gVeKotAmIL5kIYBpatq', '2021-01-05 17:38:03'),
(12, 'norton', 'visa', '500002', 125, 'en12', 'trish', 'chiwashira', '39 POORT ROAD, TWINLAKES PARK, NORTON', '01111111', 'trishc@gmail.com', '$2y$10$1GMLazAOdG9fopsuVvw8EeEJ8j69/IwRi372WRkD3UwgJmIJ/u5lO', '2021-01-03 08:29:30'),
(14, 'borrowdale', 'visa', '606060', 1000, 'cn54', 'rumbidzai', 'md', 'borrowdale brooke', '+27458155161615', 'rmd@email.com', '$2y$10$mAPYUUj.bcVUqdWg/ws86uWIanwL6pZ//r/rxzWsgd5eKyek8Y0IC', '2021-01-05 17:44:39'),
(16, 'jameson', 'nostro', '7000', 500, 'SB97', 'Saba', 'Elgammudi', '39 POORT ROAD, TWINLAKES PARK', '0548861789', 'sababaset@gmail.com', '$2y$10$9fhuIr6HQEHEMRJyueHhYuLcqdw3hG0/bNdTV1ttC1e/KCzWKqB52', '2021-01-15 11:41:13'),
(18, 'gwabalanda', 'nostro', '300018', 600, 'ng99', 'juanita', 'jidai', 'yakin dogu universitesi', '053389789789', 'jidai@gmail.com', '$2y$10$ofJ/nanO7wawt1TKPGTDEePTzlpOO7DHSc/L1fDKHhMykXeXciO0O', '2021-01-15 12:30:51'),
(23, 'belvedere', 'nostro', '66666', 100, 'en8675', 'tawanda', 'chiwashira', 'NEAR EAST UNIVERSITY', '0622686', 'chiwashirasimpson@gmail.com', '$2y$10$UWTlGtw7JbNjXKfRZ1023OMS0xVRR5GIRJ9l7z8JMQsmW6QWaMu1G', '2021-01-15 20:06:58'),
(24, 'norton', 'nostro', '56666', 5000, '21-2002418', 'taperaa', 'brian', 'chiwashira residence', '+263555', 'taperabrian0142@gmail.com', '$2y$10$3PV./LIFdBZ3ZBJERd6kseZ7tzW3.0WhX68SQYPuxkpRNMmwHMAXm', '2021-01-16 12:35:31');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `created_at`) VALUES
(1, 'irenechiwaz@hotmail.co.uk', '$2y$10$CsS3oR/4Fa0zfmJ3e9Cv.OGoTob9Kk6Ki2IiIVinwzZR1meVtB3Ku', '2021-01-18 11:29:58');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer_users`
--
ALTER TABLE `customer_users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `customer_users`
--
ALTER TABLE `customer_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 15, 2025 at 09:00 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `invoice_generator`
--

-- --------------------------------------------------------

--
-- Table structure for table `customerdetails`
--

CREATE TABLE `customerdetails` (
  `id` int(11) NOT NULL,
  `companyName` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `mobileNum` varchar(14) NOT NULL,
  `email` varchar(100) NOT NULL,
  `GSTIN` varchar(15) NOT NULL,
  `address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customerdetails`
--

INSERT INTO `customerdetails` (`id`, `companyName`, `name`, `mobileNum`, `email`, `GSTIN`, `address`) VALUES
(1, 'abc', 'raj patel', '+918899224466', 'abc@gmail.com', 'QGDTS2749USB2H@', '12,abc shade, GIDC, ahmedabad'),
(2, 'xyz enterprice', 'meet jain', '889766452388', 'meet@gmail.com', 'SDFGH678HNJ6B', '33, GIDC akwada, bhavnagar');

-- --------------------------------------------------------

--
-- Table structure for table `owncompany`
--

CREATE TABLE `owncompany` (
  `id` int(11) NOT NULL,
  `companyName` varchar(60) NOT NULL,
  `name` varchar(100) NOT NULL,
  `GSTIN` varchar(15) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mobileNum` varchar(13) NOT NULL,
  `address` varchar(200) NOT NULL,
  `invoiceCount` int(11) NOT NULL,
  `productCount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `owncompany`
--

INSERT INTO `owncompany` (`id`, `companyName`, `name`, `GSTIN`, `email`, `mobileNum`, `address`, `invoiceCount`, `productCount`) VALUES
(1, 'Radhe Enterprose', 'jay chopda', '24ATJPC2927Q1ZE', 'jaychopda7064@gmail.com', '+917984178385', 'LS.NO 204, P1, THORDI, MAHUVA BHAVNAGAR HEY,\r\n Thordi Branch Post Office, BHUDEL, Thordi, Bhavnagar,\r\n Gujarat', 7, 2);

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `id` int(11) NOT NULL,
  `productName` varchar(100) NOT NULL,
  `productId` int(11) NOT NULL,
  `customerId` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `gst` int(11) NOT NULL,
  `totalAmount` int(11) NOT NULL,
  `date` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`id`, `productName`, `productId`, `customerId`, `quantity`, `unit`, `price`, `gst`, `totalAmount`, `date`) VALUES
(5, 'bentonite red ball', 1, 1, 30, 'tonne', 4500, 5, 135000, NULL),
(6, 'bentonite red ball', 1, 1, 10, 'tonne', 4500, 5, 45000, NULL),
(7, 'bentonite red ball', 1, 1, 25, 'tonne', 4500, 5, 112500, NULL),
(8, 'dolomite shining ball', 2, 2, 20, 'tonne', 9000, 5, 180000, NULL),
(9, 'bentonite red ball', 1, 2, 20, 'tonne', 4500, 5, 90000, NULL),
(10, 'dolomite shining ball', 2, 2, 10, 'tonne', 9000, 5, 90000, NULL),
(11, 'bentonite red ball', 1, 2, 20, 'tonne', 4500, 5, 90000, NULL),
(12, 'bentonite red ball', 1, 1, 20, 'tonne', 4500, 5, 90000, '14-02-2025'),
(13, 'dolomite shining ball', 2, 1, 10, 'tonne', 9000, 5, 90000, '14-02-2025');

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `id` int(11) NOT NULL,
  `productName` varchar(100) NOT NULL,
  `quantity` int(11) NOT NULL,
  `unit` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `totalAmount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`id`, `productName`, `quantity`, `unit`, `price`, `totalAmount`) VALUES
(1, 'bentonite red ball', 375, 'tonne', 4500, 1687500),
(2, 'dolomite shining ball', 190, 'tonne', 9000, 2340000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customerdetails`
--
ALTER TABLE `customerdetails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `owncompany`
--
ALTER TABLE `owncompany`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customerdetails`
--
ALTER TABLE `customerdetails`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `owncompany`
--
ALTER TABLE `owncompany`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `sales`
--
ALTER TABLE `sales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

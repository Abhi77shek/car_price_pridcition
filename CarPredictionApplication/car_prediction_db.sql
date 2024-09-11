-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 18, 2023 at 11:31 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car_prediction_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `carsaletable`
--

CREATE TABLE `carsaletable` (
  `srno` int(10) NOT NULL,
  `year` int(10) NOT NULL,
  `showroom_price` float(10,2) NOT NULL,
  `km_drived` bigint(20) NOT NULL,
  `previous_owner` varchar(20) NOT NULL,
  `fuel_type` varchar(100) NOT NULL,
  `seller_type` varchar(100) NOT NULL,
  `transmission` varchar(100) NOT NULL,
  `price` float(10,2) NOT NULL,
  `sold_on` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `carsaletable`
--

INSERT INTO `carsaletable` (`srno`, `year`, `showroom_price`, `km_drived`, `previous_owner`, `fuel_type`, `seller_type`, `transmission`, `price`, `sold_on`) VALUES
(10, 2000, 10.00, 78000, 'No', 'Petrol', 'Dealer', 'Manual', 0.30, '2023-08-09'),
(11, 2010, 10.00, 78000, 'No', 'Diesel', 'Individual', 'Automatic', 5.17, '2023-10-17'),
(12, 2015, 5.00, 10000, 'No', 'Petrol', 'Dealer', 'Manual', 4.07, '2023-01-18'),
(13, 2015, 6.00, 12000, 'Second Hand', 'CNG', 'Individual', 'Automatic', 4.83, '2023-04-14'),
(14, 2018, 7.00, 88000, 'Second Hand', 'CNG', 'Individual', 'Automatic', 3.27, '2023-05-20'),
(15, 2018, 10.00, 56000, 'Second Hand', 'Diesel', 'Dealer', 'Manual', 8.63, '2023-02-14'),
(16, 2020, 10.00, 56000, 'Second Hand', 'Diesel', 'Individual', 'Automatic', 8.99, '2023-03-19'),
(17, 2021, 5.00, 8900, 'Second Hand', 'Diesel', 'Dealer', 'Manual', 4.80, '2023-08-03'),
(18, 2022, 5.00, 89000, 'Second Hand', 'Petrol', 'Individual', 'Automatic', 3.70, '2023-10-21'),
(19, 2022, 2.00, 89000, 'Second Hand', 'Petrol', 'Individual', 'Automatic', 1.80, '2023-03-05'),
(20, 2021, 4.00, 79000, 'Second Hand', 'Petrol', 'Dealer', 'Manual', 3.03, '2023-11-14'),
(21, 2014, 8.25, 56000, 'No', 'Petrol', 'Dealer', 'Manual', 4.05, '2023-06-15'),
(22, 2014, 7.55, 88000, 'Second Hand', 'Diesel', 'Individual', 'Automatic', 5.13, '2023-11-15'),
(23, 2014, 6.00, 88000, 'Second Hand', 'Diesel', 'Individual', 'Automatic', 4.45, '2023-09-15'),
(24, 2014, 6.00, 10000, 'No', 'Petrol', 'Dealer', 'Manual', 5.45, '2023-11-15'),
(25, 2012, 6.00, 10000, 'No', 'Petrol', 'Dealer', 'Manual', 4.22, '2023-08-15'),
(26, 2011, 8.00, 10000, 'No', 'Petrol', 'Dealer', 'Automatic', 6.04, '2023-11-15'),
(27, 2011, 7.50, 65000, 'No', 'Petrol', 'Individual', 'Manual', 1.22, '2023-11-15'),
(28, 2015, 5.00, 15000, 'No', 'CNG', 'Individual', 'Automatic', 3.92, '2023-11-15'),
(29, 2010, 8.00, 56000, 'No', 'Petrol', 'Dealer', 'Manual', 2.88, '2023-11-16');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `carsaletable`
--
ALTER TABLE `carsaletable`
  ADD PRIMARY KEY (`srno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `carsaletable`
--
ALTER TABLE `carsaletable`
  MODIFY `srno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 12, 2021 at 03:34 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hms`
--

-- --------------------------------------------------------

--
-- Table structure for table `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Token', 6, 'add_token'),
(22, 'Can change Token', 6, 'change_token'),
(23, 'Can delete Token', 6, 'delete_token'),
(24, 'Can view Token', 6, 'view_token'),
(25, 'Can add token', 7, 'add_tokenproxy'),
(26, 'Can change token', 7, 'change_tokenproxy'),
(27, 'Can delete token', 7, 'delete_tokenproxy'),
(28, 'Can view token', 7, 'view_tokenproxy'),
(29, 'Can add auth model', 8, 'add_authmodel'),
(30, 'Can change auth model', 8, 'change_authmodel'),
(31, 'Can delete auth model', 8, 'delete_authmodel'),
(32, 'Can view auth model', 8, 'view_authmodel'),
(33, 'Can add Token', 9, 'add_authtokenmodel'),
(34, 'Can change Token', 9, 'change_authtokenmodel'),
(35, 'Can delete Token', 9, 'delete_authtokenmodel'),
(36, 'Can view Token', 9, 'view_authtokenmodel'),
(37, 'Can add permission model', 10, 'add_permissionmodel'),
(38, 'Can change permission model', 10, 'change_permissionmodel'),
(39, 'Can delete permission model', 10, 'delete_permissionmodel'),
(40, 'Can view permission model', 10, 'view_permissionmodel'),
(41, 'Can add staff model', 11, 'add_staffmodel'),
(42, 'Can change staff model', 11, 'change_staffmodel'),
(43, 'Can delete staff model', 11, 'delete_staffmodel'),
(44, 'Can view staff model', 11, 'view_staffmodel'),
(45, 'Can add staff permission model', 12, 'add_staffpermissionmodel'),
(46, 'Can change staff permission model', 12, 'change_staffpermissionmodel'),
(47, 'Can delete staff permission model', 12, 'delete_staffpermissionmodel'),
(48, 'Can view staff permission model', 12, 'view_staffpermissionmodel'),
(49, 'Can add reservation model', 13, 'add_reservationmodel'),
(50, 'Can change reservation model', 13, 'change_reservationmodel'),
(51, 'Can delete reservation model', 13, 'delete_reservationmodel'),
(52, 'Can view reservation model', 13, 'view_reservationmodel'),
(53, 'Can add room model', 14, 'add_roommodel'),
(54, 'Can change room model', 14, 'change_roommodel'),
(55, 'Can delete room model', 14, 'delete_roommodel'),
(56, 'Can view room model', 14, 'view_roommodel'),
(57, 'Can add booking record model', 15, 'add_bookingrecordmodel'),
(58, 'Can change booking record model', 15, 'change_bookingrecordmodel'),
(59, 'Can delete booking record model', 15, 'delete_bookingrecordmodel'),
(60, 'Can view booking record model', 15, 'view_bookingrecordmodel'),
(61, 'Can add drink model', 16, 'add_drinkmodel'),
(62, 'Can change drink model', 16, 'change_drinkmodel'),
(63, 'Can delete drink model', 16, 'delete_drinkmodel'),
(64, 'Can view drink model', 16, 'view_drinkmodel'),
(65, 'Can add drink order model', 17, 'add_drinkordermodel'),
(66, 'Can change drink order model', 17, 'change_drinkordermodel'),
(67, 'Can delete drink order model', 17, 'delete_drinkordermodel'),
(68, 'Can view drink order model', 17, 'view_drinkordermodel'),
(69, 'Can add food model', 18, 'add_foodmodel'),
(70, 'Can change food model', 18, 'change_foodmodel'),
(71, 'Can delete food model', 18, 'delete_foodmodel'),
(72, 'Can view food model', 18, 'view_foodmodel'),
(73, 'Can add food order model', 19, 'add_foodordermodel'),
(74, 'Can change food order model', 19, 'change_foodordermodel'),
(75, 'Can delete food order model', 19, 'delete_foodordermodel'),
(76, 'Can view food order model', 19, 'view_foodordermodel'),
(77, 'Can add payment model', 20, 'add_paymentmodel'),
(78, 'Can change payment model', 20, 'change_paymentmodel'),
(79, 'Can delete payment model', 20, 'delete_paymentmodel'),
(80, 'Can view payment model', 20, 'view_paymentmodel');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(6, 'authtoken', 'token'),
(7, 'authtoken', 'tokenproxy'),
(16, 'bar', 'drinkmodel'),
(17, 'bar', 'drinkordermodel'),
(4, 'contenttypes', 'contenttype'),
(8, 'hms_auth', 'authmodel'),
(9, 'hms_auth', 'authtokenmodel'),
(18, 'kitchen', 'foodmodel'),
(19, 'kitchen', 'foodordermodel'),
(20, 'reservation', 'paymentmodel'),
(13, 'reservation', 'reservationmodel'),
(15, 'room', 'bookingrecordmodel'),
(14, 'room', 'roommodel'),
(5, 'sessions', 'session'),
(10, 'staff', 'permissionmodel'),
(11, 'staff', 'staffmodel'),
(12, 'staff', 'staffpermissionmodel');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'hms_auth', '0001_initial', '2021-01-26 09:35:42.862584'),
(2, 'contenttypes', '0001_initial', '2021-01-26 09:35:45.776216'),
(3, 'admin', '0001_initial', '2021-01-26 09:35:46.482258'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-01-26 09:35:48.794777'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-01-26 09:35:48.862434'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-01-26 09:35:50.242540'),
(7, 'auth', '0001_initial', '2021-01-26 09:35:52.095390'),
(8, 'auth', '0002_alter_permission_name_max_length', '2021-01-26 09:35:58.165565'),
(9, 'auth', '0003_alter_user_email_max_length', '2021-01-26 09:35:58.282083'),
(10, 'auth', '0004_alter_user_username_opts', '2021-01-26 09:35:58.377796'),
(11, 'auth', '0005_alter_user_last_login_null', '2021-01-26 09:35:58.578466'),
(12, 'auth', '0006_require_contenttypes_0002', '2021-01-26 09:35:58.769277'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2021-01-26 09:35:58.870007'),
(14, 'auth', '0008_alter_user_username_max_length', '2021-01-26 09:35:58.977130'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2021-01-26 09:35:59.085146'),
(16, 'auth', '0010_alter_group_name_max_length', '2021-01-26 09:36:01.047362'),
(17, 'auth', '0011_update_proxy_permissions', '2021-01-26 09:36:01.112662'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2021-01-26 09:36:01.193797'),
(19, 'authtoken', '0001_initial', '2021-01-26 09:36:01.704128'),
(20, 'authtoken', '0002_auto_20160226_1747', '2021-01-26 09:36:03.783068'),
(21, 'authtoken', '0003_tokenproxy', '2021-01-26 09:36:03.857382'),
(22, 'sessions', '0001_initial', '2021-01-26 09:36:04.634649'),
(23, 'staff', '0001_initial', '2021-01-26 09:36:05.951534'),
(24, 'hms_auth', '0002_auto_20210206_1219', '2021-02-06 11:21:15.976681'),
(25, 'hms_auth', '0003_auto_20210206_1221', '2021-02-06 11:21:16.050122'),
(26, 'reservation', '0001_initial', '2021-02-06 11:21:17.745679'),
(27, 'hms_auth', '0004_auto_20210206_1534', '2021-02-06 14:34:38.932229'),
(28, 'reservation', '0002_reservationmodel_gender', '2021-02-06 14:34:41.939932'),
(29, 'hms_auth', '0005_auto_20210206_1613', '2021-02-06 15:14:04.247656'),
(30, 'reservation', '0003_auto_20210206_1613', '2021-02-06 15:14:04.332620'),
(31, 'hms_auth', '0006_auto_20210206_1622', '2021-02-06 15:22:40.885832'),
(32, 'reservation', '0004_auto_20210206_1622', '2021-02-06 15:22:41.545666'),
(33, 'hms_auth', '0007_auto_20210208_1432', '2021-02-08 13:32:20.224323'),
(34, 'room', '0001_initial', '2021-02-08 13:32:21.565656'),
(35, 'hms_auth', '0008_auto_20210209_1027', '2021-02-09 09:27:17.880840'),
(36, 'room', '0002_auto_20210209_1027', '2021-02-09 09:27:18.041925'),
(37, 'hms_auth', '0009_auto_20210209_1302', '2021-02-09 12:02:29.412323'),
(38, 'room', '0003_bookingrecordmodel_status', '2021-02-09 12:02:30.774337'),
(39, 'hms_auth', '0010_auto_20210209_1321', '2021-02-09 12:21:44.617844'),
(40, 'room', '0004_auto_20210209_1321', '2021-02-09 12:21:45.079016'),
(41, 'hms_auth', '0011_auto_20210209_1322', '2021-02-09 12:23:03.026581'),
(42, 'room', '0005_auto_20210209_1322', '2021-02-09 12:23:03.115093'),
(43, 'bar', '0001_initial', '2021-02-09 20:43:07.792260'),
(44, 'hms_auth', '0012_auto_20210209_2142', '2021-02-09 20:43:20.985172'),
(45, 'kitchen', '0001_initial', '2021-02-09 20:43:22.659119'),
(46, 'bar', '0002_drinkordermodel_completed_by', '2021-02-11 21:49:20.721498'),
(47, 'hms_auth', '0013_auto_20210211_2246', '2021-02-11 21:49:20.787872'),
(48, 'hms_auth', '0014_auto_20210211_2249', '2021-02-11 21:49:20.832604'),
(49, 'kitchen', '0002_foodordermodel_completed_by', '2021-02-11 21:49:22.355104'),
(50, 'bar', '0003_auto_20210211_2255', '2021-02-11 21:56:08.228068'),
(51, 'hms_auth', '0015_auto_20210211_2249', '2021-02-11 21:56:08.452741'),
(52, 'hms_auth', '0016_auto_20210211_2255', '2021-02-11 21:56:08.490464'),
(53, 'kitchen', '0003_auto_20210211_2255', '2021-02-11 21:56:10.795386'),
(54, 'hms_auth', '0017_auto_20210212_0031', '2021-02-11 23:32:05.747432'),
(55, 'reservation', '0005_paymentmodel', '2021-02-11 23:32:06.202384');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `hms_auth`
--

CREATE TABLE `hms_auth` (
  `id` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_auth`
--

INSERT INTO `hms_auth` (`id`, `email`, `password`, `is_staff`, `date_created`, `last_login`, `is_active`) VALUES
(1, 'opeyemiakosile@gmail.com', 'pbkdf2_sha256$216000$2dWIYNrp8sfC$S6d5NiNdpCOUVXPt4SefUbGge3Frh/boCoDPxMgtxYY=', 1, '2021-02-05 03:05:16.139000', '2021-02-05 03:05:16.139000', 1),
(3, 'sam@gmail.com', 'pbkdf2_sha256$216000$hZK1fA1bDINi$PolNEKMHApfQ+Ywy8Eiqj6U843NEJ3VSjL4NUf+0ArU=', 1, '2021-02-05 19:23:29.770345', '2021-02-05 19:23:29.770345', 1);

-- --------------------------------------------------------

--
-- Table structure for table `hms_auth_token`
--

CREATE TABLE `hms_auth_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_auth_token`
--

INSERT INTO `hms_auth_token` (`key`, `created`, `expires`, `user_id`) VALUES
('27db1f77461eb8d1fa1e1a32004cf183b0282677', '2021-02-11 21:12:26.240790', '2021-02-12 02:45:21.778685', 1);

-- --------------------------------------------------------

--
-- Table structure for table `hms_booking_record`
--

CREATE TABLE `hms_booking_record` (
  `timestamp` datetime(6) NOT NULL,
  `id` bigint(20) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `check_in` date NOT NULL,
  `check_out` date NOT NULL,
  `reservation_id` bigint(20) NOT NULL,
  `room_id` bigint(20) NOT NULL,
  `status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_booking_record`
--

INSERT INTO `hms_booking_record` (`timestamp`, `id`, `amount`, `quantity`, `check_in`, `check_out`, `reservation_id`, `room_id`, `status`) VALUES
('2021-02-09 12:33:01.063051', 1, '29000.00', 1, '2021-02-09', '2021-02-11', 2, 2, 'active');

-- --------------------------------------------------------

--
-- Table structure for table `hms_drink`
--

CREATE TABLE `hms_drink` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `price` decimal(20,2) NOT NULL,
  `metric` varchar(255) NOT NULL,
  `available` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_drink`
--

INSERT INTO `hms_drink` (`id`, `name`, `description`, `price`, `metric`, `available`) VALUES
(1, 'Mocha Edited', 'A Bottle of Mocha Drink', '6550.00', 'bottle', 6);

-- --------------------------------------------------------

--
-- Table structure for table `hms_drink_order`
--

CREATE TABLE `hms_drink_order` (
  `id` bigint(20) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `status` varchar(15) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `drink_id` bigint(20) NOT NULL,
  `registered_by_id` int(11) DEFAULT NULL,
  `reservation_id` bigint(20) NOT NULL,
  `completed_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_drink_order`
--

INSERT INTO `hms_drink_order` (`id`, `amount`, `quantity`, `status`, `timestamp`, `drink_id`, `registered_by_id`, `reservation_id`, `completed_by_id`) VALUES
(1, '32750.00', 5, 'completed', '2021-02-10 09:16:45.639015', 1, 1, 2, NULL),
(2, '32750.00', 5, 'completed', '2021-02-11 21:13:04.266443', 1, 1, 1, NULL),
(3, '45850.00', 7, 'canceled', '2021-02-11 22:35:57.653942', 1, 1, 2, 1),
(4, '32750.00', 5, 'canceled', '2021-02-11 22:48:26.839907', 1, 1, 1, 1),
(5, '6550.00', 1, 'pending', '2021-02-11 22:59:08.965789', 1, 1, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `hms_food`
--

CREATE TABLE `hms_food` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `price` decimal(20,2) NOT NULL,
  `metric` varchar(255) NOT NULL,
  `available` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_food`
--

INSERT INTO `hms_food` (`id`, `name`, `description`, `price`, `metric`, `available`) VALUES
(1, 'Fried Rice Edited', 'Fried rice and Chicken', '1500.00', 'plate', 42),
(2, 'Jollof Rice', 'Jollof rice and Chicken', '1200.00', 'plate', 44);

-- --------------------------------------------------------

--
-- Table structure for table `hms_food_order`
--

CREATE TABLE `hms_food_order` (
  `id` bigint(20) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `status` varchar(15) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `food_id` bigint(20) NOT NULL,
  `registered_by_id` int(11) DEFAULT NULL,
  `reservation_id` bigint(20) NOT NULL,
  `completed_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_food_order`
--

INSERT INTO `hms_food_order` (`id`, `amount`, `quantity`, `status`, `timestamp`, `food_id`, `registered_by_id`, `reservation_id`, `completed_by_id`) VALUES
(3, '3000.00', 2, 'completed', '2021-02-09 22:44:47.954503', 1, 1, 2, NULL),
(5, '16500.00', 11, 'canceled', '2021-02-11 21:30:30.430389', 1, 1, 1, NULL),
(6, '15000.00', 10, 'completed', '2021-02-11 22:43:16.336172', 1, 1, 2, 1),
(7, '12000.00', 10, 'completed', '2021-02-11 22:41:08.573791', 2, 1, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `hms_payment`
--

CREATE TABLE `hms_payment` (
  `id` bigint(20) NOT NULL,
  `channel` varchar(25) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `amount_paid` decimal(20,2) NOT NULL,
  `amount_unpaid` decimal(20,2) NOT NULL,
  `status` varchar(15) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `posted_by_id` int(11) DEFAULT NULL,
  `reservation_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_payment`
--

INSERT INTO `hms_payment` (`id`, `channel`, `amount`, `amount_paid`, `amount_unpaid`, `status`, `timestamp`, `posted_by_id`, `reservation_id`) VALUES
(5, 'transfer', '50000.00', '50000.00', '70050.00', 'completed', '2021-02-12 01:45:36.323480', 1, 1),
(6, 'pos', '70050.00', '120050.00', '0.00', 'completed', '2021-02-12 01:46:10.281226', 1, 1),
(7, 'direct', '58250.00', '58250.00', '33500.00', 'completed', '2021-02-12 01:46:27.496202', 1, 2),
(8, 'cash', '33500.00', '91750.00', '0.00', 'completed', '2021-02-12 01:47:01.385726', 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `hms_permission`
--

CREATE TABLE `hms_permission` (
  `id` int(11) NOT NULL,
  `display_name` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `category` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_permission`
--

INSERT INTO `hms_permission` (`id`, `display_name`, `name`, `category`) VALUES
(1, 'Add Staff', 'can_add_staff', 'admin'),
(2, 'View Staffs', 'can_view_staff', 'admin'),
(3, 'Edit Staff', 'can_edit_staff', 'admin'),
(4, 'Make Reservation', 'can_make_reservation', 'basic'),
(5, 'View EOD', 'can_view_eod', 'management'),
(6, 'Edit Staff Permission', 'can_edit_staff_permission', 'admin'),
(7, 'View Reservation', 'can_view_reservation', 'basic'),
(8, 'Add Room', 'can_add_room', 'admin'),
(9, 'Edit Room', 'can_edit_room', 'admin'),
(10, 'Delete Room', 'can_delete_room', 'admin'),
(11, 'View Room', 'can_view_room', 'basic'),
(12, 'Book Room', 'can_book_room', 'basic'),
(13, 'View Room Booking', 'can_view_booking', 'basic'),
(14, 'Add Food', 'can_add_food', 'management'),
(15, 'Edit Food', 'can_edit_food', 'management'),
(16, 'View Food', 'can_view_food', 'management'),
(17, 'Place Food Order', 'can_place_food_order', 'management'),
(18, 'View Food Order', 'can_view_food_order', 'management'),
(19, 'Add Drink', 'can_add_drink', 'management'),
(20, 'View Drink', 'can_view_drink', 'management'),
(21, 'Edit Drink', 'can_edit_drink', 'management'),
(22, 'Place Drink Order', 'can_place_drink_order', 'management'),
(23, 'View Drink Order', 'can_view_drink_order', 'management'),
(24, 'Make Payment', 'can_make_payment', 'basic'),
(25, 'Reverse Payment', 'can_reverse_payment', 'management'),
(26, 'View Payment History', 'can_view_payment_history', 'basic'),
(27, 'Print Invoice', 'can_print_invoice', 'basic');

-- --------------------------------------------------------

--
-- Table structure for table `hms_reservation`
--

CREATE TABLE `hms_reservation` (
  `id` bigint(20) NOT NULL,
  `reference` varchar(12) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `status` varchar(15) NOT NULL,
  `credit_balance` decimal(20,2) NOT NULL,
  `amount_spent` decimal(20,2) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `gender` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_reservation`
--

INSERT INTO `hms_reservation` (`id`, `reference`, `first_name`, `last_name`, `phone_number`, `status`, `credit_balance`, `amount_spent`, `timestamp`, `created_by_id`, `gender`) VALUES
(1, 'J4SVT8NU0BCT', 'Opeyemi', 'Akosile', '08065546736', 'checked_out', '29950.00', '120050.00', '2021-02-12 01:46:10.346756', 1, 'male'),
(2, 'KSRELQR4HJ2Y', 'Jerome', 'Coleman', '09065551148', 'checked_out', '16500.00', '91750.00', '2021-02-12 01:47:01.385726', 1, 'male');

-- --------------------------------------------------------

--
-- Table structure for table `hms_room`
--

CREATE TABLE `hms_room` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `price` decimal(20,2) NOT NULL,
  `start_no` int(11) NOT NULL,
  `end_no` int(11) NOT NULL,
  `available` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_room`
--

INSERT INTO `hms_room` (`id`, `name`, `description`, `price`, `start_no`, `end_no`, `available`) VALUES
(1, 'Deluxe Room', 'Just another Deluxe Room', '24500.00', 100, 109, 10),
(2, 'Standard Room', 'Just another Standard Room', '14500.00', 200, 209, 9);

-- --------------------------------------------------------

--
-- Table structure for table `hms_staff`
--

CREATE TABLE `hms_staff` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `position` varchar(50) NOT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `auth_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_staff`
--

INSERT INTO `hms_staff` (`id`, `first_name`, `last_name`, `gender`, `phone_number`, `position`, `avatar`, `auth_id`) VALUES
(1, 'Opeyemi', 'Akosile', 'male', '08076567677', 'Administrator', '', 1),
(2, 'Samuel', 'Opeyemi', 'male', '0907383783', 'Account Officer', '', 3);

-- --------------------------------------------------------

--
-- Table structure for table `hms_staff_permission`
--

CREATE TABLE `hms_staff_permission` (
  `id` int(11) NOT NULL,
  `date_asigned` datetime(6) NOT NULL,
  `permission_id` int(11) NOT NULL,
  `staff_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_staff_permission`
--

INSERT INTO `hms_staff_permission` (`id`, `date_asigned`, `permission_id`, `staff_id`) VALUES
(1, '2021-02-05 18:23:39.056509', 1, 1),
(2, '2021-02-05 18:23:39.165007', 2, 1),
(3, '2021-02-05 18:23:39.225349', 3, 1),
(4, '2021-02-05 18:23:39.428985', 6, 1),
(5, '2021-02-06 14:53:10.605922', 4, 1),
(6, '2021-02-06 14:53:10.677777', 7, 1),
(7, '2021-02-08 15:46:21.585217', 8, 1),
(8, '2021-02-08 15:46:21.625593', 9, 1),
(9, '2021-02-08 15:46:21.702867', 10, 1),
(10, '2021-02-09 09:08:32.068313', 11, 1),
(11, '2021-02-09 12:19:32.529266', 12, 1),
(12, '2021-02-09 15:14:27.230574', 13, 1),
(13, '2021-02-09 21:16:26.804764', 14, 1),
(14, '2021-02-09 21:16:26.857777', 15, 1),
(15, '2021-02-09 21:16:26.889020', 16, 1),
(16, '2021-02-09 22:37:07.053218', 17, 1),
(17, '2021-02-09 22:37:07.113142', 18, 1),
(18, '2021-02-10 08:12:12.427568', 19, 1),
(19, '2021-02-10 08:12:12.502368', 20, 1),
(20, '2021-02-10 08:12:12.660020', 21, 1),
(21, '2021-02-10 08:12:12.756563', 22, 1),
(22, '2021-02-10 08:12:12.812119', 23, 1),
(23, '2021-02-12 01:15:55.675024', 25, 1),
(24, '2021-02-12 01:15:55.775324', 24, 1),
(25, '2021-02-12 01:15:55.813083', 26, 1),
(26, '2021-02-12 01:15:55.875585', 27, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_hms_auth_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `hms_auth`
--
ALTER TABLE `hms_auth`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `hms_auth_token`
--
ALTER TABLE `hms_auth_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `hms_booking_record`
--
ALTER TABLE `hms_booking_record`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hms_booking_record_reservation_id_50bc3b67_fk_hms_reservation_id` (`reservation_id`),
  ADD KEY `hms_booking_record_room_id_1f99642b_fk_hms_room_id` (`room_id`);

--
-- Indexes for table `hms_drink`
--
ALTER TABLE `hms_drink`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `hms_drink_order`
--
ALTER TABLE `hms_drink_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hms_drink_order_drink_id_a75367a7_fk_hms_drink_id` (`drink_id`),
  ADD KEY `hms_drink_order_reservation_id_641704bb_fk_hms_reservation_id` (`reservation_id`),
  ADD KEY `hms_drink_order_completed_by_id_034048ab_fk_hms_staff_id` (`completed_by_id`),
  ADD KEY `hms_drink_order_registered_by_id_925d406a_fk_hms_staff_id` (`registered_by_id`);

--
-- Indexes for table `hms_food`
--
ALTER TABLE `hms_food`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `hms_food_order`
--
ALTER TABLE `hms_food_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hms_food_order_food_id_f4f33934_fk_hms_food_id` (`food_id`),
  ADD KEY `hms_food_order_reservation_id_1abcddc8_fk_hms_reservation_id` (`reservation_id`),
  ADD KEY `hms_food_order_completed_by_id_a1b6dadc_fk_hms_staff_id` (`completed_by_id`),
  ADD KEY `hms_food_order_registered_by_id_7ec240c7_fk_hms_staff_id` (`registered_by_id`);

--
-- Indexes for table `hms_payment`
--
ALTER TABLE `hms_payment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hms_payment_posted_by_id_e2e4187c_fk_hms_staff_id` (`posted_by_id`),
  ADD KEY `hms_payment_reservation_id_e1e1642e_fk_hms_reservation_id` (`reservation_id`);

--
-- Indexes for table `hms_permission`
--
ALTER TABLE `hms_permission`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hms_reservation`
--
ALTER TABLE `hms_reservation`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `hms_reservation_reference_40a5d0eb_uniq` (`reference`),
  ADD KEY `hms_reservation_created_by_id_9aec3e14_fk_hms_staff_id` (`created_by_id`);

--
-- Indexes for table `hms_room`
--
ALTER TABLE `hms_room`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `hms_staff`
--
ALTER TABLE `hms_staff`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_id` (`auth_id`);

--
-- Indexes for table `hms_staff_permission`
--
ALTER TABLE `hms_staff_permission`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hms_staff_permission_permission_id_1a868e51_fk_hms_permission_id` (`permission_id`),
  ADD KEY `hms_staff_permission_staff_id_8ee23e72_fk_hms_staff_id` (`staff_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `hms_auth`
--
ALTER TABLE `hms_auth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `hms_booking_record`
--
ALTER TABLE `hms_booking_record`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `hms_drink`
--
ALTER TABLE `hms_drink`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `hms_drink_order`
--
ALTER TABLE `hms_drink_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `hms_food`
--
ALTER TABLE `hms_food`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hms_food_order`
--
ALTER TABLE `hms_food_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `hms_payment`
--
ALTER TABLE `hms_payment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `hms_permission`
--
ALTER TABLE `hms_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `hms_reservation`
--
ALTER TABLE `hms_reservation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hms_room`
--
ALTER TABLE `hms_room`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hms_staff`
--
ALTER TABLE `hms_staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hms_staff_permission`
--
ALTER TABLE `hms_staff_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_hms_auth_id` FOREIGN KEY (`user_id`) REFERENCES `hms_auth` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_hms_auth_id` FOREIGN KEY (`user_id`) REFERENCES `hms_auth` (`id`);

--
-- Constraints for table `hms_auth_token`
--
ALTER TABLE `hms_auth_token`
  ADD CONSTRAINT `hms_auth_token_user_id_e05f02f2_fk_hms_auth_id` FOREIGN KEY (`user_id`) REFERENCES `hms_auth` (`id`);

--
-- Constraints for table `hms_booking_record`
--
ALTER TABLE `hms_booking_record`
  ADD CONSTRAINT `hms_booking_record_reservation_id_50bc3b67_fk_hms_reservation_id` FOREIGN KEY (`reservation_id`) REFERENCES `hms_reservation` (`id`),
  ADD CONSTRAINT `hms_booking_record_room_id_1f99642b_fk_hms_room_id` FOREIGN KEY (`room_id`) REFERENCES `hms_room` (`id`);

--
-- Constraints for table `hms_drink_order`
--
ALTER TABLE `hms_drink_order`
  ADD CONSTRAINT `hms_drink_order_completed_by_id_034048ab_fk_hms_staff_id` FOREIGN KEY (`completed_by_id`) REFERENCES `hms_staff` (`id`),
  ADD CONSTRAINT `hms_drink_order_drink_id_a75367a7_fk_hms_drink_id` FOREIGN KEY (`drink_id`) REFERENCES `hms_drink` (`id`),
  ADD CONSTRAINT `hms_drink_order_registered_by_id_925d406a_fk_hms_staff_id` FOREIGN KEY (`registered_by_id`) REFERENCES `hms_staff` (`id`),
  ADD CONSTRAINT `hms_drink_order_reservation_id_641704bb_fk_hms_reservation_id` FOREIGN KEY (`reservation_id`) REFERENCES `hms_reservation` (`id`);

--
-- Constraints for table `hms_food_order`
--
ALTER TABLE `hms_food_order`
  ADD CONSTRAINT `hms_food_order_completed_by_id_a1b6dadc_fk_hms_staff_id` FOREIGN KEY (`completed_by_id`) REFERENCES `hms_staff` (`id`),
  ADD CONSTRAINT `hms_food_order_food_id_f4f33934_fk_hms_food_id` FOREIGN KEY (`food_id`) REFERENCES `hms_food` (`id`),
  ADD CONSTRAINT `hms_food_order_registered_by_id_7ec240c7_fk_hms_staff_id` FOREIGN KEY (`registered_by_id`) REFERENCES `hms_staff` (`id`),
  ADD CONSTRAINT `hms_food_order_reservation_id_1abcddc8_fk_hms_reservation_id` FOREIGN KEY (`reservation_id`) REFERENCES `hms_reservation` (`id`);

--
-- Constraints for table `hms_payment`
--
ALTER TABLE `hms_payment`
  ADD CONSTRAINT `hms_payment_posted_by_id_e2e4187c_fk_hms_staff_id` FOREIGN KEY (`posted_by_id`) REFERENCES `hms_staff` (`id`),
  ADD CONSTRAINT `hms_payment_reservation_id_e1e1642e_fk_hms_reservation_id` FOREIGN KEY (`reservation_id`) REFERENCES `hms_reservation` (`id`);

--
-- Constraints for table `hms_reservation`
--
ALTER TABLE `hms_reservation`
  ADD CONSTRAINT `hms_reservation_created_by_id_9aec3e14_fk_hms_staff_id` FOREIGN KEY (`created_by_id`) REFERENCES `hms_staff` (`id`);

--
-- Constraints for table `hms_staff`
--
ALTER TABLE `hms_staff`
  ADD CONSTRAINT `hms_staff_auth_id_5ed90aac_fk_hms_auth_id` FOREIGN KEY (`auth_id`) REFERENCES `hms_auth` (`id`);

--
-- Constraints for table `hms_staff_permission`
--
ALTER TABLE `hms_staff_permission`
  ADD CONSTRAINT `hms_staff_permission_permission_id_1a868e51_fk_hms_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `hms_permission` (`id`),
  ADD CONSTRAINT `hms_staff_permission_staff_id_8ee23e72_fk_hms_staff_id` FOREIGN KEY (`staff_id`) REFERENCES `hms_staff` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 24, 2021 at 04:07 PM
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
(80, 'Can view payment model', 20, 'view_paymentmodel'),
(81, 'Can add order model', 21, 'add_ordermodel'),
(82, 'Can change order model', 21, 'change_ordermodel'),
(83, 'Can delete order model', 21, 'delete_ordermodel'),
(84, 'Can view order model', 21, 'view_ordermodel'),
(85, 'Can add coupon model', 22, 'add_couponmodel'),
(86, 'Can change coupon model', 22, 'change_couponmodel'),
(87, 'Can delete coupon model', 22, 'delete_couponmodel'),
(88, 'Can view coupon model', 22, 'view_couponmodel'),
(89, 'Can add supply model', 23, 'add_supplymodel'),
(90, 'Can change supply model', 23, 'change_supplymodel'),
(91, 'Can delete supply model', 23, 'delete_supplymodel'),
(92, 'Can view supply model', 23, 'view_supplymodel'),
(93, 'Can add vendor model', 24, 'add_vendormodel'),
(94, 'Can change vendor model', 24, 'change_vendormodel'),
(95, 'Can delete vendor model', 24, 'delete_vendormodel'),
(96, 'Can view vendor model', 24, 'view_vendormodel'),
(97, 'Can add vendor payment model', 25, 'add_vendorpaymentmodel'),
(98, 'Can change vendor payment model', 25, 'change_vendorpaymentmodel'),
(99, 'Can delete vendor payment model', 25, 'delete_vendorpaymentmodel'),
(100, 'Can view vendor payment model', 25, 'view_vendorpaymentmodel'),
(101, 'Can add option model', 26, 'add_optionmodel'),
(102, 'Can change option model', 26, 'change_optionmodel'),
(103, 'Can delete option model', 26, 'delete_optionmodel'),
(104, 'Can view option model', 26, 'view_optionmodel');

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
(22, 'coupon', 'couponmodel'),
(8, 'hms_auth', 'authmodel'),
(9, 'hms_auth', 'authtokenmodel'),
(18, 'kitchen', 'foodmodel'),
(19, 'kitchen', 'foodordermodel'),
(26, 'options', 'optionmodel'),
(21, 'reservation', 'ordermodel'),
(20, 'reservation', 'paymentmodel'),
(13, 'reservation', 'reservationmodel'),
(15, 'room', 'bookingrecordmodel'),
(14, 'room', 'roommodel'),
(5, 'sessions', 'session'),
(10, 'staff', 'permissionmodel'),
(11, 'staff', 'staffmodel'),
(12, 'staff', 'staffpermissionmodel'),
(23, 'vendor', 'supplymodel'),
(24, 'vendor', 'vendormodel'),
(25, 'vendor', 'vendorpaymentmodel');

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
(55, 'reservation', '0005_paymentmodel', '2021-02-11 23:32:06.202384'),
(56, 'reservation', '0006_auto_20210216_0814', '2021-02-16 07:14:49.205517'),
(57, 'bar', '0004_drinkordermodel_payment', '2021-02-16 07:14:51.790490'),
(58, 'hms_auth', '0018_auto_20210216_0814', '2021-02-16 07:14:51.898595'),
(59, 'kitchen', '0004_foodordermodel_payment', '2021-02-16 07:14:54.072635'),
(60, 'room', '0006_bookingrecordmodel_booked_by', '2021-02-16 07:14:56.170040'),
(61, 'hms_auth', '0019_auto_20210216_1212', '2021-02-16 11:12:14.470713'),
(62, 'reservation', '0007_auto_20210216_1212', '2021-02-16 11:12:17.957525'),
(63, 'room', '0007_bookingrecordmodel_payment', '2021-02-16 11:12:23.140837'),
(64, 'reservation', '0008_auto_20210218_1335', '2021-02-18 12:35:49.055622'),
(65, 'bar', '0005_drinkordermodel_order', '2021-02-18 12:35:53.320161'),
(66, 'hms_auth', '0020_auto_20210218_1335', '2021-02-18 12:35:53.809685'),
(67, 'kitchen', '0005_foodordermodel_order', '2021-02-18 12:36:02.161021'),
(68, 'hms_auth', '0021_auto_20210218_1420', '2021-02-18 13:23:39.905907'),
(69, 'hms_auth', '0022_auto_20210218_1421', '2021-02-18 13:23:40.026317'),
(70, 'reservation', '0009_ordermodel_order_ref', '2021-02-18 13:23:41.500848'),
(71, 'coupon', '0001_initial', '2021-02-19 09:35:41.329740'),
(72, 'hms_auth', '0023_auto_20210219_1035', '2021-02-19 09:35:43.599503'),
(73, 'coupon', '0002_auto_20210219_1101', '2021-02-19 10:01:25.250134'),
(74, 'hms_auth', '0024_auto_20210219_1101', '2021-02-19 10:01:25.410909'),
(75, 'coupon', '0003_couponmodel_status', '2021-02-19 10:36:53.232633'),
(76, 'hms_auth', '0025_auto_20210219_1136', '2021-02-19 10:36:53.431076'),
(77, 'hms_auth', '0026_auto_20210219_1949', '2021-02-19 18:49:39.881889'),
(78, 'vendor', '0001_initial', '2021-02-19 18:49:44.726263'),
(79, 'hms_auth', '0027_auto_20210219_2007', '2021-02-19 19:07:17.875169'),
(80, 'vendor', '0002_auto_20210219_2007', '2021-02-19 19:07:20.240468'),
(88, 'options', '0001_initial', '2021-02-20 12:53:20.344349'),
(89, 'options', '0002_auto_20210220_1307', '2021-02-20 12:53:21.365932'),
(90, 'bar', '0006_drinkmodel_group', '2021-02-20 12:53:27.137738'),
(91, 'hms_auth', '0028_auto_20210220_0756', '2021-02-20 12:53:27.238982'),
(92, 'hms_auth', '0029_auto_20210220_1307', '2021-02-20 12:53:27.336897'),
(93, 'hms_auth', '0030_auto_20210220_1339', '2021-02-20 12:53:27.473107'),
(94, 'hms_auth', '0031_auto_20210220_1342', '2021-02-20 12:53:27.755087'),
(95, 'hms_auth', '0032_auto_20210220_1343', '2021-02-20 12:53:28.135388'),
(96, 'hms_auth', '0033_auto_20210220_1345', '2021-02-20 12:53:28.346757'),
(97, 'hms_auth', '0034_auto_20210220_1346', '2021-02-20 12:53:28.496915'),
(98, 'hms_auth', '0035_auto_20210220_1352', '2021-02-20 12:53:28.654585'),
(99, 'kitchen', '0006_foodmodel_group', '2021-02-20 12:53:31.449262'),
(100, 'hms_auth', '0036_auto_20210224_1205', '2021-02-24 11:05:09.072018'),
(101, 'reservation', '0010_reservationmodel_override_by', '2021-02-24 11:05:11.162320');

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
(1, 'opeyemiakosile@gmail.com', 'pbkdf2_sha256$216000$o1XJStCJm3Qj$dEKnwG8V4b2d7N1qGBGNECw9DJUe7rtllXUvAtAAVgk=', 1, '2021-02-05 03:05:16.139000', '2021-02-14 08:45:28.615932', 1),
(3, 'sam@gmail.com', 'pbkdf2_sha256$216000$jQDpxiGYKVcB$3/pVrNlpxDJJTAnd2fSqGMtNDf56V5hoLpYITSlrACQ=', 1, '2021-02-05 19:23:29.770345', '2021-02-19 21:34:00.908879', 1),
(4, 'samloco@gmail.com', 'pbkdf2_sha256$216000$SQnl4gsi21VC$8dTQGsN6Ng+fHgnQv+QbfE4ZBCg8S0TSHwi+FHEXaWk=', 1, '2021-02-12 13:02:19.297572', '2021-02-12 13:02:19.297572', 1),
(5, 'opeyemi@gmail.com', 'pbkdf2_sha256$216000$05Sc5TT3D0we$jyCYKVjxVbEcjQWyzkELIV+1CRrfea/W8uYqqJqeGEU=', 1, '2021-02-15 06:41:12.848483', '2021-02-15 06:41:12.848483', 1),
(6, 'rotman@gmail.com', 'pbkdf2_sha256$216000$lA9cne3edKUQ$Z2gmGB/wBLMxic8ed5QeAzRm1MIMwAxkMo4oP3yQ7hw=', 1, '2021-02-15 07:30:24.956751', '2021-02-15 07:30:24.956751', 1);

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
('13f24b3e2f5f1b01b952a0b7f4290afadacb707b', '2021-02-24 11:11:27.512693', '2021-02-24 15:22:10.419847', 1),
('77c5bb6eba3842991ebbc256a88d28255c78dfaf', '2021-02-12 13:08:28.669213', '2021-02-12 13:23:31.188880', 4),
('a5aa9ed8726c63c61dcc23e685b8819a00d7b618', '2021-02-19 07:10:31.606407', '2021-02-19 07:25:59.879893', 3);

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
  `status` varchar(15) NOT NULL,
  `booked_by_id` int(11) DEFAULT NULL,
  `payment_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_booking_record`
--

INSERT INTO `hms_booking_record` (`timestamp`, `id`, `amount`, `quantity`, `check_in`, `check_out`, `reservation_id`, `room_id`, `status`, `booked_by_id`, `payment_id`) VALUES
('2021-02-09 12:33:01.063051', 1, '29000.00', 1, '2021-02-09', '2021-02-11', 2, 2, 'active', NULL, NULL),
('2021-02-16 03:23:30.213415', 2, '24500.00', 1, '2021-02-16', '2021-02-17', 8, 1, 'active', NULL, NULL),
('2021-02-16 09:50:36.854514', 3, '60000.00', 2, '2021-02-16', '2021-02-21', 10, 3, 'active', NULL, NULL),
('2021-02-18 23:03:38.107273', 4, '58000.00', 1, '2021-02-18', '2021-02-22', 13, 2, 'canceled', 1, 15),
('2021-02-18 23:02:10.469563', 5, '58000.00', 1, '2021-02-18', '2021-02-22', 14, 2, 'checked_out', 1, 16),
('2021-02-18 22:59:22.139653', 6, '58000.00', 1, '2021-02-18', '2021-02-22', 15, 2, 'canceled', 1, 17),
('2021-02-18 22:59:00.825177', 7, '58000.00', 1, '2021-02-18', '2021-02-22', 16, 2, 'checked_out', 1, 18),
('2021-02-18 23:56:23.629004', 8, '24500.00', 1, '2021-02-19', '2021-02-20', 17, 1, 'canceled', 1, 27),
('2021-02-19 22:07:57.203273', 9, '24500.00', 1, '2021-02-19', '2021-02-20', 20, 1, 'checked_in', 1, 32);

-- --------------------------------------------------------

--
-- Table structure for table `hms_coupon`
--

CREATE TABLE `hms_coupon` (
  `id` bigint(20) NOT NULL,
  `code` varchar(14) NOT NULL,
  `discount` decimal(5,2) NOT NULL,
  `reservation_id` bigint(20) DEFAULT NULL,
  `date_created` datetime(6) NOT NULL,
  `date_used` datetime(6) DEFAULT NULL,
  `status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_coupon`
--

INSERT INTO `hms_coupon` (`id`, `code`, `discount`, `reservation_id`, `date_created`, `date_used`, `status`) VALUES
(3, 'B0DG9MACG1SVEN', '12.00', 20, '2021-02-19 11:05:26.768575', '2021-02-19 13:41:14.088617', 'used'),
(4, '66KYKWD9NZI0ZN', '9.00', 14, '2021-02-19 14:23:57.194118', '2021-02-19 22:03:13.172101', 'used');

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
  `available` int(11) NOT NULL,
  `group_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_drink`
--

INSERT INTO `hms_drink` (`id`, `name`, `description`, `price`, `metric`, `available`, `group_id`) VALUES
(1, 'Mocha Edited', 'A Bottle of Mocha Drink', '6550.00', 'bottle', 0, NULL),
(2, 'Just a Wine ', 'Just a Wine ', '16500.00', 'bottle', 45, 6);

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
  `completed_by_id` int(11) DEFAULT NULL,
  `payment_id` bigint(20) DEFAULT NULL,
  `order_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_drink_order`
--

INSERT INTO `hms_drink_order` (`id`, `amount`, `quantity`, `status`, `timestamp`, `drink_id`, `registered_by_id`, `reservation_id`, `completed_by_id`, `payment_id`, `order_id`) VALUES
(1, '32750.00', 5, 'completed', '2021-02-10 09:16:45.639015', 1, 1, 2, NULL, NULL, NULL),
(2, '32750.00', 5, 'completed', '2021-02-11 21:13:04.266443', 1, 1, 1, NULL, NULL, NULL),
(3, '45850.00', 7, 'canceled', '2021-02-11 22:35:57.653942', 1, 1, 2, 1, NULL, NULL),
(4, '32750.00', 5, 'canceled', '2021-02-11 22:48:26.839907', 1, 1, 1, 1, NULL, NULL),
(5, '6550.00', 1, 'pending', '2021-02-11 22:59:08.965789', 1, 1, 1, NULL, NULL, NULL),
(6, '13100.00', 2, 'canceled', '2021-02-17 09:56:34.714398', 1, 1, 3, 1, NULL, NULL),
(7, '13100.00', 2, 'pending', '2021-02-18 13:59:08.002556', 1, 1, 13, NULL, 22, 1),
(9, '6550.00', 1, 'pending', '2021-02-18 15:34:16.029672', 1, 1, 14, NULL, 24, 3),
(10, '6550.00', 1, 'pending', '2021-02-18 15:37:17.846658', 1, 1, 15, NULL, 25, 4),
(11, '6550.00', 1, 'pending', '2021-02-18 16:00:32.825125', 1, 1, 15, NULL, 26, 5),
(12, '6550.00', 1, 'pending', '2021-02-19 00:24:12.669394', 1, 1, 14, NULL, 30, 6),
(13, '82500.00', 5, 'pending', '2021-02-20 17:26:35.761086', 2, 1, 14, NULL, 37, 8),
(14, '16500.00', 1, 'pending', '2021-02-20 17:46:01.964163', 2, 1, 14, NULL, 38, 9),
(15, '16500.00', 1, 'pending', '2021-02-20 18:11:45.583048', 2, 1, 14, NULL, 39, 10),
(16, '16500.00', 1, 'completed', '2021-02-20 18:22:24.890960', 2, 1, 14, 1, 40, 11),
(17, '16500.00', 1, 'completed', '2021-02-20 18:21:56.715736', 2, 1, 14, 1, NULL, 15),
(18, '16500.00', 1, 'completed', '2021-02-20 18:21:46.108025', 2, 1, 14, 1, NULL, 16),
(19, '16500.00', 1, 'pending', '2021-02-23 11:31:03.730151', 2, 1, 14, NULL, 46, 19);

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
  `available` int(11) NOT NULL,
  `group_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_food`
--

INSERT INTO `hms_food` (`id`, `name`, `description`, `price`, `metric`, `available`, `group_id`) VALUES
(1, 'Fried Rice Edited', 'Fried rice and Chicken', '1500.00', 'plate', 17, 2),
(2, 'Jollof Rice', 'Jollof rice and Chicken', '1200.00', 'plate', 29, NULL),
(3, 'Just A Rice', 'Just A Rice', '2000.00', 'plate', 1500, 2);

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
  `completed_by_id` int(11) DEFAULT NULL,
  `payment_id` bigint(20) DEFAULT NULL,
  `order_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_food_order`
--

INSERT INTO `hms_food_order` (`id`, `amount`, `quantity`, `status`, `timestamp`, `food_id`, `registered_by_id`, `reservation_id`, `completed_by_id`, `payment_id`, `order_id`) VALUES
(3, '3000.00', 2, 'completed', '2021-02-09 22:44:47.954503', 1, 1, 2, NULL, NULL, NULL),
(5, '16500.00', 11, 'canceled', '2021-02-11 21:30:30.430389', 1, 1, 1, NULL, NULL, NULL),
(6, '15000.00', 10, 'completed', '2021-02-11 22:43:16.336172', 1, 1, 2, 1, NULL, NULL),
(7, '12000.00', 10, 'completed', '2021-02-11 22:41:08.573791', 2, 1, 2, 1, NULL, NULL),
(8, '6000.00', 4, 'completed', '2021-02-17 09:05:39.096733', 1, 1, 2, 1, 9, NULL),
(9, '14400.00', 12, 'pending', '2021-02-17 08:56:12.105045', 2, 1, 2, NULL, 9, NULL),
(10, '3000.00', 2, 'pending', '2021-02-17 09:09:44.512325', 1, 1, 3, NULL, NULL, NULL),
(11, '7500.00', 5, 'canceled', '2021-02-17 10:54:40.898838', 1, 1, 2, 1, 10, NULL),
(12, '3000.00', 2, 'pending', '2021-02-18 13:59:07.961860', 1, 1, 13, NULL, 22, 1),
(14, '3000.00', 2, 'pending', '2021-02-18 15:34:15.779016', 1, 1, 14, NULL, 24, 3),
(15, '1500.00', 1, 'pending', '2021-02-18 15:37:18.100944', 1, 1, 15, NULL, 25, 4),
(16, '3000.00', 2, 'pending', '2021-02-18 16:00:32.806184', 1, 1, 15, NULL, 26, 5),
(17, '3000.00', 2, 'pending', '2021-02-19 00:24:12.253811', 1, 1, 14, NULL, 30, 6),
(18, '4500.00', 3, 'pending', '2021-02-19 22:28:25.479163', 1, 1, 14, NULL, 36, 7),
(19, '3600.00', 3, 'pending', '2021-02-19 22:28:26.121011', 2, 1, 14, NULL, 36, 7),
(20, '3000.00', 2, 'pending', '2021-02-20 18:14:50.888596', 1, 1, 14, NULL, 41, 12),
(21, '1500.00', 1, 'pending', '2021-02-20 18:17:56.996967', 1, 1, 14, NULL, 42, 13),
(22, '2000.00', 1, 'canceled', '2021-02-20 18:25:48.040983', 3, 1, 14, 1, 43, 14),
(23, '1500.00', 1, 'completed', '2021-02-20 18:23:02.869922', 1, 1, 14, 1, NULL, 16),
(24, '1500.00', 1, 'completed', '2021-02-24 15:01:28.542958', 1, 1, 14, 1, 44, 17),
(25, '1500.00', 1, 'completed', '2021-02-23 11:29:48.526652', 1, 1, 14, 1, 45, 18),
(26, '1500.00', 1, 'completed', '2021-02-24 12:16:57.696768', 1, 1, 15, 1, 47, 20);

-- --------------------------------------------------------

--
-- Table structure for table `hms_options`
--

CREATE TABLE `hms_options` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `value` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_options`
--

INSERT INTO `hms_options` (`id`, `name`, `value`) VALUES
(1, 'food', 'Tuber'),
(2, 'food', 'Rice'),
(3, 'food', 'DAvid'),
(4, 'drink', 'Beer'),
(5, 'drink', 'Wine'),
(6, 'drink', 'Beverages'),
(7, 'drink', 'Citrus');

-- --------------------------------------------------------

--
-- Table structure for table `hms_order`
--

CREATE TABLE `hms_order` (
  `id` bigint(20) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `order_ref` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_order`
--

INSERT INTO `hms_order` (`id`, `amount`, `timestamp`, `order_ref`) VALUES
(1, '16100.00', '2021-02-18 13:59:07.959866', 'XC1024'),
(3, '9550.00', '2021-02-18 15:34:15.771039', '9H1025'),
(4, '8050.00', '2021-02-18 15:37:17.837682', 'FT1026'),
(5, '9550.00', '2021-02-18 16:00:32.749287', 'E81027'),
(6, '9550.00', '2021-02-19 00:24:12.179924', 'TX1028'),
(7, '-900.00', '2021-02-19 22:28:25.398379', '3C1029'),
(8, '82500.00', '2021-02-20 17:26:35.577342', 'WA1030'),
(9, '16500.00', '2021-02-20 17:46:01.840338', '3I1031'),
(10, '16500.00', '2021-02-20 18:11:45.477057', 'XT1032'),
(11, '16500.00', '2021-02-20 18:12:34.575566', 'UD1033'),
(12, '3000.00', '2021-02-20 18:14:50.883607', 'Z61034'),
(13, '1500.00', '2021-02-20 18:17:56.991977', 'JC1035'),
(14, '2000.00', '2021-02-20 18:20:06.674816', 'HI1036'),
(15, '16500.00', '2021-02-20 18:20:41.331274', 'D31037'),
(16, '18000.00', '2021-02-20 18:21:08.125929', 'CQ1038'),
(17, '1500.00', '2021-02-23 11:26:56.305263', 'TJ1039'),
(18, '1500.00', '2021-02-23 11:28:26.640632', 'YM1040'),
(19, '16500.00', '2021-02-23 11:31:03.726160', '2L1041'),
(20, '1500.00', '2021-02-24 12:14:09.467847', 'NO1042');

-- --------------------------------------------------------

--
-- Table structure for table `hms_payment`
--

CREATE TABLE `hms_payment` (
  `id` bigint(20) NOT NULL,
  `channel` varchar(25) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `status` varchar(15) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `posted_by_id` int(11) DEFAULT NULL,
  `reservation_id` bigint(20) NOT NULL,
  `narration` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_payment`
--

INSERT INTO `hms_payment` (`id`, `channel`, `amount`, `status`, `timestamp`, `posted_by_id`, `reservation_id`, `narration`) VALUES
(5, 'transfer', '50000.00', 'completed', '2021-02-12 01:45:36.323480', 1, 1, ''),
(6, 'pos', '70050.00', 'completed', '2021-02-12 01:46:10.281226', 1, 1, ''),
(7, 'direct', '58250.00', 'completed', '2021-02-12 01:46:27.496202', 1, 2, ''),
(8, 'cash', '33500.00', 'completed', '2021-02-12 01:47:01.385726', 1, 2, ''),
(9, 'cash', '20400.00', 'completed', '2021-02-17 08:56:11.113995', 1, 2, 'Cash collected by: Opeyemi Akosile'),
(10, 'pos', '7500.00', 'completed', '2021-02-17 10:52:30.416302', 1, 2, 'Payment made with POS using debit/credit card'),
(11, 'direct', '7500.00', 'reversed', '2021-02-17 10:54:41.101357', 1, 2, 'Payment reversal for food order with id: 11'),
(13, 'transfer', '10000.00', 'completed', '2021-02-17 12:26:41.090982', 1, 2, 'Customer made bank transfer with reference id/NO: uyhsyu73881738kd'),
(14, 'pos', '60000.00', 'completed', '2021-02-17 14:44:23.438500', 1, 3, 'Payment made with POS using debit/credit card'),
(15, 'transfer', '58000.00', 'completed', '2021-02-18 06:59:44.255416', 1, 13, 'Customer made bank transfer with reference id/NO: Thdjuejj7948939892'),
(16, 'transfer', '58000.00', 'completed', '2021-02-18 07:02:17.060900', 1, 14, 'Customer made bank transfer with reference id/NO: Thdjuejj7948939892'),
(17, 'transfer', '58000.00', 'completed', '2021-02-18 07:03:39.824182', 1, 15, 'Customer made bank transfer with reference id/NO: Thdjuejj7948939892'),
(18, 'transfer', '58000.00', 'completed', '2021-02-18 07:04:13.065072', 1, 16, 'Customer made bank transfer with reference id/NO: Thdjuejj7948939892'),
(22, 'pos', '16100.00', 'completed', '2021-02-18 13:59:07.879636', 1, 13, 'Payment made with POS using debit/credit card'),
(24, 'cash', '9550.00', 'completed', '2021-02-18 15:34:15.733761', 1, 14, 'Cash collected by: Opeyemi Akosile'),
(25, 'cash', '8050.00', 'completed', '2021-02-18 15:37:17.820422', 1, 15, 'Cash collected by: Opeyemi Akosile'),
(26, 'cash', '9550.00', 'completed', '2021-02-18 16:00:32.549484', 1, 15, 'Cash collected by: Opeyemi Akosile'),
(27, 'transfer', '24500.00', 'completed', '2021-02-18 23:55:27.942860', 1, 17, 'Customer made bank transfer with reference id/NO: UU030394049HJSY'),
(28, 'direct', '24500.00', 'reversed', '2021-02-19 00:00:10.563317', 1, 17, 'Reversed canceled reservation credit balance'),
(29, 'direct', '108000.00', 'reversed', '2021-02-19 00:03:35.354750', 1, 13, 'Reversed closed reservation credit balance'),
(30, 'cash', '9550.00', 'completed', '2021-02-19 00:24:11.993803', 1, 14, 'Cash collected by: Opeyemi Akosile'),
(31, 'transfer', '5000.00', 'completed', '2021-02-19 07:31:30.943742', 1, 20, 'Customer made bank transfer with reference id/NO: '),
(32, 'cash', '24500.00', 'completed', '2021-02-19 07:31:31.095085', 1, 20, 'Cash collected by: Opeyemi Akosile'),
(33, '(\'coupon\',)', '2940.00', 'completed', '2021-02-19 13:41:14.677627', 1, 20, 'Coupon payment at 12.00% of total amount spent'),
(34, 'pos', '25000.00', 'completed', '2021-02-19 21:52:41.316006', 1, 20, 'Payment made with POS using debit/credit card'),
(35, 'coupon', '6939.00', 'completed', '2021-02-19 22:03:13.552105', 1, 14, 'Coupon payment at 9.00% of total amount spent'),
(36, 'pos', '-900.00', 'completed', '2021-02-19 22:28:23.783893', 1, 14, 'Payment made with POS using debit/credit card'),
(37, 'cash', '82500.00', 'completed', '2021-02-20 17:26:34.645518', 1, 14, 'Cash collected by: Opeyemi Akosile'),
(38, 'cash', '16500.00', 'completed', '2021-02-20 17:46:01.465864', 1, 14, 'Cash collected by: Opeyemi Akosile'),
(39, 'cash', '16500.00', 'completed', '2021-02-20 18:11:44.817067', 1, 14, 'Cash collected by: Opeyemi Akosile'),
(40, 'cash', '16500.00', 'completed', '2021-02-20 18:12:34.572734', 1, 14, 'Cash collected by: Opeyemi Akosile'),
(41, 'cash', '3000.00', 'completed', '2021-02-20 18:14:50.866124', 1, 14, 'Cash collected by: Opeyemi Akosile'),
(42, 'cash', '1500.00', 'completed', '2021-02-20 18:17:56.819811', 1, 14, 'Cash collected by: Opeyemi Akosile'),
(43, 'cash', '2000.00', 'completed', '2021-02-20 18:20:06.628930', 1, 14, 'Cash collected by: Opeyemi Akosile'),
(44, 'cash', '1500.00', 'completed', '2021-02-23 11:26:55.386640', 1, 14, 'Cash collected by: Opeyemi Akosile'),
(45, 'cash', '1500.00', 'completed', '2021-02-23 11:28:26.625665', 1, 14, 'Cash collected by: Opeyemi Akosile'),
(46, 'cash', '16500.00', 'completed', '2021-02-23 11:31:03.675253', 1, 14, 'Cash collected by: Opeyemi Akosile'),
(47, 'cash', '1500.00', 'completed', '2021-02-24 12:14:09.388060', 1, 15, 'Cash collected by: Opeyemi Akosile');

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
(27, 'Print Invoice', 'can_print_invoice', 'basic'),
(28, 'Cancel Reservation', 'can_cancel_reservation', 'management'),
(29, 'Cancel Order', 'can_cancel_order', 'management'),
(31, 'Update Bookings', 'can_update_bookings', 'management'),
(32, 'Close Reservation', 'can_close_reservation', 'management'),
(33, 'Add Coupon', 'can_add_coupon', 'management'),
(34, 'View Coupon', 'can_view_coupon', 'management'),
(35, 'Override Reservation', 'can_override_reservation', 'management'),
(36, 'Vendor Management', 'can_manage_vendor', 'management');

-- --------------------------------------------------------

--
-- Table structure for table `hms_reservation`
--

CREATE TABLE `hms_reservation` (
  `id` bigint(20) NOT NULL,
  `reference` varchar(12) NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `phone_number` varchar(15) NOT NULL,
  `status` varchar(15) NOT NULL,
  `credit_balance` decimal(20,2) NOT NULL,
  `amount_spent` decimal(20,2) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `gender` varchar(15) DEFAULT NULL,
  `amount_unpaid` decimal(20,2) NOT NULL,
  `corporate_name` varchar(255) DEFAULT NULL,
  `reservation_type` varchar(50) NOT NULL,
  `override_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_reservation`
--

INSERT INTO `hms_reservation` (`id`, `reference`, `first_name`, `last_name`, `phone_number`, `status`, `credit_balance`, `amount_spent`, `timestamp`, `created_by_id`, `gender`, `amount_unpaid`, `corporate_name`, `reservation_type`, `override_by_id`) VALUES
(1, 'J4SVT8NU0BCT', 'Opeyemi', 'Akosile', '08065546736', 'checked_out', '29950.00', '120050.00', '2021-02-12 01:46:10.346756', 1, 'male', '0.00', NULL, 'individual', NULL),
(2, 'KSRELQR4HJ2Y', 'Jerome', 'Coleman', '09065551148', 'checked_out', '41500.00', '112150.00', '2021-02-17 12:26:41.217847', 1, 'male', '0.00', NULL, 'individual', NULL),
(3, 'QRVES84K1XU0', 'Joshua', 'Adebayo', '09073874783', 'checked_out', '57000.00', '3000.00', '2021-02-17 14:44:23.581224', 1, 'male', '0.00', NULL, 'individual', NULL),
(8, 'OVQLDWFQFYTQ', 'Olaniyi', 'Eunice', '0908763647', 'canceled', '10000.00', '24500.00', '2021-02-16 11:44:17.604701', 1, 'female', '0.00', NULL, 'individual', NULL),
(9, 'GSLNHMYANQMK', '', '', '09083837642', 'canceled', '150000.00', '0.00', '2021-02-17 14:48:34.263788', 1, '', '0.00', 'Bethsaid Groups', 'corporate', NULL),
(10, '7FOWJ1U6Q8QO', 'Jason', 'Derulo', '0908378362', 'canceled', '0.00', '60000.00', '2021-02-16 10:55:20.049413', 1, 'female', '0.00', '', 'individual', NULL),
(13, 'LELCAJSRAVLM', 'Adekunle', 'Johnson', '08056726736', 'closed', '108000.00', '16100.00', '2021-02-19 00:03:35.265976', 1, 'male', '0.00', '', 'individual', NULL),
(14, 'OJGPEX8HINWZ', 'Adekunle', 'Johnson', '08056726736', 'closed', '6939.00', '266700.00', '2021-02-24 11:49:27.338489', 1, 'male', '32500.00', '', 'individual', 1),
(15, 'PG7RAUJQLADF', 'Adekunle', 'Johnson', '08056726736', 'active', '108000.00', '19100.00', '2021-02-24 12:14:09.379084', 1, 'male', '0.00', 'White Deck Resort', 'corporate', NULL),
(16, 'BMDQBTPRZPD3', 'Adekunle', 'Johnson', '08056726736', 'active', '50000.00', '58000.00', '2021-02-18 07:04:13.267593', 1, 'male', '0.00', 'White Deck Resort', 'corporate', NULL),
(17, 'VO8APTXSWY8I', '', '', '09078378367', 'canceled', '24500.00', '0.00', '2021-02-19 00:00:10.559312', 1, '', '0.00', 'Green White Green', 'corporate', NULL),
(20, '83LDWWF8VOGX', '', '', '0908978839', 'active', '27940.00', '24500.00', '2021-02-19 21:52:41.546814', 1, 'male', '0.00', 'Just another Group', 'corporate', NULL);

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
(1, 'Deluxe Room', 'Just another Deluxe Room', '24500.00', 100, 109, 9),
(2, 'Standard Room', 'Just another Standard Room', '14500.00', 200, 209, 10),
(3, 'Testing Room', 'Just testing Room', '6000.00', 100, 105, 6),
(4, 'Just testing Room', 'Just testing Room', '6700.00', 100, 103, 4);

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
(2, 'Samuel', 'Opeyemi', 'male', '0907383783', 'Account Officer', '', 3),
(3, 'Sammy', 'Samora', 'male', '09092763737', 'Bar Tender', '', 4),
(4, 'Samuel', 'Toke', 'female', '09076777675', 'Account Officer', '', 5),
(5, 'Rotimi', 'Mac', 'male', '0909087783', 'Account Officer', '', 6);

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
(26, '2021-02-12 01:15:55.875585', 27, 1),
(28, '2021-02-17 09:53:18.760289', 29, 1),
(29, '2021-02-18 22:46:01.251835', 28, 1),
(30, '2021-02-18 22:46:01.486877', 31, 1),
(31, '2021-02-18 23:53:19.456982', 32, 1),
(32, '2021-02-19 10:29:30.735071', 33, 1),
(33, '2021-02-19 10:29:30.842965', 34, 1),
(34, '2021-02-24 11:45:17.407290', 35, 1),
(35, '2021-02-24 11:45:17.476401', 36, 1);

-- --------------------------------------------------------

--
-- Table structure for table `hms_supply`
--

CREATE TABLE `hms_supply` (
  `id` bigint(20) NOT NULL,
  `description` varchar(500) NOT NULL,
  `status` varchar(20) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `amount_unpaid` decimal(20,2) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `vendor_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_supply`
--

INSERT INTO `hms_supply` (`id`, `description`, `status`, `amount`, `amount_unpaid`, `date_created`, `vendor_id`) VALUES
(6, 'Bought 10 crates of Jamesson Drink', 'unpaid', '145000.00', '135000.00', '2021-02-23 10:49:44.333765', 1);

-- --------------------------------------------------------

--
-- Table structure for table `hms_vendor`
--

CREATE TABLE `hms_vendor` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_vendor`
--

INSERT INTO `hms_vendor` (`id`, `name`, `address`) VALUES
(1, 'James Drink', 'No 76, agodi'),
(2, 'Mama Cap Rice Depot', 'No 7, Ojodu Abiodun Street');

-- --------------------------------------------------------

--
-- Table structure for table `hms_vendor_payment`
--

CREATE TABLE `hms_vendor_payment` (
  `id` bigint(20) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `status` varchar(15) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `posted_by_id` int(11) DEFAULT NULL,
  `supply_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hms_vendor_payment`
--

INSERT INTO `hms_vendor_payment` (`id`, `amount`, `status`, `timestamp`, `posted_by_id`, `supply_id`) VALUES
(1, '10000.00', 'completed', '2021-02-23 10:49:58.459899', 1, 6);

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
  ADD KEY `hms_booking_record_room_id_1f99642b_fk_hms_room_id` (`room_id`),
  ADD KEY `hms_booking_record_booked_by_id_38ddcd7e_fk_hms_staff_id` (`booked_by_id`),
  ADD KEY `hms_booking_record_payment_id_ee559d26_fk_hms_payment_id` (`payment_id`);

--
-- Indexes for table `hms_coupon`
--
ALTER TABLE `hms_coupon`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `hms_coupon_reservation_id_b36e46e2_fk_hms_reservation_id` (`reservation_id`);

--
-- Indexes for table `hms_drink`
--
ALTER TABLE `hms_drink`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `hms_drink_group_id_fada3094_fk_hms_options_id` (`group_id`);

--
-- Indexes for table `hms_drink_order`
--
ALTER TABLE `hms_drink_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hms_drink_order_drink_id_a75367a7_fk_hms_drink_id` (`drink_id`),
  ADD KEY `hms_drink_order_reservation_id_641704bb_fk_hms_reservation_id` (`reservation_id`),
  ADD KEY `hms_drink_order_completed_by_id_034048ab_fk_hms_staff_id` (`completed_by_id`),
  ADD KEY `hms_drink_order_registered_by_id_925d406a_fk_hms_staff_id` (`registered_by_id`),
  ADD KEY `hms_drink_order_payment_id_78bcb10d_fk_hms_payment_id` (`payment_id`),
  ADD KEY `hms_drink_order_order_id_afd65f98_fk_hms_order_id` (`order_id`);

--
-- Indexes for table `hms_food`
--
ALTER TABLE `hms_food`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `hms_food_group_id_6295032c_fk_hms_options_id` (`group_id`);

--
-- Indexes for table `hms_food_order`
--
ALTER TABLE `hms_food_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hms_food_order_food_id_f4f33934_fk_hms_food_id` (`food_id`),
  ADD KEY `hms_food_order_reservation_id_1abcddc8_fk_hms_reservation_id` (`reservation_id`),
  ADD KEY `hms_food_order_completed_by_id_a1b6dadc_fk_hms_staff_id` (`completed_by_id`),
  ADD KEY `hms_food_order_registered_by_id_7ec240c7_fk_hms_staff_id` (`registered_by_id`),
  ADD KEY `hms_food_order_payment_id_9ce43c23_fk_hms_payment_id` (`payment_id`),
  ADD KEY `hms_food_order_order_id_35be6ccb_fk_hms_order_id` (`order_id`);

--
-- Indexes for table `hms_options`
--
ALTER TABLE `hms_options`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hms_order`
--
ALTER TABLE `hms_order`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `order_ref` (`order_ref`);

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
  ADD KEY `hms_reservation_created_by_id_9aec3e14_fk_hms_staff_id` (`created_by_id`),
  ADD KEY `hms_reservation_override_by_id_5c56504e_fk_hms_staff_id` (`override_by_id`);

--
-- Indexes for table `hms_room`
--
ALTER TABLE `hms_room`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`) USING BTREE;

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
-- Indexes for table `hms_supply`
--
ALTER TABLE `hms_supply`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hms_supply_vendor_id_7dceb2e7_fk_hms_vendor_id` (`vendor_id`);

--
-- Indexes for table `hms_vendor`
--
ALTER TABLE `hms_vendor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `hms_vendor_payment`
--
ALTER TABLE `hms_vendor_payment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `hms_vendor_payment_posted_by_id_f5757f40_fk_hms_staff_id` (`posted_by_id`),
  ADD KEY `hms_vendor_payment_supply_id_177ba0bb_fk_hms_supply_id` (`supply_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- AUTO_INCREMENT for table `hms_auth`
--
ALTER TABLE `hms_auth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `hms_booking_record`
--
ALTER TABLE `hms_booking_record`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `hms_coupon`
--
ALTER TABLE `hms_coupon`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `hms_drink`
--
ALTER TABLE `hms_drink`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hms_drink_order`
--
ALTER TABLE `hms_drink_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `hms_food`
--
ALTER TABLE `hms_food`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `hms_food_order`
--
ALTER TABLE `hms_food_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `hms_options`
--
ALTER TABLE `hms_options`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `hms_order`
--
ALTER TABLE `hms_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `hms_payment`
--
ALTER TABLE `hms_payment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `hms_permission`
--
ALTER TABLE `hms_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `hms_reservation`
--
ALTER TABLE `hms_reservation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `hms_room`
--
ALTER TABLE `hms_room`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `hms_staff`
--
ALTER TABLE `hms_staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `hms_staff_permission`
--
ALTER TABLE `hms_staff_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `hms_supply`
--
ALTER TABLE `hms_supply`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `hms_vendor`
--
ALTER TABLE `hms_vendor`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hms_vendor_payment`
--
ALTER TABLE `hms_vendor_payment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
  ADD CONSTRAINT `hms_booking_record_booked_by_id_38ddcd7e_fk_hms_staff_id` FOREIGN KEY (`booked_by_id`) REFERENCES `hms_staff` (`id`),
  ADD CONSTRAINT `hms_booking_record_payment_id_ee559d26_fk_hms_payment_id` FOREIGN KEY (`payment_id`) REFERENCES `hms_payment` (`id`),
  ADD CONSTRAINT `hms_booking_record_reservation_id_50bc3b67_fk_hms_reservation_id` FOREIGN KEY (`reservation_id`) REFERENCES `hms_reservation` (`id`),
  ADD CONSTRAINT `hms_booking_record_room_id_1f99642b_fk_hms_room_id` FOREIGN KEY (`room_id`) REFERENCES `hms_room` (`id`);

--
-- Constraints for table `hms_coupon`
--
ALTER TABLE `hms_coupon`
  ADD CONSTRAINT `hms_coupon_reservation_id_b36e46e2_fk_hms_reservation_id` FOREIGN KEY (`reservation_id`) REFERENCES `hms_reservation` (`id`);

--
-- Constraints for table `hms_drink`
--
ALTER TABLE `hms_drink`
  ADD CONSTRAINT `hms_drink_group_id_fada3094_fk_hms_options_id` FOREIGN KEY (`group_id`) REFERENCES `hms_options` (`id`);

--
-- Constraints for table `hms_drink_order`
--
ALTER TABLE `hms_drink_order`
  ADD CONSTRAINT `hms_drink_order_completed_by_id_034048ab_fk_hms_staff_id` FOREIGN KEY (`completed_by_id`) REFERENCES `hms_staff` (`id`),
  ADD CONSTRAINT `hms_drink_order_drink_id_a75367a7_fk_hms_drink_id` FOREIGN KEY (`drink_id`) REFERENCES `hms_drink` (`id`),
  ADD CONSTRAINT `hms_drink_order_order_id_afd65f98_fk_hms_order_id` FOREIGN KEY (`order_id`) REFERENCES `hms_order` (`id`),
  ADD CONSTRAINT `hms_drink_order_payment_id_78bcb10d_fk_hms_payment_id` FOREIGN KEY (`payment_id`) REFERENCES `hms_payment` (`id`),
  ADD CONSTRAINT `hms_drink_order_registered_by_id_925d406a_fk_hms_staff_id` FOREIGN KEY (`registered_by_id`) REFERENCES `hms_staff` (`id`),
  ADD CONSTRAINT `hms_drink_order_reservation_id_641704bb_fk_hms_reservation_id` FOREIGN KEY (`reservation_id`) REFERENCES `hms_reservation` (`id`);

--
-- Constraints for table `hms_food`
--
ALTER TABLE `hms_food`
  ADD CONSTRAINT `hms_food_group_id_6295032c_fk_hms_options_id` FOREIGN KEY (`group_id`) REFERENCES `hms_options` (`id`);

--
-- Constraints for table `hms_food_order`
--
ALTER TABLE `hms_food_order`
  ADD CONSTRAINT `hms_food_order_completed_by_id_a1b6dadc_fk_hms_staff_id` FOREIGN KEY (`completed_by_id`) REFERENCES `hms_staff` (`id`),
  ADD CONSTRAINT `hms_food_order_food_id_f4f33934_fk_hms_food_id` FOREIGN KEY (`food_id`) REFERENCES `hms_food` (`id`),
  ADD CONSTRAINT `hms_food_order_order_id_35be6ccb_fk_hms_order_id` FOREIGN KEY (`order_id`) REFERENCES `hms_order` (`id`),
  ADD CONSTRAINT `hms_food_order_payment_id_9ce43c23_fk_hms_payment_id` FOREIGN KEY (`payment_id`) REFERENCES `hms_payment` (`id`),
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
  ADD CONSTRAINT `hms_reservation_created_by_id_9aec3e14_fk_hms_staff_id` FOREIGN KEY (`created_by_id`) REFERENCES `hms_staff` (`id`),
  ADD CONSTRAINT `hms_reservation_override_by_id_5c56504e_fk_hms_staff_id` FOREIGN KEY (`override_by_id`) REFERENCES `hms_staff` (`id`);

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

--
-- Constraints for table `hms_supply`
--
ALTER TABLE `hms_supply`
  ADD CONSTRAINT `hms_supply_vendor_id_7dceb2e7_fk_hms_vendor_id` FOREIGN KEY (`vendor_id`) REFERENCES `hms_vendor` (`id`);

--
-- Constraints for table `hms_vendor_payment`
--
ALTER TABLE `hms_vendor_payment`
  ADD CONSTRAINT `hms_vendor_payment_posted_by_id_f5757f40_fk_hms_staff_id` FOREIGN KEY (`posted_by_id`) REFERENCES `hms_staff` (`id`),
  ADD CONSTRAINT `hms_vendor_payment_supply_id_177ba0bb_fk_hms_supply_id` FOREIGN KEY (`supply_id`) REFERENCES `hms_supply` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

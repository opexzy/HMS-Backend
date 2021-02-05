-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 05, 2021 at 08:41 PM
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
(48, 'Can view staff permission model', 12, 'view_staffpermissionmodel');

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
(4, 'contenttypes', 'contenttype'),
(8, 'hms_auth', 'authmodel'),
(9, 'hms_auth', 'authtokenmodel'),
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
(23, 'staff', '0001_initial', '2021-01-26 09:36:05.951534');

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
('181fabe9c716b2c88f873062883105e66ab46984', '2021-02-05 19:12:23.212243', '2021-02-05 19:39:27.186146', 1);

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
(4, 'Create Reservation', 'can_create_reservation', 'basic'),
(5, 'View EOD', 'can_view_eod', 'management'),
(6, 'Edit Staff Permission', 'can_edit_staff_permission', 'admin');

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
(1, 'Opeyemi', 'Akosile', 'male', '07065551148', 'Manager', NULL, 1),
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
(4, '2021-02-05 18:23:39.428985', 6, 1);

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
-- Indexes for table `hms_permission`
--
ALTER TABLE `hms_permission`
  ADD PRIMARY KEY (`id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `hms_auth`
--
ALTER TABLE `hms_auth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `hms_permission`
--
ALTER TABLE `hms_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `hms_staff`
--
ALTER TABLE `hms_staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hms_staff_permission`
--
ALTER TABLE `hms_staff_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

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

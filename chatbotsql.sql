/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - chatbot
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`chatbot` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `chatbot`;

/*Table structure for table `articles` */

DROP TABLE IF EXISTS `articles`;

CREATE TABLE `articles` (
  `article_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `article_name` varchar(100) DEFAULT NULL,
  `articles` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`article_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `articles` */

insert  into `articles`(`article_id`,`teacher_id`,`article_name`,`articles`,`date`) values (1,6,'magazine','/static/articles_file/220316-090849.jpg','2022-03-16');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`from_id`,`to_id`,`message`,`date`) values (1,0,6,'hy','2022-05-08'),(2,0,6,'helo','2022-05-08'),(3,0,6,'hy','2022-05-08'),(4,0,6,'yes','2022-05-08'),(5,7,6,'hy','2022-05-08'),(6,6,7,'ya','2022-05-08');

/*Table structure for table `chatboat` */

DROP TABLE IF EXISTS `chatboat`;

CREATE TABLE `chatboat` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `questions` varchar(200) DEFAULT NULL,
  `answers` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `chatboat` */

insert  into `chatboat`(`question_id`,`questions`,`answers`) values (1,'Hi','Hello'),(2,'what are 10 top courses?','Medical and bilogical sciences,pure mathematics and statics,business Administration and sales.'),(3,'which course is best for today?','Top trending online courses...data science,Artificial inteligence and machine learning,big data,cloud computing,full stack development'),(4,'what are the 4 year UG course','BFA,BSW,BSPA,BSN,B.phil'),(5,'How can i get full scholarship to study abroad?','These are most commo application requirements for scholarship..1.registration or application form,2.letter or motivation or personal easy,3.letter for acceptance from an academic institution,5.proof o'),(6,'who can apply for scholarships?','Anyone who meets the application requirements can apply.These are most commo application requirements for scholarship..1.registration or application form,2.letter or motivation or personal easy,3.lett'),(7,'How to find study abroad scholarships?','Scholarshipportal.com,Scholarships.com');

/*Table structure for table `chatbotchat` */

DROP TABLE IF EXISTS `chatbotchat`;

CREATE TABLE `chatbotchat` (
  `chatbot_chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `botmsg` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chatbot_chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=latin1;

/*Data for the table `chatbotchat` */

insert  into `chatbotchat`(`chatbot_chat_id`,`from_id`,`to_id`,`botmsg`,`date`) values (1,7,1,'course','2022-05-08'),(2,7,1,'hy','2022-05-08'),(3,7,1,'hi','2022-05-08'),(4,7,1,'hi','2022-05-08'),(5,7,1,'Hi','2022-05-08'),(6,7,1,'Hi','2022-05-08'),(7,7,1,'Hi','2022-05-08'),(8,7,1,'Hi','2022-05-08'),(9,7,1,'Hi','2022-05-08'),(10,7,1,'helo','2022-05-08'),(11,7,1,'helo','2022-05-08'),(12,7,1,'hw','2022-05-08'),(13,7,1,'yes','2022-05-08'),(14,7,1,'hi','2022-05-08'),(15,7,1,'hi','2022-05-08'),(16,7,1,'hi','2022-05-08'),(17,7,1,'yes','2022-05-08'),(18,7,1,'yes','2022-05-08'),(19,7,1,'yes','2022-05-08'),(20,7,1,'top course','2022-05-08'),(21,7,1,'top courses','2022-05-08'),(22,7,1,'top courses','2022-05-08'),(23,7,1,'top courses','2022-05-08'),(24,7,1,'top courses','2022-05-08'),(25,1,7,'0.16173823818875438','2022-05-08'),(26,7,1,'top courses ','2022-05-08'),(27,7,1,'top courses ','2022-05-08'),(28,1,7,'0.16173823818875438','2022-05-08'),(29,7,1,'top courses ','2022-05-08'),(30,1,7,'0.16173823818875438','2022-05-08'),(31,7,1,'top courses ','2022-05-08'),(32,1,7,'0.16173823818875438','2022-05-08'),(33,1,7,'0.7904144933273127','2022-05-08'),(34,1,7,'0.6183699008800341','2022-05-08'),(35,1,7,'0.5994640005780326','2022-05-08'),(36,1,7,'0.5693345888568139','2022-05-08'),(37,7,1,'top courses ','2022-05-08'),(38,1,7,'0.5754760814459617','2022-05-08'),(39,1,7,'0.16173823818875438','2022-05-08'),(40,1,7,'0.7904144933273127','2022-05-08'),(41,1,7,'0.5828961371481515','2022-05-08'),(42,1,7,'0.6183699008800341','2022-05-08'),(43,1,7,'0.5994640005780326','2022-05-08'),(44,1,7,'0.5693345888568139','2022-05-08'),(45,1,7,'0.5754760814459617','2022-05-08'),(46,1,7,'0.5828961371481515','2022-05-08'),(47,7,1,'Hi','2022-05-08'),(48,7,1,'Hi','2022-05-08'),(49,1,7,'1.0','2022-05-08'),(50,1,7,'0.3174081647161003','2022-05-08'),(51,1,7,'0.30113130102016866','2022-05-08'),(52,1,7,'0.3314735756806698','2022-05-08'),(53,7,1,'Hi','2022-05-08'),(54,1,7,'1.0','2022-05-08'),(55,1,7,'0.36617287383761854','2022-05-08'),(56,1,7,'0.3174081647161003','2022-05-08'),(57,1,7,'0.27503324729244527','2022-05-08'),(58,1,7,'0.28562869910989314','2022-05-08'),(59,1,7,'0.30113130102016866','2022-05-08'),(60,1,7,'0.3314735756806698','2022-05-08'),(61,7,1,'top courses ','2022-05-08'),(62,7,1,'top courses ','2022-05-08'),(63,1,7,'0.16173823818875438','2022-05-08'),(64,1,7,'0.16173823818875438','2022-05-08'),(65,1,7,'0.7904144933273127','2022-05-08'),(66,1,7,'0.7904144933273127','2022-05-08'),(67,1,7,'0.6183699008800341','2022-05-08'),(68,1,7,'0.6183699008800341','2022-05-08'),(69,1,7,'0.5994640005780326','2022-05-08'),(70,1,7,'0.5994640005780326','2022-05-08'),(71,1,7,'0.5693345888568139','2022-05-08'),(72,1,7,'0.5693345888568139','2022-05-08'),(73,1,7,'0.5754760814459617','2022-05-08'),(74,1,7,'0.5754760814459617','2022-05-08'),(75,1,7,'0.5828961371481515','2022-05-08'),(76,1,7,'0.5828961371481515','2022-05-08'),(77,7,1,'top courses ','2022-05-08'),(78,7,1,'top courses ','2022-05-08'),(79,1,7,'c','2022-05-08'),(80,1,7,'c','2022-05-08'),(81,7,1,'top courses ','2022-05-08'),(82,7,1,'top courses ','2022-05-08'),(83,1,7,'Medical and bilogical sciences,pure mathematics and statics,business Administration and sales.','2022-05-08'),(84,1,7,'Medical and bilogical sciences,pure mathematics and statics,business Administration and sales.','2022-05-08'),(85,7,1,'apply scholarship ','2022-05-08'),(86,1,7,'Anyone who meets the application requirements can apply.These are most commo application requirements for scholarship..1.registration or application form,2.letter or motivation or personal easy,3.lett','2022-05-08'),(87,7,1,'yes','2022-05-08'),(88,7,1,'yes','2022-05-08'),(89,7,1,'yes','2022-05-08'),(90,7,1,'yes','2022-05-08'),(91,1,7,'Sorry.. i didnt get you','2022-05-08'),(92,1,7,'Sorry.. i didnt get you','2022-05-08'),(93,1,7,'Sorry.. i didnt get you','2022-05-08'),(94,1,7,'Sorry.. i didnt get you','2022-05-08');

/*Table structure for table `event` */

DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
  `event_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `events` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `event` */

insert  into `event`(`event_id`,`teacher_id`,`events`,`description`,`date`,`status`) values (2,2,'cbhrfbvh','ccrcjferfh','2022-03-08','approved'),(4,NULL,'exam','series exam','2022-03-11','pending'),(5,6,'quiz','tgyhb gvcfv ','2022-03-15','pending');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `feedbacks` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`student_id`,`feedbacks`,`date`) values (1,1,'bcfhbvchbdfvgbhbhfbgvfb','2022-03-15');

/*Table structure for table `group_members` */

DROP TABLE IF EXISTS `group_members`;

CREATE TABLE `group_members` (
  `group_member_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`group_member_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `group_members` */

insert  into `group_members`(`group_member_id`,`group_id`,`student_id`) values (1,3,1);

/*Table structure for table `groups` */

DROP TABLE IF EXISTS `groups`;

CREATE TABLE `groups` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `group_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `groups` */

insert  into `groups`(`group_id`,`teacher_id`,`group_name`) values (2,6,'group1');

/*Table structure for table `ideas` */

DROP TABLE IF EXISTS `ideas`;

CREATE TABLE `ideas` (
  `idea_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `ideas` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`idea_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `ideas` */

insert  into `ideas`(`idea_id`,`teacher_id`,`ideas`,`date`) values (1,NULL,'huh','2022-03-11'),(2,6,'vtftvgbhn','2022-03-15');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values (1,'admin','admin','admin'),(2,' binu','binu','teacher'),(7,'a','a','student'),(6,'binuthottath99@gmail.com','binu@1999','teacher'),(8,'g@gmail.com','gs','student'),(9,'fv@gmail .com','yh','student');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`notification`,`date`) values (1,'bjigv',NULL),(2,'',NULL),(3,'ji','2022-03-10');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `ratings` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`student_id`,`ratings`,`date`) values (1,1,'udhcudhc','2022-03-15');

/*Table structure for table `rating_article` */

DROP TABLE IF EXISTS `rating_article`;

CREATE TABLE `rating_article` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `ratings` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `article_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `rating_article` */

insert  into `rating_article`(`rating_id`,`student_id`,`ratings`,`date`,`article_id`) values (1,1,'5.0','2022-04-21',1);

/*Table structure for table `rating_ideas` */

DROP TABLE IF EXISTS `rating_ideas`;

CREATE TABLE `rating_ideas` (
  `rating_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `ratings` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `idea_id` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `rating_ideas` */

insert  into `rating_ideas`(`rating_id`,`student_id`,`ratings`,`date`,`idea_id`) values (NULL,1,'3.0','2022-04-22',1);

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) DEFAULT NULL,
  `student_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(6) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `course` varchar(100) DEFAULT NULL,
  `phoneno` int(11) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`student_id`,`student_name`,`place`,`post`,`pin`,`photo`,`gender`,`course`,`phoneno`,`email`) values (7,'asx','aaa','frdc',34567,'dcbjh','dcnd','cdbchs',2147483647,'bchdbdyed'),(8,'gg','hh','hgh',33,'/static/st','Female','cgg',2565,'g@gmail.com'),(9,'ggh','ggh','utt',6599,'/static/student_photo/220508-170947.jpg','Female','fgg',6653,'fv@gmail .com');

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `teacher_id` int(11) DEFAULT NULL,
  `teacher_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(6) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `qualification` varchar(100) DEFAULT NULL,
  `phoneno` bigint(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `teacher` */

insert  into `teacher`(`teacher_id`,`teacher_name`,`place`,`post`,`pin`,`photo`,`gender`,`qualification`,`phoneno`,`email`) values (2,'hjbhb','hgvgv',' bbhb',675437,' bv',' vgg',' cfcbhb',67548979,' vgvv'),(6,'binu','ang','ang',679321,'/static/teacher_photo/220311-095434.jpg','female','mca',9746442164,'binuthottath99@gmail.com'),(7,'Anusree','Melattur','Melattur',679322,'/static/teacher_photo/220316-140624.jpg','Female','b.ed',8891926264,'anuthottath001@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

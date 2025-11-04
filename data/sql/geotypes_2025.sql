/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.13-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: topkar
-- ------------------------------------------------------
-- Server version	10.11.13-MariaDB-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `geotypes`
--

DROP TABLE IF EXISTS `geotypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `geotypes` (
  `id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `short_ru` varchar(32) DEFAULT NULL COMMENT 'Short description in Russian',
  `name_ru` varchar(64) NOT NULL COMMENT 'Name in Russian',
  `desc_ru` varchar(255) DEFAULT NULL COMMENT 'Description in Russian',
  `short_en` varchar(32) DEFAULT NULL COMMENT 'Short description in English',
  `name_en` varchar(64) DEFAULT NULL COMMENT 'Name in English',
  `desc_en` varchar(255) DEFAULT NULL COMMENT 'Description in English',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_ru_UNIQUE` (`name_ru`),
  UNIQUE KEY `short_ru_UNIQUE` (`short_ru`),
  UNIQUE KEY `short_en_UNIQUE` (`short_en`),
  UNIQUE KEY `name_en_UNIQUE` (`name_en`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin COMMENT='Types of geographic objects (geo features).';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `geotypes`
--

LOCK TABLES `geotypes` WRITE;
/*!40000 ALTER TABLE `geotypes` DISABLE KEYS */;
INSERT INTO `geotypes` VALUES
(1,NULL,'участок',NULL,NULL,'plot, section',NULL),
(2,NULL,'пожога',NULL,NULL,'burnt clearing',NULL),
(3,'с.','село',NULL,NULL,'rural locality',NULL),
(4,NULL,'луда','каменистая прибрежная мель',NULL,'luda','rocky littoral shoal or islet'),
(5,NULL,'омут',NULL,NULL,'deep pool',NULL),
(6,NULL,'полуостров',NULL,'Pen.','peninsula',NULL),
(7,NULL,'камень',NULL,NULL,'stone',NULL),
(8,NULL,'родник',NULL,'Spg.','spring, wellspring',NULL),
(9,NULL,'колхоз','предприятие в СССР, созданное для коллективного ведения сельского хозяйства',NULL,'collective farm','Soviet collective farm'),
(10,NULL,'канава',NULL,NULL,'ditch','ditch, gutter, drain, trench'),
(11,NULL,'порог',NULL,'Rpd.','rapid, threshold',NULL),
(12,NULL,'пастбище',NULL,NULL,'pasture','meadow pasture'),
(13,NULL,'нива','пахотная земля, пригодная для обработки и сельскохозяйственного использования, но в данный момент она может быть как засаженной, так и находиться под паром (неиспользуемой)',NULL,'arable land',NULL),
(14,NULL,'смолокурня',NULL,NULL,'tar kiln',NULL),
(15,NULL,'мост',NULL,'Br.','bridge',NULL),
(16,'б-г','берег',NULL,NULL,'shore',NULL),
(17,NULL,'прогон',NULL,NULL,'cattle drive, pasture trail',NULL),
(18,NULL,'яма',NULL,NULL,'pit',NULL),
(19,NULL,'пролив',NULL,'Str.','strait',NULL),
(20,NULL,'мель',NULL,'Sh.','shoal',NULL),
(21,'д.','деревня',NULL,'Vlg.','village',NULL),
(22,NULL,'мыс',NULL,'C.','cape',NULL),
(23,NULL,'ручей',NULL,'Bk.','stream, brook',NULL),
(24,NULL,'покос',NULL,NULL,'hayfield',NULL),
(25,NULL,'озеро',NULL,'L.','lake',NULL),
(26,'р.','река',NULL,'R.','river',NULL),
(27,NULL,'поле','открытая территория, включает пахотные и непахотные земли','Fld.','field',NULL),
(28,NULL,'бор',NULL,NULL,'pinewood','pinewood, pine forest'),
(29,NULL,'дом',NULL,NULL,'house',NULL),
(30,NULL,'овраг',NULL,'Gul.','ravine, gully',NULL),
(31,NULL,'лес',NULL,'Frst.','forest',NULL),
(32,NULL,'колодец','узкая и глубокая, защищённая от обвалов яма для добывания воды из водоносных слоёв земли','W.','well','a hole sunk into the ground as a source of water'),
(33,NULL,'губа','геогр. залив моря или озера, обычно являющийся устьем крупной реки',NULL,'inlet','bay or inlet of a sea or lake (usually at the mouth of a large river)'),
(34,NULL,'ламба','малое, как правило, бессточное пресноводное лесное озеро',NULL,'lamba','forest lake'),
(35,'дор.','дорога',NULL,'Rd.','road',NULL),
(36,NULL,'пруд',NULL,'Pd.','pond',NULL),
(37,NULL,'часовня',NULL,'Chap.','chapel',NULL),
(38,NULL,'угодье',NULL,NULL,'land, hunting ground',NULL),
(39,NULL,'крест',NULL,NULL,'cross',NULL),
(40,'хут.','хутор',NULL,'Hmlt.','hamlet',NULL),
(41,NULL,'рига',NULL,NULL,'drying barn',NULL),
(42,NULL,'болото',NULL,'Swp.','swamp','bog, swamp, marsh, quagmire, mire'),
(43,NULL,'кузница','мастерская, в которой производится ручная обработка металла, как правило, ковкой',NULL,'smithy','the location where a smith (particularly a blacksmith) works, a forge'),
(44,NULL,'скала',NULL,'Cl.','cliff, rock',NULL),
(45,NULL,'церковь',NULL,'Ch.','church',NULL),
(46,'зал.','залив',NULL,'B.','bay',NULL),
(47,'уроч.','урочище',NULL,'Tract.','tract',NULL),
(48,NULL,'тоня','традиционное рыболовное хозяйство или место, где ведётся добыча и обработка рыбы',NULL,'fishery','a traditional fishing industry or place where fish are caught and processed; fishing camp, fishing station'),
(49,NULL,'мельница',NULL,'Ml.','mill',NULL),
(50,NULL,'место',NULL,NULL,'place',NULL),
(51,NULL,'остров',NULL,'Is.','island',NULL),
(52,NULL,'кладбище','специально отведённое место, предназначенное для погребения, захоронения умерших людей','Cem.','cemetery','cemetery, graveyard'),
(53,NULL,'гора',NULL,'Mt.','mountain',NULL),
(54,NULL,'пристань',NULL,NULL,'pier, wharf',NULL),
(55,NULL,'поляна',NULL,NULL,'glade, clearing',NULL),
(56,NULL,'шахта',NULL,'M.','mine',NULL),
(57,NULL,'маяк',NULL,'Lh.','lighthouse',NULL),
(59,NULL,'часть реки',NULL,NULL,'part of a river',NULL),
(60,NULL,'часть озера',NULL,NULL,'part of a lake',NULL),
(62,NULL,'улица',NULL,'St.','street',NULL),
(63,NULL,'поселение',NULL,NULL,'inhabited place',NULL),
(64,NULL,'протока',NULL,'Chan.','channel',NULL),
(65,NULL,'плёс',NULL,NULL,'stretch of river, reach',NULL),
(66,NULL,'дерево',NULL,NULL,'tree',NULL),
(67,NULL,'плотина',NULL,'Dm.','dam',NULL),
(68,NULL,'монастырь',NULL,NULL,'monastery',NULL),
(69,'терр.','территория',NULL,NULL,'territory',NULL),
(70,NULL,'море',NULL,NULL,'sea',NULL),
(71,NULL,'гумно',NULL,NULL,'threshing floor',NULL),
(72,NULL,'отмель',NULL,NULL,'sandbank, shoal',NULL),
(73,NULL,'перевоз',NULL,NULL,'ferry crossing',NULL),
(74,NULL,'волок',NULL,NULL,'portage',NULL),
(75,NULL,'закол',NULL,NULL,'fish weir',NULL),
(76,NULL,'ток','место глухариного тока',NULL,'lek','place of wood grouse mating'),
(77,NULL,'часть деревни',NULL,NULL,'part of a village',NULL),
(78,NULL,'местность',NULL,NULL,'locality, terrain',NULL),
(79,NULL,'низина',NULL,NULL,'lowland',NULL),
(80,NULL,'перешеек',NULL,'Isth.','isthmus',NULL),
(81,NULL,'межа',NULL,NULL,'division','abutment, abuttal, boundary, margin, division (as in land plots)'),
(82,NULL,'поворот',NULL,NULL,'turn, bend',NULL),
(83,NULL,'устье',NULL,NULL,'river mouth',NULL),
(84,NULL,'часть мыса',NULL,NULL,'part of a cape',NULL),
(85,NULL,'выгон','общинный выпас, выгул скота рядом с поселением, см. пастбище',NULL,'commons','communal grazing, grazing of livestock near a settlement, see pasture'),
(86,NULL,'фамилия',NULL,NULL,'surname',NULL),
(87,NULL,'постройка',NULL,NULL,'building, structure',NULL),
(88,'вдп.','водопад',NULL,'Wf.','waterfall',NULL),
(89,NULL,'изба',NULL,NULL,'hut','izba, (peasant\'s) log hut, cottage'),
(90,NULL,'тропа',NULL,'Tr.','trail, path',NULL),
(91,'п.','поселок',NULL,'t.','town',NULL),
(92,NULL,'перекресток',NULL,NULL,'crossroads',NULL),
(93,'г.','город',NULL,'Cy','city',NULL),
(94,NULL,'бочага','впадина, яма, заполненная водой; глубокая лужа',NULL,'pit with water','(regional) a hollow, a pit filled with water; deep puddle'),
(95,NULL,'заводь',NULL,NULL,'creek',NULL),
(96,NULL,'лесопункт',NULL,NULL,'lumber camp',NULL),
(97,NULL,'зимник','дорога, проложенная по снегу',NULL,'ice road','a seasonal winter road over frozen terrain and/or frozen bodies of water'),
(98,NULL,'просека',NULL,NULL,'clearing, cut-line',NULL),
(99,NULL,'мостки',NULL,NULL,'footbridge',NULL),
(100,'ст.','станция',NULL,'Stn.','station',NULL),
(101,'мест.','местечко',NULL,NULL,'mestechko',NULL),
(102,'пгт','посёлок городского типа',NULL,'uts','urban-type settlement',NULL),
(103,'раз.','разъезд',NULL,'Sdg.','siding',NULL),
(104,NULL,'пудас',NULL,NULL,'fish trap',NULL),
(105,NULL,'бухта',NULL,'Cv.','bay, cove',NULL),
(106,NULL,'карьер',NULL,'Qy.','quarry',NULL),
(107,'выс.','выселок',NULL,NULL,'small settlement',NULL),
(108,NULL,'часть поселения',NULL,NULL,'part of a settlement',NULL),
(109,NULL,'барак',NULL,NULL,'barrack',NULL),
(110,'кол. пос.','колонизационный поселок','Пенитенциарный институт, существовавший в 1930-е годы, – колонизационные поселки исправительно-трудовых лагерей (ИТЛ), специально организованные для проживания и работы там заключенных, к которым могли приехать семьи.',NULL,'colonization settlement',NULL),
(111,'л. изба','лесная изба',NULL,NULL,'forest hut',NULL),
(112,'гид. мет. ст.','гидрометеорологическая станция',NULL,NULL,'hydrometeorological station',NULL),
(113,NULL,'казарма',NULL,NULL,'barracks',NULL),
(114,NULL,'развалины',NULL,NULL,'ruins',NULL),
(116,NULL,'склон',NULL,NULL,'slope',NULL),
(117,NULL,'изгородь',NULL,NULL,'fence',NULL),
(118,NULL,'лужа',NULL,NULL,'puddle',NULL),
(119,NULL,'расщелина',NULL,NULL,'crevice, fissure',NULL),
(120,NULL,'лабиринт',NULL,NULL,'labyrinth, maze',NULL),
(121,NULL,'ущелье',NULL,'G.','gorge, canyon',NULL),
(122,NULL,'рыбный забор',NULL,NULL,'fish trap, weir',NULL),
(123,NULL,'лесозавод',NULL,NULL,'timber mill',NULL),
(124,NULL,'варница',NULL,NULL,'saltworks',NULL),
(125,NULL,'лесоучасток',NULL,NULL,'forest plot',NULL),
(126,'н.п.','населённый пункт',NULL,'settl.','settlement',NULL),
(127,NULL,'фарватер',NULL,NULL,NULL,NULL),
(128,NULL,'прорубь',NULL,NULL,'ice hole',NULL),
(129,NULL,'роща',NULL,NULL,'lehto',NULL),
(130,NULL,'часть моря',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `geotypes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-04 22:32:06

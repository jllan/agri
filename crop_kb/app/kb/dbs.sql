CREATE TABLE `crop` (
  `crop_id` tinyint NOT NULL AUTO_INCREMENT,
  `crop` varchar(20) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`crop_id`),
  UNIQUE(`crop`)	
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `ftime` (
  `ftime_id` tinyint NOT NULL AUTO_INCREMENT,
  `ftime` varchar(20) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`ftime_id`),
  UNIQUE(`ftime`)		
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `ftype` (
  `ftype_id` tinyint NOT NULL AUTO_INCREMENT,
  `ftype` varchar(20) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`ftype_id`),
  UNIQUE(`ftype`)		
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `farming` (
  `fid` tinyint NOT NULL AUTO_INCREMENT,
  `crop_id` tinyint NOT NULL,
  `ftime_id` tinyint NOT NULL,
  `ftype_id` tinyint NOT NULL,	
  `fdetail` text CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`fid`),
  KEY `farming_crop_id_foreign` (`crop_id`),
  CONSTRAINT `farming_crop_id_foreign` FOREIGN KEY (`crop_id`) REFERENCES `crop` (`crop_id`) ON DELETE CASCADE,
  KEY `farming_ftime_id_foreign` (`ftime_id`),
  CONSTRAINT `farming_ftime_id_foreign` FOREIGN KEY (`ftime_id`) REFERENCES `ftime` (`ftime_id`) ON DELETE CASCADE,
  KEY `farming_ftype_id_foreign` (`ftype_id`),
  CONSTRAINT `farming_ftype_id_foreign` FOREIGN KEY (`ftype_id`) REFERENCES `ftype` (`ftype_id`) ON DELETE CASCADE	
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


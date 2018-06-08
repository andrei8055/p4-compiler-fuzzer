CREATE TABLE fuzzer.bugs (
	id INT NOT NULL AUTO_INCREMENT,
	test varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
	error TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
	file varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
	seed bigint(20) unsigned NOT NULL DEFAULT '0',
	known BOOL DEFAULT False NOT NULL,
	CONSTRAINT bugs_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=latin1
COLLATE=latin1_swedish_ci ;

CREATE TABLE `tamed_bugs` (
  `bug_id` int(11) NOT NULL,
  `cluster` int(11) NOT NULL,
  `is_medoid` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`bug_id`),
  CONSTRAINT `tamed_bugs_bugs_FK` FOREIGN KEY (`bug_id`) REFERENCES `bugs` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1

CREATE TABLE `tests` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test` varchar(255) CHARACTER SET utf8 NOT NULL,
  `seed` bigint(20) unsigned NOT NULL DEFAULT '0',
  `unique_tokens` int(20) unsigned NOT NULL DEFAULT '0',
  `tokens` int(20) unsigned NOT NULL DEFAULT '0',
  `f_size` int(20) unsigned NOT NULL DEFAULT '0',
  `compile_time` float DEFAULT NULL,
  `generate_time` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10548 DEFAULT CHARSET=latin1;

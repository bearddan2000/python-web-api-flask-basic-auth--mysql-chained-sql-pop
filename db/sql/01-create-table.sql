DROP TABLE IF EXISTS `beverage`.pop;

CREATE TABLE `beverage`.pop (
	id INT PRIMARY KEY auto_increment,
	name varchar(25) NOT NULL,
	color varchar(10) NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;

-- Set up MySQL server for testing
-- This is basically the exact same thing as setup_mysql_dev.sql

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

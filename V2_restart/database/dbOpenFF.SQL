CREATE DATABASE DBOpenFF;
USE DBOpenFF;


CREATE TABLE categories (
                ID INT AUTO_INCREMENT NOT NULL,
                category_name VARCHAR(300) NOT NULL,
                PRIMARY KEY (ID)
) ENGINE=INNODB;


CREATE TABLE products (
                ID INT AUTO_INCREMENT NOT NULL,
                product_name VARCHAR(300) NOT NULL,
                category_name VARCHAR(300),
                category_id INT NOT NULL,
                nutrition_grade CHAR(1) NOT NULL,
                product_desc VARCHAR(1500) NOT NULL,
                product_store VARCHAR(500),
                product_url VARCHAR(1000) NOT NULL,
                substitute_id INT DEFAULT 1 NOT NULL,
                PRIMARY KEY (ID)
) ENGINE=INNODB;



CREATE TABLE products_by_category (
                ID INT AUTO_INCREMENT NOT NULL,
                category_id INT NOT NULL,
                product_id INT NOT NULL,
                PRIMARY KEY (ID)
) ENGINE=INNODB;


ALTER TABLE products_by_category ADD CONSTRAINT category_category_products_fk
FOREIGN KEY (category_id)
REFERENCES categories (ID);

ALTER TABLE products_by_category ADD CONSTRAINT product_category_products_fk
FOREIGN KEY (product_id)
REFERENCES products (ID);

ALTER TABLE products ADD CONSTRAINT products_products_fk
FOREIGN KEY (substitute_id)
REFERENCES products (ID);




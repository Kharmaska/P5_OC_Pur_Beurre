CREATE DATABASE DBOpenFF;
USE DBOpenFF;


-- TABLE for categories
CREATE TABLE categories (
                ID INTEGER NOT NULL AUTO_INCREMENT,
                category_name VARCHAR(300) NOT NULL,
                CONSTRAINT categories_pk PRIMARY KEY (ID)
) ENGINE=INNODB;

-- TABLE for products
CREATE TABLE products (
                ID INTEGER NOT NULL AUTO_INCREMENT,
                product_name VARCHAR(300) NOT NULL,
                category_name VARCHAR(300),
                category_id INTEGER NOT NULL,
                nutrition_grade CHAR(1) NOT NULL,
                product_desc VARCHAR(1500) NOT NULL,
                product_url VARCHAR(1000) NOT NULL,
                substitute_id INTEGER NOT NULL,
                CONSTRAINT products_pk PRIMARY KEY (ID)
) ENGINE=INNODB;


CREATE TABLE products_by_category (
                ID INTEGER NOT NULL AUTO_INCREMENT,
                category_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                CONSTRAINT products_by_category_pk PRIMARY KEY (ID)
) ENGINE=INNODB;


ALTER TABLE products_by_category ADD CONSTRAINT Category_category_products_fk
FOREIGN KEY (category_id)
REFERENCES categories (ID);

ALTER TABLE products_by_category ADD CONSTRAINT product_category_products_fk
FOREIGN KEY (product_id)
REFERENCES products (ID);

ALTER TABLE products ADD CONSTRAINT products_products_fk
FOREIGN KEY (substitute_id)
REFERENCES products (ID);
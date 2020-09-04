CREATE DATABASE DBOpenFF;
USE DBOpenFF;

-- TABLE : product
CREATE TABLE product (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    category_id SMALLINT(6) UNSIGNED NULL,
    product_name VARCHAR(300) NOT NULL,
    category_name VARCHAR(300) NULL,
    nutrition_grade CHAR(1) NOT NULL,    
    PRIMARY KEY (id)
)  ENGINE=INNODB;

-- TABLE : category
CREATE TABLE category (
    id INT UNSIGNED AUTO_INCREMENT NOT NULL,
    category_name VARCHAR(300) NOT NULL,
    PRIMARY KEY (id)
)  ENGINE=INNODB;

-- TABLE : substitute
CREATE TABLE substitute (
    saved_product_id INT UNSIGNED NOT NULL,
    saved_product_name VARCHAR(800) NOT NULL,
    saved_product_grade CHAR(1) NOT NULL,
    saved_substitute_id INT UNSIGNED NOT NULL,
    saved_substitute_name VARCHAR(800) NOT NULL,
    saved_substitute_grade CHAR(1) NOT NULL,
    saved_substitute_url VARCHAR(1000) NOT NULL,
    saved_substitute_store VARCHAR(500)  NULL       
)  ENGINE=INNODB;

-- TABLE : category_products
CREATE TABLE category_products (
    product_id INT UNSIGNED,
    category_id INT UNSIGNED
)  ENGINE=INNODB;

-- CREATE FOREIGN KEY

-- FK category_products : product_id
ALTER TABLE category_products
ADD CONSTRAINT fk_cat_prod_product_id FOREIGN KEY (product_id) REFERENCES product(id);

-- FK category_product : category_id
ALTER TABLE category_products
ADD CONSTRAINT fk_cat_prod_category_id FOREIGN KEY (category_id) REFERENCES category(id);

-- FK substitute :  substitute_product_id (fk : nom de table _ id)
ALTER TABLE substitute
ADD CONSTRAINT fk_sav_prod_product_id FOREIGN KEY (saved_product_id) REFERENCES product(id);



-- CREATE INDEXES

-- Index category : category_name
ALTER TABLE category
ADD INDEX ind_cat_name (category_name);

-- Index product : product_name
ALTER TABLE product
ADD INDEX ind_product_name (product_name);




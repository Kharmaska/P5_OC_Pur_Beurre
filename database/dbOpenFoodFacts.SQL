CREATE DATABASE DBOpenFF;
USE DBOpenFF;

-- TABLE : product
CREATE TABLE product (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    category_id SMALLINT(6) UNSIGNED NULL,
    product_name VARCHAR(300) NOT NULL,
    category_name VARCHAR(300) NULL,
    nutrition_grade CHAR(1) NOT NULL,
    product_url VARCHAR(1000) NOT NULL,
    product_store VARCHAR(500) NULL,
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
    saved_substitute_grade CHAR(1) NOT NULL
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

-- FK substitute : substitute_substitute_id
ALTER TABLE substitute
ADD CONSTRAINT fk_sav_subs_product_id FOREIGN KEY (saved_substitute_id) REFERENCES product(id);


-- CREATE INDEXES

-- Index category : category_name
ALTER TABLE category
ADD INDEX ind_cat_name (category_name);

-- Index product : product_name
ALTER TABLE product
ADD INDEX ind_product_name (product_name);


-- TEST data for testing - To be removed once python script to connect with OFF is created

-- insert data into the Products table
INSERT INTO Product VALUES (1,123,'Coucou-Cola','Boissons gazeuses', 'D','www.coucou-cola.fat',"Le Gras C'est la vie"),
(2,1234,'NesLow','Petit-déjeuner', 'E','www.NesLow.sugar','Tout pour le petit déj'),
(3,12345,'Coquinou','Saucisses', 'E','www.Biendecheznous.fr','Carrouf');


-- insert data  into the Category table
INSERT INTO Category VALUES (123,'Boissons gazeuses'),
(1234,'Petit-déjeuner'),
(12345,'Saucisses');
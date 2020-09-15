"""
This module will be responsible for the Database objet
It will handle database creation and use
"""
import mysql.connector as mysql
import config


class Database:
    def __init__(self, user, password):
        self.localdb = mysql.connect(
            host = 'localhost', user = user, password = password
        )
        self.mycursor = self.localdb.cursor()

    def clear_favorites(self):
        # Removes all the favorite products for the user
        self.mycursor.execute("USE dbopenff")
        
        self.mycursor.execute("""
             UPDATE products
             SET favorite = False
             WHERE favorite = True                    
        """)
        return print("Vos favoris ont été effacés !")

    def create(self):
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS dbopenff")
        
        self.mycursor.execute("USE dbopenff")
        
        self.mycursor.execute("""
            CREATE TABLE categories (
                ID INT AUTO_INCREMENT NOT NULL,
                category_name VARCHAR(300) NOT NULL,
                PRIMARY KEY (ID)
            ) ENGINE=INNODB;
            """)

        self.mycursor.execute("""
            CREATE TABLE products (
                ID INT NOT NULL,
                product_name VARCHAR(300) NOT NULL,
                category_name VARCHAR(300),
                category_id INT NOT NULL,
                nutrition_grade CHAR(1) NOT NULL,
                product_desc VARCHAR(1500) NOT NULL,
                product_url VARCHAR(1000) NOT NULL,
                favorite BOOLEAN DEFAULT False NOT NULL,
                substitute_id INT NULL,
                PRIMARY KEY (ID)
                ) ENGINE=INNODB;
            """)

        self.mycursor.execute("""
            CREATE TABLE products_by_category (
                ID INT AUTO_INCREMENT NOT NULL,
                category_id INT NOT NULL,
                product_id INT NOT NULL,
                PRIMARY KEY (ID)
                ) ENGINE=INNODB;
            """)

        self.mycursor.execute("""
            ALTER TABLE products_by_category ADD CONSTRAINT category_category_products_fk
            FOREIGN KEY (category_id)
            REFERENCES categories (ID);
            """)

        self.mycursor.execute("""
            ALTER TABLE products_by_category ADD CONSTRAINT product_category_products_fk
            FOREIGN KEY (product_id)
            REFERENCES products (ID);
            """)

        self.mycursor.execute("""
            ALTER TABLE products ADD CONSTRAINT products_products_fk
            FOREIGN KEY (substitute_id)
            REFERENCES products (ID);
            """)
        return print("Création de la base de données réussie")

newdb = Database('root','Snoopy1909!')
newdb.clear_favorites()
newdb.create()

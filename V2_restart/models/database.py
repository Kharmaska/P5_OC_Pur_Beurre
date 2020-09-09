"""
This module will be responsible for the Database objet
It will handle database creation and use
"""
import mysql.connector as mysql
import config

class Database:
    def __init__(self, user, password):
        self.localdb = mysql.connect(
            host = config.HOST, user = user, password = password,
            database = config.DATABASE
        )
        self.mycursor = self.localdb.cursor()
        
    def db_exist(self):
        #if the database exist USE Database
        pass
        
    def create(self):
        #If the database DOES NOT exist - use dbOpenFF.SQL script to create database
        pass
    
    
        
    

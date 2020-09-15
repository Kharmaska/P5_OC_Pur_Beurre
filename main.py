#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""
This program gathers data from 10 pre-selected categories of products on
Openfoodfacts.org. It then creates a local database of products per category.
The user can then select a product from the local database that will return an healthier
alternative. The user will also have the option to add a selected product and its substitute
to a list of favorites.
"""

from models.category import Category
from models.product import Product
import mysql.connector as mysql
import config

# Database initialization

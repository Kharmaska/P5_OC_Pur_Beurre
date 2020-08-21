# Project n°: OC_Pur_Beurre

## 1. Purpose of the application

The main goal of this little application is to propose the customers from the company Pur Beurre an access to healthier alternatives to their favorite products (eg. Nutella, Coca Cola, Kinder, etc.).
The application is using the [Open Food Facts REST API](https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest) to provide such information along side with a nearby store to purchase the product alternative.

This program was developped as part of my Master 1 degree at OpenClassRooms.
For the purpose of the exercise, I will be using Doc Driven Developement before programming any functionnality in Python.

Please note that as Pur Beurre is a fictive French company only serving French customers, the program will only return the French products of the Open Food Facts database.
  
## 2. Installation

### VirtualEnv

 You will first need to install a Python Virtual Environment.
 To that matter, open a Terminal on your computer (Powershell on Windows, Bash on Mac or Linux) and proceed as follows:

#### a. Installing VirtualEnv

Open your terminal and type in:

```bash
 pip install virtualenv
```

#### b. Creating your virtualEnv

Open the terminal into the folder where you have installed the application's files and type the following:

```bash
virtualenv -p python3 env
```

if you are on Windows's PowerShell:

```powershell
 virtualenv -p $env:python3 env
```

This should have created an ENV or VENV folder in the installation folder for the app.

#### c. Activating your virtualEnv

 In order to activate the VirtualEnv then you would need to run the following command:

```bash
 source env/bin/activate
```

if VENV folder was created:

```bash
 source venv/bin/activate
```

if you are on Windows's PowerShell:

```powershell
 ./env/scripts/activate.ps1

 OR if you created a 'venv' folder and not an 'env' folder

 ./venv/scripts/activate.ps1
```

### 3.2 Installing dependencies

In order to install the required dependencies you will have to enter the following command in your terminal

```bash
 pip install -r requirements.txt
 ```

 In case you would like to modify the version of any of the dependencies, you can do so by modifying the requirements.txt file and then by running again the command above

## 3. User Journey description

The user will be using a Python Terminal to execute the program and will be served with the following choices:

1 - Which aliment would you like to substitute?
2 - Retrieve my list of substituted aliments.

When the use selects the **option '1'**, the application is asking the following questions:

* Please select a category | Each category is linked to an interger used by the customer to make a choise (e.g: 46 - Nuts)
* Please select an aliment | Each aliment or product is associated to an interger; again this is how the customer will be able to select a product from a given category
* The program serves a proposed alternative, its description, a link to the Open Food Facts page for that product and a retailer where to purchase it
* The user then has the possibility to save that result in the Database for later | The user can chose to save the result by picking the corresponding number in the proposed options

When the use selects the **option '2'**, the application is leading the user to a list of previously saved products and aliments.

## 4. Functionalities and User Stories

**User Stories:**

* As a new user, I want to be able to create a new database in which I will be able to store my prefered alternative products
* As a user, I want that the data saved is using MySQL database so I can easily and quickly retrieve my data on a later use of the program
* As a user, I want to be able to reconnecte to the database on which I saved OFF products, so I don't have to go through the database creation process again and finding products I already searched for.
* As a user, I want to be able to select a product or a category just by entering their number in the terminal so I don't have to type the full name of the category or the product
* As a user, I want that the system asks me the same question until I enter a valid number so I can only use the options available in the system

**Functionalities:**

* Categories: For the purpose of this exercise, [The API Call on Categories](https://fr.openfoodfacts.org/categories.json) should be limited to only food categories with more than 20 products listed.
* Products: Once a category is selected, the user should be served with a list of products based this example [API Call on a specific Category](https://fr.openfoodfacts.org/categorie/pommes-de-terre-charlotte.json)

TBD

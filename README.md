# Project n°: OC_Pur_Beurre

## 1. Purpose of the application

The main goal of this little application is to propose the customers from the company Pur Beurre an access to healthier alternatives to their favorite products (eg. Nutella, Coca Cola, Kinder, etc.).
The application is using the Open Food Facts REST API to provide such information along side with a nearby store to purchase the product alternative.
  
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

## 4. Functionalities

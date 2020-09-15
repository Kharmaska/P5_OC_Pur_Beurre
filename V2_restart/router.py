#!/usr/bin/python3
# -*- coding: Utf-8 -*


def display_options():
    """
    Function responsible for greeting the user on program execution.
    The user will have to choose between 3 options.
    On Categories or Saved Products selection, the function will call on
    corresponding functions to guide the user through more choices.
    """
    while True:
        choice = input("\nBienvenue sur l'application Pur Beurre ! \n"
                "   \n"
                "Veuillez effectuer un choix : \n"
                "   \n"
                "1- Remplacer un produit alimentaire. \n"
                "2- Retrouver mes aliments favoris. \n"
                "3- Quitter le programme. \n"
                "Entrez le chiffre correspondant à votre choix :\n")
        if choice == "1":

            display_categories()
        elif choice == "2":

            display_saved_prodcuts()
        elif choice == "3":
            print("Merci d'avoir utiliser Pur Beurre, à bientôt !")
            break
        else:
            print("===========\n"
                  "   \n"
                  "Merci d'entrer un chiffre valide.\n"
                  "\n===========\n")

def display_categories():
    """
    Function responsible for displaying the 10 available categories of products

    """
    categories_dict = {
        1 : {
            "name" : "Pizzas",
            "url" : "https://fr.openfoodfacts.org/categorie/pizzas.json"

        },
        2 : {
            "name" : "Snacks",
            "url" : "https://fr.openfoodfacts.org/categorie/snacks.json"

        },
        3 : {
            "name" : "Boissons",
            "url" : "https://fr.openfoodfacts.org/categorie/boissons.json"

        },
        4 : {
            "name" : "Apéritif",
            "url" : "https://fr.openfoodfacts.org/categorie/aperitif.json"

        },
        5 : {
            "name" : "Plats préparés",
            "url" : "https://fr.openfoodfacts.org/categorie/plats-prepares.json"

        },
        6 : {
            "name" : "Biscuits et gâteaux",
            "url" : "https://fr.openfoodfacts.org/categorie/biscuits-et-gateaux.json"
      
        },
        7 : {
            "name" : "Produits à tartiner sucrés",
            "url" : "https://fr.openfoodfacts.org/categorie/produits-a-tartiner-sucres.json"

        },
        8 : {
            "name" : "Surgelés",
            "url" : "https://fr.openfoodfacts.org/categorie/surgeles.json"

        },
        9 : {
            "name" : "Yaourts",
            "url" : "https://fr.openfoodfacts.org/categorie/yaourts.json"

        },
        10 : {
            "name" : "Pâtisseries",
            "url" : "https://fr.openfoodfacts.org/categorie/patisseries.json"

        },
    }
    # Ici on récupérera la liste des 10 catégories pré-sélectionnées
    #  et incluse dans un dictionnaire python
        # 1- Pizzas
        # 2- Boissons
        # 3-Le gras c'est la vie, etc
    # Puis on boucle sur la liste pour afficher les nom des catégories avec un choix numérique
    
    for category in categories_dict:
        print (str(category) + " : " + categories_dict[category]['name'])
        input("Veuillez choisir l'une des catégories de produits suivantes en tapant son chiffre: \n")
        if int(input) == category:
            print("Vous avez sélectionné la catégorie" + categories_dict[category]['name'])
            print("voici la liste des produits disponibles : ")
            # ici on boucle sur la liste de 100 produits disponibles pour la 
            # catégorie dans la BDD locale
        else:
            break
    # On récupère l'input utilisateur
    # On boucle sur la liste des 100 premiers produits de la catégorie
    # L'utilisateur sélectionne un produit dans la liste
    # On affiche un substitut avec un meilleur nutriscore
    # print("Example: Vous avez sélectionné le produit X d'un nutriscore 'E', qui peut être remplacé par Y qui a un score de 'C'")
    # On propose à l'utilisateur de sauvegarder son produit ainsi que le substitut proposé
    # print("Souhaitez-vous sauvegarder votre produit pour plus tard ?")
    # Input Oui, on insert le produit dans la table des saved_product ou alors on ajoute un champ boolean saved product sur le produit
    # Input Non, on repropose la liste de 100 produits de la catégorie

def display_saved_prodcuts():
    # On boucle sur la table saved_product ou alors on affiche tous les product dont le champ favorite vaut True.
    print("On imagine ici qu'on a une liste de produits déjà pre-save")

display_options()


from random import randint

# Variables globales pour les limites du jeu
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NMBRE_VIES = 5

# Fonction principale
def main():
    while True:
        print("\n*** Bienvenue dans l'application multi-fonctions ***")
        show_options()
        choix = demander_entier("👉 Votre choix : ", 1, 4)
        
        if choix == 1:
            calculator()
        elif choix == 2:
            course_app()
        elif choix == 3:
            game_myst()
        elif choix == 4:
            print("Au revoir !")
            break

# Afficher le menu principal
def show_options():
    print('''
        Menu de l'app :
        1: Calculatrice  
        2: Gestion des courses
        3: Le jeu du Nombre Mystère
        4: Quitter
    ''')

# Demande un entier valide entre une plage donnée
def demander_entier(message, min_val=None, max_val=None):
    while True:
        try:
            valeur = int(input(message))
            if (min_val is not None and valeur < min_val) or (max_val is not None and valeur > max_val):
                print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
            else:
                return valeur
        except ValueError:
            print("ERREUR: Vous devez entrer un nombre valide.")

# Fonction pour le calculateur
def calculator():
    print("\n*** Calculatrice ***")
    nombre1 = demander_entier("Entrez un premier nombre : ")
    nombre2 = demander_entier("Entrez un deuxième nombre : ")
    somme = nombre1 + nombre2
    print(f"Le résultat de l'addition de {nombre1} et {nombre2} vaut {somme}")

# Gestion des courses
listes = []

def course_app():
    while True:
        print("\n*** Gestion des courses ***")
        display_option()
        choix = demander_entier("👉 Votre choix : ", 1, 6)
        
        if choix == 1:
            add_list()
        elif choix == 2:
            remove_item()
        elif choix == 3:
            display_item()
        elif choix == 4:
            update_item()
        elif choix == 5:
            remove_all_item()
        elif choix == 6:
            print("Retour au menu principal.")
            break

def display_option():
    print('''
       1: Ajouter un élément à la liste 
       2: Retirer un élément de la liste 
       3: Afficher la liste
       4: Modifier un élément de la liste 
       5: Vider la liste
       6: Retour
    ''')

def add_list():
    add_item = input("Entrez l'élément à ajouter : ").strip()
    if add_item:
        listes.append(add_item)
        print(f"L'élément '{add_item}' a bien été ajouté.")
    else:
        print("ERREUR: Vous devez entrer un élément à ajouter.")

def display_item():
    if not listes:
        print("Votre liste est vide.")
    else:
        print("Voici votre liste :")
        for i, item in enumerate(listes, 1):
            print(f"{i}. {item}")

def remove_item():
    display_item()
    if listes:
        choix = demander_entier("Entrez le numéro de l'élément à retirer : ", 1, len(listes))
        item = listes.pop(choix - 1)
        print(f"L'élément '{item}' a bien été retiré.")

def update_item():
    display_item()
    if listes:
        choix = demander_entier("Entrez le numéro de l'élément à modifier : ", 1, len(listes))
        nouvel_item = input("Entrez le nouvel élément : ").strip()
        if nouvel_item:
            listes[choix - 1] = nouvel_item
            print("L'élément a bien été modifié.")
        else:
            print("ERREUR: Vous devez entrer un nouvel élément.")

def remove_all_item():
    if listes:
        confirmation = input("Voulez-vous vraiment vider la liste ? (o/n) : ").lower()
        if confirmation == 'o':
            listes.clear()
            print("La liste a été vidée.")
    else:
        print("La liste est déjà vide.")

# Jeu du Nombre Mystère
def game_myst():
    NOMBRE_MAGIQUE = randint(NOMBRE_MIN, NOMBRE_MAX)
    vie = 0

    print("\n*** Jeu du Nombre Mystère ***")
    while vie < NMBRE_VIES:
        print(f"Il vous reste {NMBRE_VIES - vie} vies.")
        nbre = demander_entier(f"Devinez le nombre (entre {NOMBRE_MIN} et {NOMBRE_MAX}) : ", NOMBRE_MIN, NOMBRE_MAX)

        if nbre == NOMBRE_MAGIQUE:
            print(f"Bravo ! Vous avez trouvé le nombre mystère ({NOMBRE_MAGIQUE}) en {vie + 1} essais.")
            return
        elif nbre > NOMBRE_MAGIQUE:
            print("Le nombre mystère est plus petit.")
        else:
            print("Le nombre mystère est plus grand.")
        
        vie += 1

    print(f"Dommage, vous avez perdu ! Le nombre mystère était {NOMBRE_MAGIQUE}.")

# Lancer l'application
main()

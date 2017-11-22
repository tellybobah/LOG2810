"""
@author: Boubacar, Abderahmane, Leandre
"""

from delevery import Delevery

def main():
    user_input = 'f'
    delevery = Delevery()
    while(user_input != 'd'):
        print("(a) Creer automate")
        print("(b) Traiter des requetes")
        print("(c) Afficher les statistiques")
        print("(d) Quitter")
        user_input = input()
        
        if user_input == 'a':

            user_txt_input = input()
            if delevery.parse_request(user_txt_input):
                print('Arbre d\'adresse cree')
            else:
                print('Erreur dans le nom du fichier')
        elif user_input == 'b':
            pass
        elif user_input == 'c':
            pass
        elif user_input == 'd':
            pass
        else:
            print("Mauvaise entree")
            
if __name__ == "__main__":
    main()
"""
@author: Boubacar, Abderahmane, Leandre
"""

from delivery import Delivery

def main():
    user_input = 'e'
    delivery = Delivery()
    while(user_input != 'd'):
        print("(a) Creer automate")
        print("(b) Traiter des requetes")
        print("(c) Afficher les statistiques")
        print("(d) Quitter")
        user_input = input()
        
        if user_input == 'a':
            print("Entrez le nom du txt")
            user_txt_input = input()
            if delivery.create_automaton(user_txt_input):
                print('Arbre d\'adresse cree')
            else:
                print('Erreur dans le nom du fichier')
        elif user_input == 'b':
            print("Entrez le fichier qui de la requete")
            user_txt_input = input()
            if delivery.parse_request(user_txt_input):
                delivery.equilibrate_swarm()
                delivery.deliver_packages()
            else:
                print('Erreur dans le nom du fichier')
            
        elif user_input == 'c':
            delivery.print_statistics()
        elif user_input == 'd':
            pass
        else:
            print("Mauvaise entree")
            
if __name__ == "__main__":
    main()
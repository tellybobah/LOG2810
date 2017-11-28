"""
@author: Boubacar, Abderahmane, Leandre
"""

from delivery import Delivery

def main():
    user_input = 'e'
    delivery = Delivery()
    while(user_input != 'd'):
        print()
        print("(a) Creer automate")
        print("(b) Traiter des requetes")
        print("(c) Afficher les statistiques")
        print("(d) Quitter")
        user_input = input()
        
        if user_input == 'a':
            print("Entrez le nom du txt :", end=' ')
            user_txt_input = input()
            delivery = Delivery()
            if delivery.create_automaton(user_txt_input):
                print('Arbre d\'adresse cree')
                delivery.equilibrate_swarm()
            else:
                print('Erreur dans le nom du fichier!')
        elif user_input == 'b':
            print("Entrez le fichier qui de la requete :", end=' ')
            user_txt_input = input()
            if delivery.parse_request(user_txt_input):
                delivery.deliver_packages()
                delivery.equilibrate_swarm()
            else:
                print('Erreur dans le nom du fichier!')
            
        elif user_input == 'c':
            print()
            delivery.print_statistics()
        elif user_input == 'd':
            pass
        else:
            print("Mauvaise entree!")
            
if __name__ == "__main__":
    main()
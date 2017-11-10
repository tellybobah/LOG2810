# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:35:05 2017

@author: Léandre
"""

from graph import *
from dijkstra import *
from hasse import *
from drone import Package
import os.path


def menu_drones():
    user_input = None
    is_loaded_file = False
    while(user_input != 'c'):
        print()
        print("(a) Mettre a jour la carte")
        print("(b) Determiner le plus court chemin securitaire")
        print("(c) Quitter")
        user_input = input()
        
        if user_input == 'a':
            file_name = input('Veuiller entrer le nom du fichier: ')
            if os.path.isfile(file_name) :
                drone_map = GraphDrone(file_name)
                is_loaded_file = True
            else: 
                print('Erreur, le fichier n\' a pas été trouvé')
                continue

        elif user_input == 'b':
            if is_loaded_file == False:
                print('Erreur, le fichier n\' a pas été généré')
                continue
            
            print("Choisir le noeud de debut: ", end = '')
            debut = int(input())
            print("Choisir le noeud de fin: ", end = '')
            fin = int(input())
            
            print("Choisir le packet a apporter: ")
            print("(a) Leger")
            print("(b) Medium")
            print("(c) Lourd")
            package_input = input()
            package = None
            if package_input == "a":
                package = Package.LIGHT
            elif package_input == "b":
                package = Package.MEDIUM
            elif package_input == "c":
                package = Package.HEAVY
                
            if debut in drone_map.connections.keys() and fin in drone_map.connections.keys() and package != None:
                dijk = Dijkstra(drone_map)
                dijk.solution(debut, fin, package)    
            else:
                print("Desole, impossible de calculer le chemin")
        elif user_input == 'c':
            pass
        else:
            print("Mauvaise entree")

def menu_recettes():
    user_input = None
    is_loaded_file = False
    while(user_input != 'c'):
        print()
        print("(a) Creer et afficher le graphe de recettes")
        print("(b) Generer et afficher le diagramme de Hasse")
        print("(c) Quitter")
        user_input = input()
        
        if user_input == 'a':
            file_name = input('Veuiller entrer le nom du fichier: ')
            if os.path.isfile(file_name) :
                recette_map = GraphRecette(file_name)
                is_loaded_file = True
            else: 
                print('Erreur, le fichier n\' a pas été trouvé')
                continue
            print()
            recette_map.display()
            print()
        elif user_input == 'b':
            if is_loaded_file == False:
                print('Erreur, le fichier n\' a pas été généré')
                continue
            hasse_diagram = Hasse(recette_map)
            hasse_diagram.remove_relexivity()
            hasse_diagram.remove_transitivity()
            print()
            hasse_diagram.print_hasse()
            print()
        elif user_input == 'c':
            pass
        else:
            print("Mauvaise entree")

def main():
    user_input = 'd'
    
    while(user_input != 'c'):
        print("(a) Drones")
        print("(b) Recettes")
        print("(c) Quitter")
        user_input = input()
        
        if user_input == 'a':
            menu_drones()
        elif user_input == 'b':
            menu_recettes()
        elif user_input == 'c':
            pass
        else:
            print("Mauvaise entree")
            
if __name__ == "__main__":
    main()
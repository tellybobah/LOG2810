# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:35:05 2017

@author: Léandre
"""

from graph import *
from dijkstra import *
from drone import Package
from node import Node

def menu_drones():
    drone_map = GraphDrone('drone/arrondissements.txt')
    user_input = 'd'
    while(user_input != 'c'):
        print("(a) Mettre a jour la carte")
        print("(b) Determiner le plus court chemin securitaire")
        print("(c) Quitter")
        user_input = input()
        
        if user_input == 'a':
            drone_map = GraphDrone('drone/arrondissements.txt')
        elif user_input == 'b':
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
    dessert_map = GraphDessert('desserts/manger.txt')
    user_input = 'd'
    while(user_input != 'c'):
        print("(a) Creer et afficher le graphe de recettes")
        print("(b) Generer et afficher le diagramme de Hasse")
        print("(c) Quitter")
        user_input = input()
        
        if user_input == 'a':
            dessert_map = GraphDessert('recette/manger.txt')
            #TODO: Ajouter un display du graphe apres lecture, sans reduction
            #dessert_map.display()
        elif user_input == 'b':
            #generate_hasse()
            pass
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
            
            
main()
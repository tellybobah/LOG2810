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


drone_map = GraphDrone('arrondissements.txt')
              
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
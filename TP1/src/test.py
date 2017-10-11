"""
@author: Boubacar, Abderahmane, Leandre
"""
import util
from graph import GraphDrone
from dijkstra import *
from util import timeit
from node import Node

g = GraphDrone('drone/arrondissements.txt')
#g.display()

path, distance = shortest_path(g, Node(2), Node(5), None)

#mettre dans une fonction?
print('Path:')
for n in reversed(path):
    print(n, '-> ', end='')

print('Distance:', distance)
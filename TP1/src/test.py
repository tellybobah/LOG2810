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

def ex1():
    path, distance = shortest_path(g, Node(2), Node(5), None)
    print('Path:')
    for n in reversed(path):
        print(n, '-> ', end='')

    print('Distance:', distance)

ex1()
#g.plot()



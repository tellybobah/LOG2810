"""
@author: Boubacar, Abderahmane, Leandre
"""
import util
from graph import GraphDrone
from dijkstra import *
from util import timeit
from node import Node
from drone import *

#g.display()

def ex1():
    drone = Drone3Amp(Package.LIGHT)
    g = GraphDrone('drone/arrondissements.txt')
    path, distance = shortest_path(g, Node(15), Node(2), drone, g.list_stations)
    print('Path:')
    for n in reversed(path):
        print(n, '-> ', end='')

    print('Distance:', distance)

ex1()

print(d.getEnergy())



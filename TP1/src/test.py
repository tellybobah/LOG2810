"""
@author: Boubacar, Abderahmane, Leandre
"""
import util
from graph import *
#from dijkstra import *
from util import timeit
from node import Node
from drone import *
from Hasse import *

#g.display()

#def ex1():
 #   drone = Drone3Amp(Package.LIGHT)
 #   g = GraphDrone('drone/arrondissements.txt')
 #   path, distance = shortest_path(g, Node(15), Node(2), drone, g.list_stations)
 #   print('Path:')
 #   for n in reversed(path):
  #      print(n, '-> ', end='')

   # print('Distance:', distance)
    
def ex2():
    g1 = GraphDessert('desserts/manger.txt')
    Has = Hasse()
    test_trans = dict()
    test_trans[1] = [4,6] 
    test_trans[2] = [3,6]
    test_trans[3] = [4]
    test_trans[4] = [5]
    test_trans[5] = [6]
    test_trans[6] = []
    Has.remove_relexivity(g1.connections)
    #print(*g1.connections)
    Has.remove_transitivity(g1.connections)
    #Has.removeTransitivity(test_trans)
    Has.printHasse(g1.connections)
#ex1()
ex2()
#print(d.getEnergy())



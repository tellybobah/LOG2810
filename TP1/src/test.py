"""
@author: Boubacar, Abderahmane, Leandre
"""

from graph import *
from dijkstra import *
from node import Node
from drone import *
from hasse import Hasse

    
def ex2():
    g1 = GraphDessert('recette/manger.txt')
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
    Has.print_hasse(g1, g1.connections)

ex2()




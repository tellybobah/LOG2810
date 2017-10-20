"""
@author: Boubacar, Abderahmane, Leandre
"""
from graph import GraphDrone
from dijkstra import Dijkstra
from drone import Package
from node import Node

#g.display()

def ex1():
    g = GraphDrone('drone/arrondissements.txt')
    d = Dijkstra(g)
    start_node = Node(8)
    end_node = Node(17)
    d.solution(start_node,end_node, Package.LIGHT)
    

ex1()



from graph import GraphDrone
from dijkstra import *

g = GraphDrone('drone/arrondissements.txt')
#g.display()

shortest_path(g, 1, 5, None)
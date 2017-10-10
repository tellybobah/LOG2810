from graph import GraphDrone
from dijkstra import *

g = GraphDrone('drone/arrondissements.txt')
#g.display()

path, distance = shortest_path(g, 2, 5, None)
print('Path:', path)
print('Distance:', distance)
"""
@author: Boubacar, Abderahmane, Leandre
"""
from node import Node

class Graph:
    pass

class GraphDrone(Graph):
    def __init__(self, file_name):
        #self.connections = defaultdict(list)
        self.connections = {}
        self.list_stations = set()
        self.parse_file(file_name)

    def parse_file(self,file_name):
        with open(file_name) as file:
            for line in file:
                if line == '\n':
                    break
                else:
                    node, is_station = map(int, line.strip().split(','))
                    self.connections.update({Node(node):{}})
                    #print('Hash Debug', hash(Node(node,'')), hash(node))
                    if is_station == 1:
                        self.list_stations.add(node)

            for line in file:
                if line == '\n':
                    break
                else:
                    node1, node2, distance = map(int, line.strip().split(','))
                    self.connections[node1].update({node2: distance})
                    self.connections[node2].update({node1: distance})                    

    def getNeighbours(self, node):
        return self.connections[node]

    def display(self):
        for node, neighbours in self.connections.items():
            print(node, ':', neighbours)
        print('List of stations:', self.list_stations)

    def generate_matix():
        pass

class GraphDessert(Graph):
    def __init__(self):
        pass

    def parse_file(self):
        pass



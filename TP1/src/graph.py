"""
Created on Wed Oct  4 10:12:43 2017

@author: Boubacar
"""
from collections import defaultdict
from node import Node

class GraphDrone:
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
                    node, isStation = map(int, line.strip().split(','))
                    self.connections.update({node:[]})
                    if isStation == '1':
                        self.list_stations.add(node)

            for line in file:
                if line == '\n':
                    break
                else:
                    node1, node2, distance = map(int, line.strip().split(','))
                    self.connections[node1].append((node2, distance))
                    self.connections[node2].append((node1, distance))                    

    def getNeighbours(self, node):
        return self.connections[node]

    def display(self):
        for node, neighbours in self.connections.items():
            print(node, ':', neighbours)

        print('List of stations:', self.list_stations)

class GraphDessert:
    def __init__(self):
        pass

"""
@author: Boubacar, Abderahmane, Leandre
"""
from node import Node

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import takewhile

class Graph:
    pass

class GraphDrone(Graph):
    def __init__(self, file_name):
        node_lines, edge_lines = self.parse_file(file_name)
        self.create_graph(node_lines, edge_lines)

    def parse_file(self, file_name):
        with open(file_name) as file:
            node_lines = list(takewhile(lambda x : x != '\n', file))
            edge_lines = list(takewhile(lambda x : x != '\n', file))
            return node_lines, edge_lines

    def create_graph(self, node_lines, edge_lines):
        self.connections = dict()
        self.list_stations = set()
        for line in node_lines:
            node, is_station = map(int, line.strip().split(','))
            self.add_node(node)
            if is_station == 1:
                self.add_station(node)

        for line in edge_lines:
            node1, node2, distance = map(int, line.strip().split(','))
            self.add_edge(node1, node2, distance)
            self.add_edge(node2, node1, distance)

    def add_node(self, node):
        self.connections.update({Node(node):{}})

    def add_edge(self, node1, node2, distance):
        self.connections[node1].update({Node(node2): distance})

    def add_station(self, node):
        self.list_stations.add(node)

    def get_neighbours(self, node):
        return self.connections[node]

    def get_nodes(self):
        return self.connections.keys()

    def get_edges(self):
        edges = []
        for node1, neighbours in self.connections.items():
            for node2, distance in neighbours.items():
                edge = (node1, node2, distance)
                edges.append(edge)
        return edges

    def display(self):
        for node, neighbours in self.connections.items():
            print(node, ':', neighbours)
        print('List of stations:', self.list_stations)

    def generate_matix(self):
        m = len(self.connections)
        nodes = list(self.connections.keys())
        arr = [[0 for j in range(m)] for i in range(m)]

        for i, node in enumerate(nodes):
            neighbours = self.connections[node]
            for neighbour, distance in neighbours.items():
                j = nodes.index(neighbour)
                arr[i][j] = distance

        return np.array(arr)

    def plot(self):   
        G = nx.Graph()
        nodes = [node.ID for node in self.connections.keys()]
        G.add_nodes_from(nodes)
        edges = [(node.ID,dest,dist) for node, adj in self.connections.items() for dest, dist in adj.items()]
        G.add_weighted_edges_from(edges)

        options = {
        'node_color': 'yellow',
        'node_size': 300,
        'width': 2,
        'with_labels':True
        }

        plt.subplot(121)
        nx.draw(G, **options)
        plt.show() 

class GraphDessert(Graph):
    def __init__(self, file_name):
        self.connections = {}
        self.parse_file(file_name)

    def parse_file(self, file_name):
        with open(file_name) as file:
            for line in file:
                if line == '\n':
                    break
                else:
                    currentLine = line.split(",")
                    nodeID = int(currentLine[0])
                    name = currentLine[1].strip()
                    self.connections.update({Node(nodeID, name):[]})

            for line in file:
                if line == '\n':
                    break
                else:
                    node1, node2 = map(int, line.strip().split(','))
                    self.connections[node1].append(node2)
                    
    def get_name(self, ID):
        nodes = self.connections.keys()
        for node in nodes:
            if node == ID:
                return node.name
        
        


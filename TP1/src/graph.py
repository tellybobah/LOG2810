"""
@author: Boubacar, Abderahmane, Leandre
"""
from node import Node
from itertools import takewhile

class GraphDrone:
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

    def add_node(self, ID, name=None):
        self.connections.update({Node(ID, name):{}})

    def add_edge(self, node_1, node_2, distance):
        node_2_name = None
        self.connections[node_1].update({Node(node_2, node_2_name): distance})

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
            print(node, ':', *neighbours)
        print('List of stations:', self.list_stations)

class GraphRecette:
    def __init__(self, file_name):
        node_lines, edge_lines = self.parse_file(file_name)
        self.create_graph(node_lines, edge_lines)        

    def add_node(self, node_ID, name):
        self.connections[Node(node_ID, name)] = set()

    def add_edge(self, node_1, node_2):
        node_2_name = self.get_node_name(node_2)
        self.connections[node_1].add(Node(node_2, node_2_name))

    def parse_file(self, file_name):
        with open(file_name) as file:
            node_lines = list(takewhile(lambda x : x != '\n', file))
            edge_lines = list(takewhile(lambda x : x != '\n', file))
            return node_lines, edge_lines

    def create_graph(self, node_lines, edge_lines):
        self.connections = dict()
        self.list_stations = set()

        for line in node_lines:
            current_line = line.strip().split(",")
            node_ID = int(current_line[0])
            name = current_line[1]
            self.add_node(node_ID, name)

        for line in edge_lines:
            node_1, node_2 = map(int, line.strip().split(','))
            self.add_edge(node_1, node_2)
                    
    def get_node_name(self, ID):
        nodes = self.connections.keys()
        for node in nodes:
            if node == ID:
                return node.name
        
    def display(self):
        for node, neighbours in self.connections.items():
            print('({}, {}'.format(node.name, node.ID),end='')
            if len(neighbours) > 0:
                print(' (', end='')
                for neighbour in neighbours:
                    print('({}, {})'.format(neighbour.name, neighbour.ID), end='')
                print('', end='')
            print(')')
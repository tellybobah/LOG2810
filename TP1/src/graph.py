"""
@author: Boubacar, Abderahmane, Leandre
"""
from node import Node
from itertools import takewhile

class GraphDrone:
    """
        This id the constructor function
        It calls parse_file to separate it into two string lists
        Then it creates the graph with those two lists

        file_name - represents the name of the file in the filesystem

    """
    def __init__(self, file_name):
        node_lines, edge_lines = self.parse_file(file_name)
        self.create_graph(node_lines, edge_lines)

    """
        This method take a txt file and divide it in two part , the first part
        is the informations about the node (if it's a station) and the second part
        contains the informations between the connection of the nodes

        file_name - represents the name of the file in the filesystem
    """
    def parse_file(self, file_name):
        with open(file_name) as file:
            node_lines = list(takewhile(lambda x: x != '\n', file))
            edge_lines = list(takewhile(lambda x: x != '\n', file))
            return node_lines, edge_lines


    """
        This method create a graph as a dictionary with nodes as keys and another
        dictionary of neighbours and theirs distances for each nodes

        node_lines - Contains the information about the stations
        edge_lines - contains the information about the connection of the stations
    """
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

    """
        This method adds a node in our dictionary that contains our graph informations
        It leaves it's neighbours empty

        ID - the node ID
        name - the node name | defaults to None
    """
    def add_node(self, ID, name=None):
        self.connections.update({Node(ID, name):{}})

    """
        This method adds an distance between two nodes

        node_1,node_2 - The nodes that we want to change the distance
        distace - the distance we want to set
    """
    def add_edge(self, node_1, node_2, distance):
        node_2_name = None
        self.connections[node_1].update({Node(node_2, node_2_name): distance})

    """
        This method adds a station in our stations set

        node -- is the node we want to add
    """
    def add_station(self, node):
        self.list_stations.add(node)

    """
        This methode return the neighbours of a node
        in dictionary form with nodes as keys and distances as values

        node - the node that we want the neighbours
    """
    def get_neighbours(self, node):
        return self.connections[node]

    """
        This method returns all the node present in the Hashmap
    """
    def get_nodes(self):
        return self.connections.keys()

    """
        This method display the informations of our graph
    """
    def display(self):
        for node, neighbours in self.connections.items():
            print(node, ':', *neighbours)
        print('List of stations:', self.list_stations)

class GraphRecette:
    """
        This id the constructor function
        It calls parse_file to separate it into two string lists
        Then it creates the graph with those two lists

        file_name - represents the name of the file in the filesystem

    """
    def __init__(self, file_name):
        node_lines, edge_lines = self.parse_file(file_name)
        self.create_graph(node_lines, edge_lines)

    """
        This method adds a node in the connections dictionary
        It leaves the neighbours as an empty set
    """
    def add_node(self, node_ID, name):
        self.connections[Node(node_ID, name)] = set()

    """
        This method add an edge between two nodes
    """
    def add_edge(self, node_1, node_2):
        node_2_name = self.get_node_name(node_2)
        self.connections[node_1].add(Node(node_2, node_2_name))

    """
        This method take a txt file and divide it in two part , the first part
        is the informations about the node and the second part contains the
        informations between the connection of the nodes

        file_name - represent the name of the file in the filesystem
    """
    def parse_file(self, file_name):
        with open(file_name) as file:
            node_lines = list(takewhile(lambda x: x != '\n', file))
            edge_lines = list(takewhile(lambda x: x != '\n', file))
            return node_lines, edge_lines

    """
        This method create the graph of "Food" and all the connections
    """
    def create_graph(self, node_lines, edge_lines):
        self.connections = dict()
        for line in node_lines:
            current_line = line.strip().split(",")
            node_ID = int(current_line[0])
            name = current_line[1]
            self.add_node(node_ID, name)

        for line in edge_lines:
            node_1, node_2 = map(int, line.strip().split(','))
            self.add_edge(node_1, node_2)

    """
        This method return a name of a node giving his ID

        ID- is the ID of the node that we want the name
    """
    def get_node_name(self, ID):
        nodes = self.connections.keys()
        for node in nodes:
            if node == ID:
                return node.name
            
    """
        This method print the graph and all the connections.
    """
    def display(self):
        for node, neighbours in self.connections.items():
            print('({}, {}'.format(node.name, node.ID), end='')
            if len(neighbours) > 0:
                print(' (', end='')
                for neighbour in neighbours:
                    print('({}, {})'.format(neighbour.name, neighbour.ID), end='')
                print('', end='')
            print(')')

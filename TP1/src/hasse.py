"""
@author: Boubacar, Abderahmane, Leandre
"""
class Hasse:
    def __init__(self, graph):
        self.graph = graph


    """
        This method find if node 1 and node 2 are connected
        parameters :
            connections -- Hashmap that contains the node as key and it's
            connections as value

            node1,Node2 -- the two nodes which we will determine if they
            are connected
    """
    def is_in_relation(self, node1, node2):
        return node2 in self.graph.connections[node1]


    """
        This method delete the reflexivity in a graph
            connections -- Hashmap that contains the node as key and his
            connection as value

    """
    def remove_relexivity(self):
        for node, neighbours in self.graph.connections.items():
            if self.is_in_relation(node,node):
                #If a node is connected to itself, remove it
                neighbours.remove(node)


    """
        This method delete transitivity
        parameters :
            connections -- Hashmap that contains the node as key and his
            connection as value

    """
    def remove_transitivity(self):
<<<<<<< HEAD
        for node, neighbours in self.graph.connections.items():
            for neighbour in neighbours :
                self.graph.connections[node] = neighbours - self.graph.connections[neighbour]
=======
        connections = self.graph.connections
        for node, common_nodes in connections.items():
            for connected_node in connections[node] :
                #For all the neighbour of our current node remove the common elements
                connection = connections[connected_node]
                common_nodes_temp = set(common_nodes).intersection(connection)
                #Remove the common element of the current node and his neigbour
                connections[node] = list(set(connections[node]) - set(common_nodes_temp))
>>>>>>> 9e3aaf33919084e52a331fb46c21cbbdb83137fc

    """
        This recursive method adds to a pile the node and print the stack when it can't find another connected node
        parameters :
            node -- The current node to look up for other nodes
            parents -- contains the stack of parents
    """
    def print_hasse_rec(self, node, parents):
        neighbours = self.graph.connections[node]
        if len(neighbours) == 0:
            print(*map(lambda x : x.name, parents), sep=' -> ')
            return

        for nodes in neighbours:
            parents.append(nodes)
            self.print_hasse_rec(nodes, parents)
            parents.pop()

    """
        This method calls the recursive function print_hasse_rec to print each branch of Hasse`s diagram
    """
    def print_hasse(self):
        for node in self.graph.connections:
            result = self.find_connected(node)
            if len(result) != 0:
                continue
            parents = [node]
            self.print_hasse_rec(node, parents)

    """
        This method find which nodes are connected a node and
        return a list:

            connections -- Hashmap that contains the node as key and his
            connection as value

            node -- the node that we will find the connections
    """
    def find_connected(self, node):
        return [a_node for a_node, a_neighbours in self.graph.connections.items() if node in a_neighbours]

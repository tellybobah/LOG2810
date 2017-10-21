"""
@author: Boubacar, Abderahmane, Leandre
"""
class Hasse:
    def __init__(self, graph):
        self.graph = graph
    
    def is_in_relation(self, node1, node2):
        """
        This function find if node 1 and node 2 are connected
        parameters :
            connections -- Hashmap that contains the node as key and his 
            connection as value
            
            node1,Node2 -- the two nodes which we will determine if they
            are connected
        """
        return node2 in self.graph.connections[node1]
      
    def remove_relexivity(self):
        """
        This function delete the reflexivity in a graph
            connections -- Hashmap that contains the node as key and his 
            connection as value
            
        """
        for node in self.graph.connections:
            if self.is_in_relation(node,node):
                #If a node is connected to himself then remove it
                self.graph.connections[node].remove(node)
                    
        
    def remove_transitivity(self):
        """
        This function delete transitivity
        parameters :
            connections -- Hashmap that contains the node as key and his 
            connection as value
            
        """
        connections = self.graph.connections
        for node, common_nodes in connections.items():
            common_nodes = connections[node]
            for connected_node in connections[node] : 
                #For all the neighbour of our current node remove the common elements
                connection = connections[connected_node]
                common_nodes = set(common_nodes).intersection(connection)
                #Remove the common element of the current node and his neigbour
                connections[node] = set(connections[node]) - set(common_nodes)
    
    def print_hasse_rec(self, node, parents):
        connections = self.graph.connections
        if len(connections[node]) == 0:
            print(*parents, sep=' -> ')
            return
        
        for nodes in connections[node]:
            parents.append(nodes)
            self.print_hasse_rec(nodes, parents)
            parents.pop()
            
    
    def print_hasse(self):
        connections = self.graph.connections
        for node in connections:
            result = self.find_connected(node)
            if len(result) != 0:
                continue
            parents = [node]
            self.print_hasse_rec(node, parents)
                
                
    def find_connected(self, node):
        """
        This function find which nodes are connected a node and 
        return a list:
            
            connections -- Hashmap that contains the node as key and his 
            connection as value
            
            node -- the node that we will find the connections
        """
        result = []
        connections = self.graph.connections
        for a_node in connections : 
            if node in connections[a_node]:
                #For all the nodes in connections, look if node is connected
                result.append(a_node)
        return result       
        
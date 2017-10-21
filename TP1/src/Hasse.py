"""
@author: Boubacar, Abderahmane, Leandre
"""
class Hasse:
    def __init__(self):
        pass
    
    def is_in_relation(self, connections, node1, node2):
        """
        This function find if node 1 and node 2 are connected
        parameters :
            connections -- Hashmap that contains the node as key and his 
            connection as value
            
            node1,Node2 -- the two nodes which we will determine if they
            are connected
        """
        for connected_node in connections[node1]:
            if connected_node == node2:
                return True
        return False
      
    def remove_relexivity(self, connections):
        """
        This function delete the reflexivity in a graph
            connections -- Hashmap that contains the node as key and his 
            connection as value
            
        """
        for node in connections:
            if self.is_in_relation(connections,node,node):
                #If a node is connected to himself then remove it
                connections[node].remove(node)
                    
        
    def remove_transitivity(self, connections):
        """
        This function delete transitivity
        parameters :
            connections -- Hashmap that contains the node as key and his 
            connection as value
            
        """
        for node in connections:
            common_nodes = connections[node]
            for connected_node in connections[node] : 
                #For all the neighbour of our current node remove the common elements
                connection = connections[connected_node]
                common_nodes = list(set(common_nodes).intersection(connection)) 
                #Remove the common element of the current node and his neigbour
                connections[node] = list(set(connections[node])- set(common_nodes))
    
    def print_hasse_rec(self, graph, connections, node, parents):
        
        if len(connections[node]) == 0:
            for node in parents[:-1]:
                print(graph.get_name(node), end=' -> ')
            print(graph.get_name(parents[-1]))
            return
        
        for nodes in connections[node]:
            parents.append(nodes)
            self.print_hasse_rec(graph, connections, nodes, parents)
            parents.pop()
            
    
    def print_hasse(self, graph, connections):
        for node in connections:
            result = self.find_connected(connections, node)
            if len(result) != 0:
                continue
            parents = [node]
            self.print_hasse_rec(graph, connections, node, parents)
                
                
    def find_connected(self,connections,node):
        """
        This function find which nodes are connected a node and 
        return a list:
            
            connections -- Hashmap that contains the node as key and his 
            connection as value
            
            node -- the node that we will find the connections
        """
        result = []
        for a_node in connections : 
            if node in connections[a_node]:
                #For all the nodes in connections, look if node is connected
                result.append(a_node)
        return result       
        
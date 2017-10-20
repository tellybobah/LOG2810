"""
@author: Boubacar, Abderahmane, Leandre
"""
class Hasse:
    def __init__(self):
        pass
    
    def is_in_relation(self, connections, node1, node2):
          for connectedNode in connections[node1]:
                if connectedNode == node2:
                    return True
          return False
      
    def remove_relexivity(self, connections):
        for node in connections:
            if self.is_in_relation(connections,node,node):
                connections[node].remove(node)
                    
        
    def remove_transitivity(self, connections):
        for node in connections:
            #print(connections[node])
            commonNodes = connections[node]
            for connectedNode in connections[node] : 
                connection = self.get_connected_node(connections,connectedNode)
                commonNodes = list(set(commonNodes).intersection(connection)) #prendre les elements en commun
                connections[node] = list(set(connections[node])- set(commonNodes))
            print("connection",connections[node])
    
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
        result = []
        for aNode in connections : 
            if node in connections[aNode]:
                result.append(aNode)
        return result       
        
    def get_connected_node(self,connections,node):
        return connections[node]
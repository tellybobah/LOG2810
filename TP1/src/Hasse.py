"""
@author: Boubacar, Abderahmane, Leandre
"""
class Hasse:
    def __init__(self):
        pass
    
    def is_in_relation(self,connections,node1,node2):
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
                connection = self.getConnectedNode(connections,connectedNode)
                commonNodes = list(set(commonNodes).intersection(connection)) #prendre les elements en commun
                connections[node] = list(set(connections[node])- set(commonNodes))
            print("connection",connections[node])
    
    def printHasse_rec(self,connections, node, parent_node):
        
    
    def printHasse(self, connections):
        list_temp = []
        for node in connections:
            if len(connections[node]) == 0:
                self.printHasse_rec(connections,node,parent_node)
                
                
    def find_connections(self,connections,node):
        result = []
        for aNode in connections : 
            if node in connections[aNode]:
                result.append(aNode)
        return result        
        
    def getConnectedNode(self,connections,node):
        return connections[node]
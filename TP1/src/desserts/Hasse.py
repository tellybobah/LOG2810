class Hasse:
    def __init__(self):
        pass
    
    def isInRelation(self,connections,node1,node2):
          for connectedNode in connections[node1]:
                if connectedNode == node2:
                    return True
          return False
      
    def removeRelexivity(self, connections):
        for node in connections:
            if (self.isInRelation(connections,node,node)):
                connections[nodes].remove(connectedNode)
                    
            
    def removeTransitivity(self, connections):
        for node in connections:
            for connectedNode in connections[node]:
                for ()
    
    def printHasse(self, connections):
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
            
                    
        
    def removeTransitivity(self, connections):
        for node in connections:
            commonNodes = connection[node]
            for connectedNode in connection[node] : 
                connection = getConnectedNode(connections,connectedNode)
                commonNodes = list(set(connectedNodes).intersection(connection)) #prendre les elements en commun
                
    
    def printHasse(self, connections):
        
    def findCommonElements(self,list1,list2):
        
    def getConnectedNode(self,connections,node):
        return connections[node]
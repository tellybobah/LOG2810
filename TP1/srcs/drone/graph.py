# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:12:43 2017

@author: Boubacar
"""
from summit import Summit
from arc import Arc

class Graph:
    #connexionMatrice = [[Arc() for j in range(18)] for i in range(18)]
    
    def __init__(self,txtname):
         
         self.connexionMatrice = [[Arc(-1) for j in range(20)] for i in range(20)] #create a 20 by 20 matrice of arcs
         self.listOfSummit = [None] * 20 #create a list with 20 empty case
         self.createGraph(txtname)
         
    def createGraph(self,txtname): 
         #create the summits and connexionMatrice
         f= open(txtname)
         with open(txtname, "r") as filestream:
             for line in filestream:
                 if(line== '\n'):
                     break
                 else:
                     currentline = line.split(",")
                     id = int(int(currentline[0]))
                     isStation = bool(currentline[1])
                     self.listOfSummit[id]= (Summit(id,isStation,"" )) 
             for line in filestream:
                 if(line== '\n'):
                     break
                 else:
                     currentline = line.split(",")
                     summit1 = int(currentline[0])
                     summit2 = int(currentline[1])
                     time = int(currentline[2])
                     self.connexionMatrice[summit1][summit2]= time      
                 
         f.close()
           # connexionMatrice[0][j] = Summit(id,isStation,"") 
        
    def display(self):
        
    
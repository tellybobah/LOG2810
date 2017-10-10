# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:10:10 2017

@author: Boubacar
"""
class Node(object) : 
    def __init__(self,ID,name):
        self.ID = ID
        self.name = name
        
    def getID(self):
        return self.ID

    def getNAme(self):
        return self.name

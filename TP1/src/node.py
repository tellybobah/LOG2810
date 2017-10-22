# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:10:10 2017

@author: Boubacar
"""
class Node() : 
    def __init__(self,ID,name=''):
        self.ID = ID
        self.name = name

    def getID(self):
        return self.ID

    def getName(self):
        return self.name

    def __str__(self):
        if self.name is None:
            return str(self.ID)
        else:
            return '\'{}\'-{}'.format(self.name, self.ID)

    def __hash__(self):
        return hash(self.ID)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.ID == other.ID
        elif isinstance(other, int):
            return self.ID == other
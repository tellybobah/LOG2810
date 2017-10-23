# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:10:10 2017

@author: Boubacar
"""
class Node() : 
    def __init__(self,ID,name=''):
        self.ID = ID
        self.name = name
        """
        This function return the ID
        """
    def getID(self):
        return self.ID
<<<<<<< Updated upstream

    def getName(self):
=======
    """
    this function return the name of a NODE
    """
    def getNAme(self):
>>>>>>> Stashed changes
        return self.name
    """
    This function 
    """
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
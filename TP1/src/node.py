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
    def get_ID(self):
        return self.ID

    """
        This function return the name of a NODE
    """
    def get_name(self):
        return self.name

    """
        This function gives a string representation of the node
    """
    def __str__(self):
        if self.name is None:
            return str(self.ID)
        else:
            return '\'{}\'-{}'.format(self.name, self.ID)

    """
        This method redefines the hash function of the node
        When a node is placed in a dictionary, it's hash is computed using only the ID
        This gives us the ability to find a node in a dictionary by only using its ID
    """
    def __hash__(self):
        return hash(self.ID)

    """
        This method redefines the hash function of the node 
        When who nodes are compared, they compare their IDs
        This gives us the ability to find a node in a dictionary by only using its ID
    """
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.ID == other.ID
        elif isinstance(other, int):
            return self.ID == other
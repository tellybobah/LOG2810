# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:10:10 2017

@author: Boubacar
"""
class Summit(object) : 
    neighbourd = []
    def __init__(self,id,isStation,name):
        self.id = id
        self.isStation = isStation
        self.name = name
        
    def isASsation(self):
        return self.isStation
    
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:16:37 2017

@author: Boubacar
"""
from enum import Enum
class Package(Enum):
      LIGHT = 0
      MEDIUM = 1
      HEAVY = 2
        
class Drone(object):   
    def __init__(self,package):
        self.energy = 100
        self.package = package
        
    def getEnergy (self):
        return self.energy
    
    def getPackage(self):
        return self.package
    
    def reduceEnergy(self):
        return 
    
    def setEnergy(self,newEnergy):
        self.energy = newEnergy

    
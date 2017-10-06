# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:16:37 2017

@author: Boubacar
"""
from enum import Enum
class PACKAGE(Enum):
      LIGHT = 0
      MEDIUM = 1
      HEAVY = 2
        
class Drone(object):
    energy = 0.0
   
    def __init__(self,energy,package):
        self.energy = energy
        self.package = package
        
    def getEnery (self):
        return self.energy
    
    def getPackage(self):
        return self.package
    
    def reduceEnergy(self):
        return 
    def setEnergy(self,newEnergy):
        self.energy = newEnergy
        
    def setPackage(self):
        return 
    
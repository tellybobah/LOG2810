# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:16:37 2017

@author: Boubacar
"""

def testxksk():
    print("dkosdkow")
    
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
    
    def setEnergy(self,newEnergy):
        self.energy = newEnergy

class Drone3Amp(Drone):
    def __init__(self,package):
        super(Drone3Amp,self).__init__(package)
        
    def reduceEnergy(self, time):
        self.energy = self.predictEnergy(time)

    def predictEnergy(self, time):
        delta = 0
        if self.package == Package.LIGHT:
            delta = 1
        elif self.package == Package.MEDIUM:
            delta = 2
        elif self.package == Package.HEAVY:
            delta = 4

        return self.energy - (time * delta)
    
class Drone5Amp(Drone):
    def __init__(self,package):
        super(Drone5Amp, self).__init__(package)
        
    def reduceEnergy(self, time):
        self.energy = self.predictEnergy(time)

    def predictEnergy(self, time):
        delta = 0
        if self.package == Package.LIGHT:
            delta = 1
        elif self.package == Package.MEDIUM:
            delta = 1.5
        elif self.package == Package.HEAVY:
            delta = 2.5

        return self.energy - (time * delta)
    
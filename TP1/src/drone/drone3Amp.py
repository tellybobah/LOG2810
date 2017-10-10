# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:29:20 2017

@author: Boubacar
"""
from drone import Drone, Package


class Drone3Amp(Drone):

    def _init_(self):
        pass

    def reduceEnergy(self, time):
        delta = 0
        if self.package == Package.LIGHT:
            delta = 1
        elif self.package == Package.MEDIUM:
            delta = 2
        elif self.package == Package.HEAVY:
            delta = 4

        self.energy -= time * delta

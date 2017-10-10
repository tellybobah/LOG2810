# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:26:35 2017

@author: Boubacar
"""
from drone import Drone, Package


class Drone5Amp(Drone):

    def reduceEnergy(self, time):
        delta = 0
        if self.package == Package.LIGHT:
            delta = 1
        elif self.package == Package.MEDIUM:
            delta = 1.5
        elif self.package == Package.HEAVY:
            delta = 2.5

        self.energy -= time * delta

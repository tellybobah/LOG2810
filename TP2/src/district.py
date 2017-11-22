"""
@author: Boubacar, Abderahmane, Leandre
"""
import queue
from package import Package
class District : 
    
    def __init__(self, value):
        self.packages = queue.Queue()
        self.last_visit_counter = 0 
        self.value = value

    def add_package(self, weight, destination):
        self.packages.put(Package(weight,destination))
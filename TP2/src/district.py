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

    def get_last_visit_counter(self):
        return self.last_visit_counter

    def calculate_score(self):
        return 0.6*len(self.packages) + 0.4* self.last_visit_counter

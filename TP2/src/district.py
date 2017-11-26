"""
@author: Boubacar, Abderahmane, Leandre
"""
import queue
from package import Package
from collections import deque

class District : 
    
    def __init__(self, value=""):
        self.packages = deque()
        self.last_visit_counter = 0 
        self.value = value
        self.name = ""

    def add_package(self, weight, destination):
        self.packages.append(Package(weight,destination))

    def get_last_visit_counter(self):
        return self.last_visit_counter
    
    def visit(self):
        self.last_visit_counter = 0

    def calculate_score(self):
        return 0.6*len(self.packages) + 0.4* self.last_visit_counter

    def __str__(self):
        return "District : " + self.name

    def __lt__(self, other):
        return self.calculate_score() > other.calculate_score()
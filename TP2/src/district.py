"""
@author: Boubacar, Abderahmane, Leandre
"""
from multiprocessing import Queue
from package import Package
class District : 
    
    def __init__(self):
        self.package = Queue()
        self.last_visit_counter = 0 

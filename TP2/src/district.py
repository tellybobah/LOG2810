"""
@author: Boubacar, Abderahmane, Leandre
"""
from multiprocessing import Queue
from automat import Automat
class District : 
    
    def __init__(self,package, drones):
        self.package = Queue()
        self.automat = Automat()
    
    def equilibrate_swarm(self):
        pass
    
    def assign_packages(self):
        pass
    
    def parse_request(self,file_number):
        pass
    
    def print_statistics(self):
        pass

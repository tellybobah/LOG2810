"""
@author: Boubacar, Abderahmane, Leandre
"""

import queue
import os.path
from automat import Automat
class Delevery : 
    
    def __init__(self):
        self.drones = []
        self.automat = Automat()
        self.treated_query = 0
        self.invalid_query =0
        self.adresses = queue.PriorityQueue()
    
    def equilibrate_swarm(self):
        pass
    
    def assign_packages(self):
        pass
    
    def parse_request(self,file_name):
        if os.path.exists("../adress/" + file_name):
            self.automat.create_state_adress(file_name)
            return True
        return False
    
    def print_statistics(self):
        pass

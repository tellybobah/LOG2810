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
        """
        add_packages :
            :param weight: 
            :param destination: 
        """   
        self.packages.append(Package(weight,destination))

    def get_last_visit_counter(self):
        """
        get_last_visit_counter
             
        """  
        return self.last_visit_counter
    
    def visit(self):
        """
        visit : methode qui remet last_visit_counter a zero
        """  
        self.last_visit_counter = 0

    def calculate_score(self):
        """
        calculate_score : methode qui calcule la cote d'un district pour 
        la file de priorite
        """  
        return 0.6*len(self.packages) + 0.4* self.last_visit_counter

    def __str__(self):
        """
        __str__ : surcharge de l'operateur to string pour print      
        """  
        return "District : " + self.name

    def __lt__(self, other):
        """
        __lt__ : Definition de l'operateur > pour la file de priorite
        """  
        return self.calculate_score() > other.calculate_score()
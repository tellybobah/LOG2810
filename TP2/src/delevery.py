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
        self.invalid_query = 0
        self.drone_light_delevery_query = 0
        self.drone_heavy_delevery_query = 0
        self.remaining_adresses_w_packages = queue.PriorityQueue()
    
    def equilibrate_swarm(self):
        pass
    
    def assign_package_to_district(self, from_adress, to_adress, mass):
        adress1 = self.automat.get_adress(from_adress)
        adress2 = self.automat.get_adress(to_adress)
        weight = int(mass)
        if (not adress1 == None and not adress2 == None) and (weight > 0 and weight <= 5000):
            adress1.add_package(weight, adress2)
        else:
           self.invalid_query += 1 
    
    def create_automat(self, file_name):
        file_path = "../adress/" + file_name
        if os.path.exists(file_path):
            self.automat.create_state_adress(file_path)
            return True
        return False

    def parse_request(self,file_name):
        file_path = "../request/" + file_name
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                while(True):
                    line = f.readline().strip('\n').strip(' ').strip('\r').split()
                    if not line:
                        break
                    if not len(line[0]) == 6 or not len(line[1]) == 6:
                        self.invalid_query += 1
                        continue
                    self.assign_package_to_district(line[0], line[1], line[2])
        else:
            return False
        return True
    
    def print_statistics(self):
        print('Requetes Traitees :',self.treated_query)
        print('Requete Invalides :',self.invalid_query)

        # TODO: Ajouter une liste de cartier avec le nombre de drones repartis

        print('Nombre Moyen de Colis par Drone :')
        print('Faible Capacite: ', self.drone_light_delevery_query/10)
        print('Forte Capacite: ' , self.drone_heavy_delevery_query/5)
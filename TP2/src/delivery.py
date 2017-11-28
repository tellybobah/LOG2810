"""
@author: Boubacar, Abderahmane, Leandre
"""

import queue
import os.path
from automaton import Automaton
from drone import *
from collections import deque

class Delivery : 

    def __init__(self):
        self.drones = []
        self.automaton = Automaton()
        self.treated_query = 0
        self.invalid_query = 0
        self.drone_light_delivery_query = 0
        self.drone_heavy_delivery_query = 0
        self.priority_district = queue.PriorityQueue()
        self.initialisation()

    def initialisation(self):
        """
        initialisation : initialise la file de priorite en ordre inverse
        """

        for i in range(10):
            self.drones.append(Drone(1000))

        for i in range(5):
            self.drones.append(Drone(5000))

    def deliver_packages(self):
        """
        deliver_packages
        """  
        self.assign_packages_to_drones()
        self.assign_packages_to_drones() # Assure que les drones 1KG sont bien utilises si le premier colis est plus lourd
        for drone in self.drones : 
            if len(drone.get_packages())!=0:
                drone.set_position(drone.get_packages()[0].get_destination())
                self.treated_query+=1
                drone.packages = drone.packages[:-1]
                if drone.get_max_weight() == 1000:
                    self.drone_light_delivery_query +=1
                else:
                    self.drone_heavy_delivery_query+=1

        for district in self.automaton.get_all_districts():
            if self.count_drones_by_cat_district(district, 1000) == 0 and self.count_drones_by_cat_district(district, 5000) == 0:
                district.last_visit_counter += 1

    def equilibrate_swarm(self):
        """
        equilibrate_swarm
             
        """  
        for drone in self.drones:
            if len(drone.packages) != 0:
                continue

            temp_useless_district = []
            while True:
                first_elem = self.priority_district.get_nowait()
                if len(first_elem.packages) != 0:
                    if drone.max_weight >= first_elem.packages[0].get_weight():
                        drone.set_position(first_elem)
                        first_elem.visit()
                        self.priority_district.put(first_elem)
                        break
                    else:
                        temp_useless_district.append(first_elem)
                else:
                    drone.set_position(first_elem)
                    self.priority_district.put(first_elem)
                    break
                
            for item in temp_useless_district:         
                self.priority_district.put(item)
    

    def assign_packages_to_drones(self):
        """
        assign_packages_to_drones
             
        """  
        counter = 0
        for drone in self.drones :
            if len(drone.get_packages()) == 0:
                district = drone.get_current_position()
                if len(district.packages) > 0:
                    first_package = district.packages.popleft()
                    counter+=1
                    if drone.get_max_weight() >= first_package.get_weight():
                        drone.add_package(first_package)
                    else:
                        district.packages.appendleft(first_package)
                        continue

                    remaining_weight_to_fill = drone.get_max_weight()-first_package.get_weight()

                    to_remove = []
                    for item in district.packages:
                        if item.get_destination() == first_package.get_destination():
                            if(remaining_weight_to_fill >= item.get_weight()):
                                remaining_weight_to_fill -= item.get_weight()
                                drone.add_package(item)
                                to_remove.append(item)

                    for item in to_remove:
                        district.packages.remove(item)



    def assign_package_to_district(self, from_adress, to_adress, mass):
        adress1 = self.automaton.get_adress(from_adress)
        adress2 = self.automaton.get_adress(to_adress)
        weight = int(mass)
        if (not adress1 == None and not adress2 == None) and (weight > 0 and weight <= 5000):
            adress1.add_package(weight, adress2)
        else:
           self.invalid_query += 1 
    
    def create_automaton(self, file_name):
        """
        create_automaton:

            :param file_name: 
        """   
        file_path = "../adress/" + file_name
        if os.path.exists(file_path):
            self.automaton.create_state_adress(file_path)

            for district in self.automaton.get_all_districts() :
                self.priority_district.put(district)

            return True
        return False

    def parse_request(self,file_name):
        """
        parse_request 
            :param file_name: 
        """   

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
        """
        deliver_packages
             
        """  

        print('\n')
        print("-------------------------")
        print('Requetes Traitees :',self.treated_query)
        print('Requete Invalides :',self.invalid_query)
        print("-------------------------")
        # TODO: Ajouter une liste de cartier avec le nombre de drones repartis
        print("Repartition de la flotte")
        print("Quartier | Drones faible capacite | Drones forte capacite")
        for district in self.automaton.get_all_districts():
            print(district.name, " | ",self.count_drones_by_cat_district(district, 1000), "\t\t\t  | ", self.count_drones_by_cat_district(district, 5000))

        print('Nombre Moyen de Colis par Drone :')
        print('Faible Capacite: ', self.drone_light_delivery_query/10)
        print('Forte Capacite: ' , self.drone_heavy_delivery_query/5)
        print("-------------------------")
        print('\n')

    def count_drones_by_cat_district(self, district, max_weight):
        counter = 0
        for drone in self.drones:
            if drone.get_current_position() == district and drone.get_max_weight() == max_weight:
                counter += 1
        return counter
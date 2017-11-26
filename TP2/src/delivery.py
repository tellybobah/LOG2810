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
        for drone in self.drones : 
            if len(drone.get_packages())!=0:
                drone.packages = drone.packages[:-1]
                if drone.get_max_weight() == 1000:
                    self.drone_light_delivery_query +=1
                else:
                    self.drone_heavy_delivery_query+=1

        self.assign_packages_to_drones()

    def equilibrate_swarm(self):
        for drone in self.drones:
            if len(drone.packages) != 0:
                continue

            temp_useless_district = []
            while True:
                first_elem = self.priority_district.get_nowait()
                #print(first_elem)
                if len(first_elem.packages) != 0:
                    #print("Debug", *first_elem.packages, sep='\n')
                    if drone.max_weight >= first_elem.packages[0].get_weight():
                        #print('A', first_elem)
                        drone.set_position(first_elem)
                        first_elem.visit()
                        self.priority_district.put(first_elem)
                        break
                    else:
                        #print('C')
                        temp_useless_district.append(first_elem)
                else:
                    #print('I')
                    #print(first_elem)
                    drone.set_position(first_elem)
                    self.priority_district.put(first_elem)
                    break
                
            for item in temp_useless_district:
                #print('G')           
                self.priority_district.put(item)
    

    def assign_packages_to_drones(self):
        #TODO appeler deux fois
        counter = 0
        for drone in self.drones :
            if len(drone.get_packages()) == 0:
                district = drone.get_current_position()
                #print(district, "Package : ",len(district.packages))
                if len(district.packages) > 0:

                    print("counter",counter)
                    first_package = district.packages.popleft()
                    print(first_package)
                    counter+=1
                    if drone.get_max_weight() >= first_package.get_weight():
                        drone.add_package(first_package)
                    else:
                        first_package.appendleft(first_package)
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
        file_path = "../adress/" + file_name
        if os.path.exists(file_path):
            self.automaton.create_state_adress(file_path)

            for district in self.automaton.get_all_districts() :
                self.priority_district.put(district)

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
        print('\n')
        print("-------------------------")
        print('Requetes Traitees :',self.treated_query)
        print('Requete Invalides :',self.invalid_query)
        print("-------------------------")
        # TODO: Ajouter une liste de cartier avec le nombre de drones repartis
        print("Repartition de la flotte")

        print('Nombre Moyen de Colis par Drone :')
        print('Faible Capacite: ', self.drone_light_delivery_query/10)
        print('Forte Capacite: ' , self.drone_heavy_delivery_query/5)
        print("-------------------------")
        print('\n')
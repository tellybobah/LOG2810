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
        initialisation : methode qui fait la creation de 15 drones, soit 10 de 1000g et 5 de 5000g
        """
        #Creation des drones de faible capacite
        for i in range(10):
            self.drones.append(Drone(1000))
        #Creation des drone de fortes capacite
        for i in range(5):
            self.drones.append(Drone(5000))

    def deliver_packages(self):
        """
        deliver_packages : methode qui fait la distribution de colis en assignant les colis aux drones
        """  
        self.assign_packages_to_drones()
        self.assign_packages_to_drones() # Assure que les drones 1KG sont bien utilises si le premier colis est plus lourd

        #Deposer les colis des drone pour cycle en cours
        for drone in self.drones : 
            if len(drone.get_packages())!=0:
                drone.set_position(drone.get_packages()[0].get_destination())
                self.treated_query+=1
                drone.packages = drone.packages[:-1]
                if drone.get_max_weight() == 1000:
                    self.drone_light_delivery_query +=1
                else:
                    self.drone_heavy_delivery_query+=1
        #Mise a jours des valeurs pour la fonction print_statistic
        for district in self.automaton.get_all_districts():
            if self.count_drones_by_cat_district(district, 1000) == 0 and self.count_drones_by_cat_district(district, 5000) == 0:
                district.last_visit_counter += 1
            else:
                district.visit()

    def equilibrate_swarm(self):
        """
        equilibrate_swarm : methode qui permet de reequilibrer la distribution des drones sur les adresses
                            disponibles en prenant en compte la cote de priorite de ces adresses             
        """  
        for drone in self.drones:
            if len(drone.get_packages()) != 0:
                continue

            temp_useless_district = []
            #Tant que le drone n'est pas assigne a un quartier 
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
        assign_packages_to_drones : methode qui permet d'assigner des colis aux drones
             
        """  
        counter = 0
        for drone in self.drones :
            if len(drone.get_packages()) == 0: # Verifie si le drone n'a pas deja des colis
                district = drone.get_current_position()
                if len(district.packages) > 0: # Verifie si l'endroit ou il est possede des colis
                    first_package = district.packages.popleft()
                    counter+=1
                    if drone.get_max_weight() >= first_package.get_weight(): # Verifie si le drone peut supporter le colis
                        drone.add_package(first_package)
                    else:
                        district.packages.appendleft(first_package)
                        continue

                    remaining_weight_to_fill = drone.get_max_weight()-first_package.get_weight()

                    to_remove = []
                    
                    for item in district.packages: # Regarde pour les autres colis ayant la meme destination et un poids acceptable pour le drone
                        if item.get_destination() == first_package.get_destination():
                            if(remaining_weight_to_fill >= item.get_weight()):
                                remaining_weight_to_fill -= item.get_weight()
                                drone.add_package(item)
                                to_remove.append(item)

                    for item in to_remove:
                        district.packages.remove(item)



    def assign_package_to_district(self, from_adress, to_adress, mass):
        """
        assign_package_to_district: Methode qui permet d'assigner des colis a un adress

            :param from_adress: l'adresse a ajouter le colis
            :param to_adress: l'adresse de destination du colis
            :param mass: le poids du colis
        """  
        adress1 = self.automaton.get_adress(from_adress)
        adress2 = self.automaton.get_adress(to_adress)
        weight = int(mass)
        if (not adress1 == None and not adress2 == None) and (weight > 0 and weight <= 5000):
            adress1.add_package(weight, adress2)
        else:
           self.invalid_query += 1 
    
    def create_automaton(self, file_name):
        """
        create_automaton: Permet de verifier l'existance du fichier et d'appeler la methode d'automaton pour creer l'arbre

            :param file_name: le nom du fichier a lequel on veut generer l'automate
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
        parse_request : permet de lire un fichier de requetes tout en validant l'existance des adresses d'origine et de destionation
            et en assignant les packets valides aux bons districts
            :param file_name: le nom du fichier de requete
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
        print_statistics : methode qui permet d'afficher les statistiques de la livraison des drones ainsi que la
                        disposition des drones dans les differents districts
             
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
        """
        count_drones_by_cat_district : Compte le nombre de drones par catégorie aux district
            :param district: District dont on veut connaitre le nombre de drone
            :param max_weight: categorie de drone dont on veut connaitre le nombre
        """   
        counter = 0
        for drone in self.drones:
            if drone.get_current_position() == district and drone.get_max_weight() == max_weight:
                counter += 1
        return counter
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:36:08 2017

@author: Boubacar,Leandre,Abder
"""
from state import State
from district import District

class Automaton : 
    
 
    def __init__(self):
        self.initial_state = State()
        self.districts_list = []
    
    def create_state_adress(self,file):
        """
        create_state_adress : methode qui va lire le fichier contenant 
        les adresses et va creer un automate
            :param self: 
            :param file: nom du fichier qui va contenir les adresses
        """   
        current_node = self.initial_state
        #Lire le fichier
        with open(file, "r") as f:
            while(True):
                line = f.readline().strip('\n').strip(' ').strip('\r')
                if not line:
                    break
                if not len(line) == 6:
                    continue

                if not (line[0].isupper() and line[2].isupper() and line[4].isupper()):
                    continue
                if not (line[1].isdigit() and line[3].isdigit() and line[5].isdigit()):
                    continue
                
                current_node = self.initial_state
                counter = 0
                #
                while not counter == 6:
                    node = line[counter]
                    found_node = False
                    for state in current_node.next_states:
                        if state.value == node :
                            current_node = state
                            found_node = True
                    #Si il n'est pas deja dans les fils
                    if  not found_node :
                        inserted_state = None
                        if counter == 5:
                            inserted_state = District(node)
                            self.districts_list.append(inserted_state)
                        else:
                            inserted_state = State(node)
                        current_node.add_state(inserted_state)
                        inserted_state.name = current_node.name + node
                        if counter == 2:
                            inserted_state.name += " "
                        current_node = inserted_state
                    counter = counter + 1

    def verify_adress(self, adress):
        """
        verify_adress : verifie qu'une adresse est bien valide selon l'automate
            :param self: 
            :param adress: adresses qui va etre verifiee
        """   
        counter = 0
        current_node = self.initial_state
        while  counter != 6:
            node = adress[counter]
            found_next_state = False
            for state in current_node.next_states:
                if state.value == node :
                    current_node = state
                    found_next_state = True

            if not found_next_state:
                return False
            
            counter = counter + 1
        return True

    def get_adress(self, adress):
        """
        get_adress : retourne le noeud final de l'adresse passee en parametre si elle existe
            :param self: 
            :param adress: adresse qui va etre verifee
        """   
        counter = 0
        current_node = self.initial_state

        #Verifie que la taille est bien valide
        while  counter != 6:
            node = adress[counter]
            found_next_state = False
            
            #Chercher dans la liste de fils
            for state in current_node.next_states:
                if state.value == node :
                    current_node = state
                    found_next_state = True

            if not found_next_state:
                return None
            
            counter = counter + 1
        return current_node

    def get_all_districts(self):
        """
        get_all_districs : methode qui permet de retourner une liste de pointeurs d'adresse de destination
            :param self: 
        """   
        return self.districts_list
        
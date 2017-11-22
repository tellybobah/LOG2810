# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:36:08 2017

@author: Boubacar
"""
from state import State
class Automat : 
    
    def __init__(self):
        self.initial_State = State()
    
    def create_state_adress(self,file):
        current_node = self.initial_State
        with open(file, "r") as f:
            while(True):
                line = f.readline().strip('\n').strip(' ').strip('\r')
                if not line:
                    break
                if not len(line) == 6:
                    continue 
                counter = 0
                while not counter == 6:
                    node = line[counter]
                    found_node = False

                    for state in current_node.next_states:
                        if state.value == node :
                            current_node = state
                            found_node = True

                    if  not found_node : 
                        inserted_state = State(node)
                        current_node.next_states.append(inserted_state)
                        current_node = inserted_state
                    counter = counter + 1

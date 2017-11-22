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
        with open (file) as f :
            while(True):
                node = f.read(1)
                if node == '\n':
                    current_node = self.initial_State
                if not node :
                    break
                found = False
                for state in current_node.next_states:
                    if state.value == node :
                        current_node = state
                        found = True
                if  not found : 
                    inserted_state = State(node)
                    current_node.next_states.append(inserted_state)
                    current_node = inserted_state 

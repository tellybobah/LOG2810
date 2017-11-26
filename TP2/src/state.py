# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:36:14 2017

@author: Boubacar,Leandre,Adber
"""
class State : 
    
    def  __init__(self,value=''):
        self.next_states = []
        self.value = value
        self.name = ""

    def add_state(self,state):
        self.next_states.append(state)
       
        

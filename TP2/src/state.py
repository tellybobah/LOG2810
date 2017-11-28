# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:36:14 2017

@author: Boubacar,Leandre,Adber
"""
class State : 
    
    def  __init__(self,value=''):
        """
        __init__ : contructeur de la classe State
            :param value='': Valeur par defaut du state
        """   
        self.next_states = []
        self.value = value
        self.name = ""

    def add_state(self,state):
        """
        add_state : methode qui ajoute un etat a next_states
            :param state: State a ajouter dans sa liste de prochain state
        """   
        self.next_states.append(state)
       
        

"""
@author: Boubacar, Abderahmane, Leandre
"""

class Package : 

    def __init__(self,weight,destination):
        """
        __init__ : contructeur de la classe package
            :param weight: Poids du colis
            :param destination: Adresse de destination
        """   
        self.weight = weight
        self.destination = destination
    
    def get_weight(self):
        """
        get_weight : Methode qui permet de retourner le poids du colis
            :param self: 
        """   
        return self.weight

    def get_destination(self):
        """
        get_destination : Methode qui permet de retourner la destination du colis
        """
        return self.destination

    def __str__(self):
        """
        __str__ : surcharge de l'operateur string afin d'afficher la classe
        """
        return "Weight : " + str(self.weight) + " Destination :" + str(self.destination)
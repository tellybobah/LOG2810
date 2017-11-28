class Package : 

    def __init__(self,weight,destination):
        """
        __init__ : contructeur de la classe package
            :param weight: 
            :param destination: 
        """   
        self.weight = weight
        self.destination = destination
    
    def get_weight(self):
        """
        get_weight
            :param self: 
        """   
        return self.weight

    def get_destination(self):
        """
        deliver_packages
        """
        return self.destination

    def __str__(self):
        """
        __str__ : surcharge de l'operateur string afin d'afficher la classe
        """
        return "Weight : " + str(self.weight) + " Destination :" + str(self.destination)
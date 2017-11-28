from district import District
class Drone : 

    def __init__(self,max_weight):
        """
        __init__ : Constructeur de la classe drone
            :param max_weight: Poids maximal que le drone peut transporter
        """   
        self.curent_position = District()
        self.max_weight = max_weight
        self.packages = []
        
    def get_current_position(self):
        """
        deliver_packages : methode qui retourne l'attribut current_position
        """  
        return self.curent_position

    def get_max_weight(self):
        """
        get_max_weight : methode qui retourne l'attribut max_weight
        """
        return self.max_weight

    def get_packages(self):
        """
        get_packages : methode qui retourne l'attribut packages
        """
        return self.packages
    
    def set_position(self,position):
        """
        set_position : methode qui modifie la valeur de l'attribut current_position
            :param position: la position a laquelle nous voulons mettre le drone
        """   
        self.curent_position = position

    def add_package(self,package):
        """
        add_package: Methode qui permet d'ajouter un colis au drone
            :param package: Le colie a ajouter
        """   
        self.packages.append(package)

    def pop_package(self):
        """
        deliver_packages : methode qui retire un element de la liste de package
        """
        self.packages.pop()

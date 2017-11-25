from district import District
class Drone : 

    def __init__(self,max_weight):
        self.curent_position = District()
        self.max_weight = max_weight
        self.packages = []
        
    def get_current_position(self):
        return self.curent_position

    def get_max_weight(self):
        return self.max_weight

    def get_packages(self):
        return self.packages
    
    def set_position(self,position):
        self.position = position

    def add_package(self,package):
        self.packages.append(package)

    def pop_package(self):
        self.packages.pop()

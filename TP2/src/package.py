class Package : 

    def __init__(self,weight,destination):
        self.weight = weight
        self.destination = destination
    
    def get_weight(self):
        return self.weight

    def get_destination(self):
        return self.destination

    def __str__(self):
        return "Weight : " + str(self.weight) + " Destination :" + str(self.destination)
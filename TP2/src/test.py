from district import District
from delivery import Delivery
from drone import *
from queue import PriorityQueue


import queue

delivery = Delivery()
delivery.create_automaton("CodesPostaux.txt")

# q = queue.PriorityQueue()
# for item in delivery.automaton.get_all_districts():
#     q._put(item)
# while  not q.empty() : 
#     print(q.get())

delivery.parse_request("requetesTest.txt")
delivery.equilibrate_swarm()

# print(delivery.automaton.verify_adress('H1W1B2'))
# print(delivery.automaton.verify_adress('H4N2Y8')) 
district = delivery.automaton.get_adress('H1W1B2')

print("Number of pack: ", len(district.packages))

#delivery.drones[0].curent_position = district

#print(delivery.drones[0].curent_position)

delivery.assign_packages_to_drones()

for drone in delivery.drones:
    print("Pos: ", drone.curent_position, drone.packages)

# print(delivery.drones[14].get_current_position())
# print(delivery.drones[14].packages)
# for item in delivery.drones[14].get_packages():
#     print("Le poid ",item.get_weight(),"Ls destination",item.get_destination())

print("Number of pack: ", len(district.packages))
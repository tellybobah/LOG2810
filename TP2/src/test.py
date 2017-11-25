from district import District
from delivery import Delivery
from drone import *

import queue

delivery = Delivery()
delivery.create_automaton("CodesPostaux.txt")
delivery.parse_request("requetesTest.txt")

# print(delivery.automaton.verify_adress('H1W1B2'))
# print(delivery.automaton.verify_adress('H4N2Y8')) 
district = delivery.automaton.get_adress('H1W1B2')

print("Number of pack: ", district.packages.qsize())

# while not district.packages.empty():
#     print(district.packages.get().get_weight())

delivery.drones[0].curent_position = district

print(delivery.drones[0].curent_position)

delivery.assign_packages_to_drones()

print(delivery.drones[0].packages)

print("Number of pack: ", district.packages.qsize())

# automaton = Automat()
# automaton.create_state_adress("testAutomat.txt")

# for state in automaton.initial_state.next_states:
#     print(state.value)

# print(automaton.verify_adress('H3W1W6'))
# print(automaton.verify_adress('H3W1W7'))
# print(automaton.verify_adress('J4E1M7'))
# print(automaton.verify_adress('H5W1W6'))

# district = automaton.get_adress('H3W1W7')
# if not district:
#     print('none')
# else:
#     print(district.value)

# print(' ')
# print(' ')
# print(' ')
# print(' ')

# queue = queue.Queue()
# queue.put(automaton.initial_state)

# #for state in automaton.initial_State.next_states:
#     #print(state.value)


# def print_automaton():
#     while not queue.empty() :
#         elem = queue.get()
#         print(elem.value)
#         if not isinstance(elem, District):
#             for node in elem.next_states:
#                 queue.put(node)

# #print_automaton()

# with open("../request/requetes1.txt", "r") as f:
#     while(True):
#         line = f.readline().strip('\n').strip(' ').strip('\r').split()
#         if not line:
#             break
#         print(line[0])
#         print(line[1])
#         print(line[2])


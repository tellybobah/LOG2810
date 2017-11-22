from district import District
from delevery import Delevery

import queue

delevery = Delevery()
delevery.create_automat("CodesPostaux.txt")
delevery.parse_request("requetes1.txt")
 
print(delevery.automat.verify_adress('H1W1B2'))
print(delevery.automat.verify_adress('H4N2Y8')) 
district = delevery.automat.get_adress('H1W1B2')

print(district.packages.qsize())

while not district.packages.empty():
    print(district.packages.get().getWeight())

# automat = Automat()
# automat.create_state_adress("testAutomat.txt")

# for state in automat.initial_state.next_states:
#     print(state.value)

# print(automat.verify_adress('H3W1W6'))
# print(automat.verify_adress('H3W1W7'))
# print(automat.verify_adress('J4E1M7'))
# print(automat.verify_adress('H5W1W6'))

# district = automat.get_adress('H3W1W7')
# if not district:
#     print('none')
# else:
#     print(district.value)

# print(' ')
# print(' ')
# print(' ')
# print(' ')

# queue = queue.Queue()
# queue.put(automat.initial_state)

# #for state in automat.initial_State.next_states:
#     #print(state.value)


# def print_automat():
#     while not queue.empty() :
#         elem = queue.get()
#         print(elem.value)
#         if not isinstance(elem, District):
#             for node in elem.next_states:
#                 queue.put(node)

# #print_automat()

# with open("../request/requetes1.txt", "r") as f:
#     while(True):
#         line = f.readline().strip('\n').strip(' ').strip('\r').split()
#         if not line:
#             break
#         print(line[0])
#         print(line[1])
#         print(line[2])


from automat import Automat 

from multiprocessing import Queue

automat = Automat()
automat.create_state_adress("testAutomat.txt")
queue = Queue()
queue.put(automat.initial_State)

#for state in automat.initial_State.next_states:
    #print(state.value)


def print_automat():
    while not queue.empty() : 
        elem = queue.get()
        print(elem.value)
        for node in elem.next_states :
            queue.put(node)

print_automat()
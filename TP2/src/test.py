from automat import Automat 
import Queue
automat = Automat()
automat.create_state_adress("testAutomat.txt")
queue = Queue.Queue()
queue.put(automat.initial_State)

def print_automoat():
    while not queue.empty() : 
        elem = queue.get()
        print(elem.value)
        for node in elem.next_states :
            queue.put(node)

print_automoat()
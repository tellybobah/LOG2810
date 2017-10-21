"""
@author: Boubacar, Abderahmane, Leandre
"""

from graph import *
from hasse import Hasse

    
def ex2():
    g1 = GraphDessert('recette/manger.txt')
    g1.display()
    Has = Hasse(g1)
    Has.remove_relexivity()
    Has.remove_transitivity()
    Has.print_hasse()

ex2()




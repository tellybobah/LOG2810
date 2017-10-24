"""
@author: Boubacar, Abderahmane, Leandre
"""
import math
from drone import *

class Dijkstra:
    """
        Constructor fucntions
        Keeps the graph as an attribute as it is used by all the funtions

        graph - a graph
    """
    def __init__(self, graph):
        self.graph = graph

    """
        Tries to find a path with the 3amp drone or the 5amp drone or if there was no solution

        start_node - the starting node in the graph | Node
        end_node - the end node in the graph | Node
        package - the weight of the package | Package Enum
    """
    def solution(self, start_node, end_node, package):
        drone_3 = Drone3Amp(package)
        path, temp, energy_left = self.shortest_path(start_node, end_node, drone_3)

        #TODO find a cleaner way
        if path is False:
            drone_5 = Drone5Amp(package)
            path, temp, energy_left = self.shortest_path(start_node, end_node, drone_5)
        else:
            print('Utilisation du Drone 3.3 Amp')
            print('Chemin')
            print(*path, sep=' => ')
            print('Temp requis:', temp, 'minutes')
            print('Energie restante:', energy_left, '%')
            return

        if path is False:
            print('Aucun chemin possible')
        else:
            print('Utilisation du Drone 5.0 Amp')
            print('Chemin:')
            for node in path:
                print(node, end=' => ')
            print('Temp requis:', temp, 'minutes')
            print('Energie restante:', energy_left, '%')
            return

    """
        Finds the shortest path in the graph through dijkstra's algorithm with a specefic drone

        start_node - the starting node in the graph | Node
        end_node - the end node in the graph | Node
        drone - the drone used for this path | Drone
    """
    def shortest_path(self, start_node, end_node, drone):
        #Two dictionaries of nodes used by the algorithm
        visited_nodes = dict()
        remaining_nodes = dict()

        connections = self.graph.connections
        nodes = self.graph.get_nodes()

        #Initialize the remaining nodes dict with default values
        #default prev_node = None (represents the previous node)
        #default distance = infinity (represents the distance from the stating node)
        #Initialize the energy cost at that position to None
        for node in nodes:
            remaining_nodes.update({node:{'prev_node':None, 'distance':math.inf, 'energy_cost':None}})

        #The first node has a relative distance from the start_node of 0
        #and an energy cost of 0
        remaining_nodes[start_node].update({'prev_node':None, 'distance':0, 'energy_cost':0})

        #dijkstra algorithm
        #1. choose a node from the remaining nodes with shortest distance from the start
        #2. update the neighbours of that node if the distance is shorter in that path
        #3. put that node in the visited nodes
        #repeat until the end node is not in visited nodes
        while end_node not in visited_nodes:
            #1
            curr_node = self.closest_node(remaining_nodes)
            #2
            self.update_neighbours(curr_node, end_node, remaining_nodes, visited_nodes, drone)
            #3
            visited_nodes.update({curr_node:remaining_nodes.pop(curr_node)})
        
        #End of the algorithm
        #Return the path or false if there is no path
        path = self.generate_final_path(start_node, end_node, visited_nodes)
        if not path:
            return (False, 0, 0)
        path_time = visited_nodes[end_node]['distance']
        energy_left = 100 - visited_nodes[end_node]['energy_cost']


        return (path, path_time, energy_left)

    """
        Iterate over all of the neighbours of the current node
        Update their distance from the start_node and their last node in the remaining_nodes dict

        curr_node - the current node from which we are updating the neighbours | Node
        remaining_nodes - dict of not yet visited nodes | Dictionary
        visited_nodes - dict of visited nodes | Dictionary
    """
    def update_neighbours(self, curr_node, end_node, remaining_nodes, visited_nodes, drone):
        # if the current node is a station, set the energy cost to 0
        if curr_node in self.graph.list_stations and curr_node != end_node:
            remaining_nodes[curr_node]['energy_cost'] = 0

        for neighbour, dist_from_node in self.graph.get_neighbours(curr_node).items():
            if neighbour in visited_nodes:
                continue

            old_dist = remaining_nodes[neighbour]['distance']
            dist_from_start = remaining_nodes[curr_node]['distance']
            new_dist = dist_from_start + dist_from_node

            if neighbour in self.graph.list_stations and neighbour != end_node:
                new_dist += 20

            #Updates the distance and the energy to a node if the cost is less then what it was
            neighbour_cost = remaining_nodes[neighbour]['energy_cost']
            if neighbour_cost is None or neighbour_cost > remaining_nodes[curr_node]['energy_cost'] + drone.predictEnergy(dist_from_node):
                remaining_nodes[neighbour]['energy_cost'] = remaining_nodes[curr_node]['energy_cost'] + drone.predictEnergy(dist_from_node)
                remaining_nodes[neighbour].update({'prev_node':curr_node, 'distance':new_dist})

            if 100 - remaining_nodes[neighbour]['energy_cost'] < 20:
                remaining_nodes[neighbour].update({'distance':math.inf})  
    """
        Finds the closest node in the remaining nodes
    """
    def closest_node(self, remaining_nodes):
        return min(remaining_nodes.items(), key=lambda x: x[1]['distance'])[0]

    """
        Finds a the path by iterating through the previous nodes from the end node
        Returns false if no path exists to the start node
    """
    def generate_final_path(self, start_node, end_node, visited_nodes):
        path = []
        last = end_node
        path.append(last)
        while last != start_node:
            if last is None:
                return False
            last = visited_nodes[last]['prev_node']
            path.append(last)

        return reversed(path)

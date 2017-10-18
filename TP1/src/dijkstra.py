"""
@author: Boubacar, Abderahmane, Leandre
"""
import math
from util import timeit

@timeit
def shortest_path(graph, start, end, drone, list_stations):
    path = []
    path_distance = 0
    visited = dict()
    remaining_nodes = dict()
    connections = graph.connections
    nodes = connections.keys()

    for node in connections.keys():
        remaining_nodes.update({node:(math.inf, None)})
        
    remaining_nodes[start] = (0, None)

    while end not in visited:
        curr_node = closest_node(remaining_nodes)
        update_neighbours(curr_node, connections, remaining_nodes, visited, drone, list_stations)
        visited.update({curr_node:remaining_nodes.pop(curr_node)})
        print(*remaining_nodes)
        print(*visited)

    last = end
    path.append(last)
    while last != start:
        last = visited[last][1]
        path.append(last)

    return (path, visited[end][0])


def update_neighbours(curr_node, connections, remaining_nodes, visited, drone, list_stations):
    neighbours = connections[curr_node]
    for neighbour, distance in neighbours.items():
        if neighbour in visited:
            continue
        old_dist = remaining_nodes[neighbour][0]

        dist_from_start = remaining_nodes[curr_node][0]
        dist_from_node = distance

        new_dist = dist_from_start + dist_from_node

        if drone.predictEnergy(dist_from_node) < 20:
            #TODO : recalculer l'energie selon le chemin qu'il a 
            print("Predicted energy: ", drone.predictEnergy(dist_from_node))
            new_dist = math.inf
        elif neighbour in list_stations:
            new_dist += 20

        if new_dist < old_dist:
            remaining_nodes[neighbour] = (new_dist, curr_node)
            


def closest_node(remaining_nodes):
    return min(remaining_nodes.items(), key=lambda x: x[1][0])[0]
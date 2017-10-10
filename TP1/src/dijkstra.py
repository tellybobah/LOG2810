import math

def shortest_path(graph, start, end, drone):
    path = []
    path_distance = 0
    visited = dict()
    remaining_nodes = dict()
    connections = graph.connections

    for node in connections.keys():
        remaining_nodes.update({node:(math.inf, None)})

    remaining_nodes[start] = (0, None)


    while end not in visited:
        curr_node = closest_node(remaining_nodes)
        print('current node', curr_node)
        update_neighbours(curr_node, connections, remaining_nodes, visited)
        visited.update({curr_node:remaining_nodes.pop(curr_node)})

    print('visited:', visited)
    print('last node:',remaining_nodes)
    #return (path, path_distance)
    #return false

def update_neighbours(curr_node, connections, remaining_nodes, visited):
    neighbours = connections[curr_node]
    for neighbour, distance in neighbours.items():
        print(neighbour)
        if neighbour in visited:
            continue
        old_dist = remaining_nodes[neighbour][0]

        dist_from_start = remaining_nodes[curr_node][0]
        dist_from_node = distance

        new_dist = dist_from_start + dist_from_node

        if new_dist < old_dist:
            remaining_nodes[neighbour] = (new_dist, curr_node)

def closest_node(remaining_nodes):
    return min(remaining_nodes.items(), key=lambda x: x[1][0])[0]


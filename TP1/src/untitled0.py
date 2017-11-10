# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:31:01 2017

@author: Léandre
"""
from itertools import takewhile
from collections import defaultdict
from heapq import *

def parse_file( file_name):
        with open(file_name) as file:
            node_lines = list(takewhile(lambda x: x != '\n', file))
            edge_lines = list(takewhile(lambda x: x != '\n', file))
            return node_lines, edge_lines


g = []
def create_graph(g):
    #self.connections = dict()
    #self.list_stations = set()
    with open("arrondissements.txt") as file:
            node_lines = list(takewhile(lambda x: x != '\n', file))
            edge_lines = list(takewhile(lambda x: x != '\n', file))
    
    temp = ()
    
    for line in edge_lines:
        current_line = line.strip().split(",")
        node1 = current_line[0]
        node2 = current_line[1]
        distance = int(current_line[2])
        g.append((node1, node2, distance))
        g.append((node2, node1, distance))
    for line in node_lines:
        current_line = line.strip().split(",")
        for item in g : 
            if bool(current_line[1]):
                temp = (item[0],item[1],item[2]+20)
                item = temp
        pass
            



def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")


edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
        ]

print ("=== Dijkstra ===")

print (g)
#print ("A -> E:")
create_graph(g)
print (dijkstra(g, "2", "5"))
print (dijkstra(g, "7", "6"))
#print ("F -> G:")
#print (dijkstra(edges, "F", "G"))
    
import sys
from dimacs import *
from itertools import combinations
import random

def remove_edge(G, S):
    Gc = G.copy()
    for i in range(0, len(G)):
        Gc[i] = G[i].copy() - S
    return Gc

def vertex_cover(G):
    S=set()
    Es = edgeList(G)
    for (u,v) in Es:
        if u not in S and v not in S:
            S = S|{u,v}
    return S

def solve_vertex_cover(G):
    return vertex_cover(G)

if len(sys.argv) < 2:
    print("Specify graph")
    exit()
    
graph_file = sys.argv[1]
G = loadGraph("{0}".format(graph_file))
S = solve_vertex_cover(G)
saveSolution("{0}.sol".format(graph_file), S)

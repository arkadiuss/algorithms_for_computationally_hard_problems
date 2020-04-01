import sys
from dimacs import *
from itertools import combinations

def remove_edge(G, S):
    Gc = G.copy()
    for i in range(0, len(G)):
        Gc[i] = G[i].copy() - S
    return Gc

def vertex_cover(G, k, S):
    Es = edgeList(G)
    if k==0 and len(Es)>0:
        return None
    for (u,v) in Es:
        if u not in S and v not in S:
            Gc = remove_edge(G, {u,v})
            return vertex_cover(Gc, k-2, S|{u,v})
    return S

def solve_vertex_cover(G):
    for k in range(len(G)):
        S = vertex_cover(G, k, set())
        if S != None:
            return S
    return []

if len(sys.argv) < 2:
    print("Specify graph")
    exit()
    
graph_file = sys.argv[1]
G = loadGraph("{0}".format(graph_file))
S = solve_vertex_cover(G)
saveSolution("{0}.sol".format(graph_file), S)

import sys
from dimacs import *
from itertools import combinations

def remove_edge(G, S):
    Gc = G.copy()
    for i in range(0, len(G)):
        Gc[i] = G[i].copy() - S
    for s in S:
        Gc[s] = set()
    return Gc

def vertex_cover(G, k, S):
    c = -1
    for i in range(len(G)):
        if len(G[i]) > 0 and (c == -1 or len(G[i]) > len(G[c])):
            c = i
    if c != -1 and k<=0:
        return None
    elif c==-1:
        return S
    Gc = remove_edge(G, {c})
    return vertex_cover(Gc, k-1, S|{c})

def solve_vertex_cover(G):
    for k in range(len(G)):
    #    print(k,"----------------")
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

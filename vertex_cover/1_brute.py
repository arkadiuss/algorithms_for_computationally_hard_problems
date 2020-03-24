import sys
from dimacs import *
from itertools import combinations

def vertex_cover(G, k, S):
    Es = edgeList(G)
    for comb in combinations(range(len(G)), k):
        if isVC(Es, comb):
            return comb
    return None

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

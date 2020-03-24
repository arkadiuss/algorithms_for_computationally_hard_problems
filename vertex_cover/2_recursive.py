import sys
from dimacs import *
from itertools import combinations

def all_in(Es, S):
    for (u,v) in Es:
        if u not in S and v not in S:
            return (u,v)
    return None    

def filtered(Es, u):
    res = []
    for (x,y) in Es:
        if x != u and y != u:
            res.append((x,y))
    return res

def vertex_cover(Es, k, S):
    uv = all_in(Es, S)
    if uv == None:
        return S
    if k < 1:
        return None

    u = uv[0]
    v = uv[1]

    S1 = vertex_cover(filtered(Es, u), k-1, S|{u})
    if S1 != None:
        return S1
    S2 = vertex_cover(filtered(Es, v), k-1, S|{v})
    if S2 != None:
        return S2

def solve_vertex_cover(G):
    Es = edgeList(G)
    for k in range(len(G)):
        S = vertex_cover(Es, k, set())
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

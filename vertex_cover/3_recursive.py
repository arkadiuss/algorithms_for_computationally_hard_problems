import sys
from dimacs import *
from itertools import combinations

def all_in(Es, S):
    for (u,v) in Es:
        if u not in S and v not in S:
            return u
    return None    

def neigh(Es, u):
    S = set()
    for (x,y) in Es:
        if x==u:
            S.add(y)
        if y==u:
            S.add(x)
    return S

def filtered(Es, S):
    res = []
    for (x,y) in Es:
        if x not in S and y not in S:
            res.append((x,y))
    return res

def vertex_cover(Es, k, S):
    u = all_in(Es, S)
    if u == None:
        return S
    if k < 1:
        return None
    Nu = neigh(Es, u)
    S1 = vertex_cover(filtered(Es, {u}), k-1, S|{u})
    if S1 != None:
        return S1
    S2 = vertex_cover(filtered(Es, Nu), k-1, S|Nu)
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

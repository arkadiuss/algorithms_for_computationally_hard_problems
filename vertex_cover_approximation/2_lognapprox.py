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

def find_one(G):
    for i in range(1, len(G)):
        if len(G[i])==1:
            return list(G[i])[0]
    return None

def find_two(G):
    for i in range(1, len(G)):
        if len(G[i])==2:
            return i
    return None

def poly(G, k):
    c = len([1 for i in G if len(i)>1])
    if c/2 >= k:
        return None
    R = set()
    Gc = G.copy()
    while True:
        o = find_one(Gc)
        if o == None:
            o = find_two(Gc)
        if o == None:
            break
        if k <= 0:
            return None
        Gc = remove_edge(Gc, {o})
        R.add(o)
        k = k -1
    return R

def vertex_cover(G, k, S):
    c = -1
    for i in range(len(G)):
        if len(G[i]) > 2 and (c == -1 or len(G[i]) > len(G[c])):
            c = i
    if c != -1 and k<=0:
        return None
    elif c==-1:
        Sp = poly(G, k)
        if Sp == None:
            return None
        return S|Sp
    Gc = remove_edge(G, {c})
    return vertex_cover(Gc, k-1, S|{c})

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

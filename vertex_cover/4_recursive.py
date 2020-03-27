import sys
from dimacs import *
from itertools import combinations

def all_in(G, S):
    for u in range(1,len(G)):
        Su = G[u]
        if len(Su) > 2 and len(Su & S) == 0:
            return u 
    return None    

def neigh(G, u):
    return G[u]

def filtered(G, S):
    Gc = G.copy()
    for u in range(1, len(G)):
        Gc[u] = G[u].copy() - S
    for s in S:
        Gc[s]=set()
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

def poly(G):
    R = set()
    Gc = G.copy()
    while True:
        o = find_one(Gc)
        if o == None:
            o = find_two(Gc)
        if o == None:
            break;
        Gc = filtered(Gc, {o})
        R.add(o)
    return R

def vertex_cover(G, k, S):
    u = all_in(G, S)
    if u == None:
        return S|poly(G)
    if k < 1:
        return None
    Nu = neigh(G, u)
    S1 = vertex_cover(filtered(G, {u}), k-1, S|{u})
    if S1 != None:
        return S1
    S2 = vertex_cover(filtered(G, Nu), k-1, S|Nu)
    if S2 != None:
        return S2

def kernelize(G,k):
    Gc = G.copy()
    R = set()
    while True:
        changed = False
        Rs = set()
        for i in range(1, len(Gc)):
            if k < 1:
                break;
            if len(Gc[i]) == 1:
                Rs.add(list(Gc[i])[0])
                changed=True
                k = k-1
            if len(Gc[i]) > k:
                Rs.add(i)
                changed=True
                k = k-1
        Gc = filtered(Gc, Rs)
        R |= Rs
        if not changed:
            break
    if len(edgeList(Gc)) >= k*k:
        return None
    return Gc, R

def solve_vertex_cover(G):
    for k in range(1,len(G)):
        print(k)
        GcR = kernelize(G,k)
        if GcR == None:
            continue
        S = vertex_cover(GcR[0], k, set())
        if S != None:
            return S|GcR[1]
    return []

if len(sys.argv) < 2:
    print("Specify graph")
    exit()
    
graph_file = sys.argv[1]
G = loadGraph("{0}".format(graph_file))
S = solve_vertex_cover(G)
saveSolution("{0}.sol".format(graph_file), S)

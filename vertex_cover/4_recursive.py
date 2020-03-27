import sys
from dimacs import *
from itertools import combinations

def all_in(G, S):
    v = None
    for u in range(1,len(G)):
        Su = G[u]
        if len(Su) > 2:
            if v == None or len(Su) > len(G[v]):
                v=u 
    return v   

def neigh(G, u):
    return G[u]

def filtered(G, S):
    Gc = [set()]*len(G)
    for u in range(1, len(G)):
        if u not in S:
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
        Gc = filtered(Gc, {o})
        R.add(o)
        k = k -1
    return R

def vertex_cover(G, k, S):
    #R = kernelize(G,k)
    #if R == None:
    #    return None
    #G, RS = R
    #k -= len(RS) 
    if k<0:
        return None
    u = all_in(G, S)
    if u == None:
        P = poly(G,k)
        if P == None:
            return None
        return S|P
    if k < 1:
        return None
    Nu = neigh(G, u)
    S2 = vertex_cover(filtered(G, Nu), k-len(Nu), S|Nu)
    if S2 != None:
        return S2
    S1 = vertex_cover(filtered(G, {u}), k-1, S|{u})
    if S1 != None:
        return S1


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
    for k in range(60,len(G)):
        GcR = kernelize(G,k)
        if GcR == None:
            continue
        print(k, len(GcR[1]))
        S = vertex_cover(GcR[0], k-len(GcR[1]), set())
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

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

def poly(G):
    c = len([1 for i in G if len(i)>1])
    R = set()
    Gc = G.copy()
    while True:
        o = find_one(Gc)
        if o == None:
            o = find_two(Gc)
        if o == None:
            break
        Gc = remove_edge(Gc, {o})
        R.add(o)
    return R

def kernelize(G):
    Gc = G.copy()
    R = set()
    while True:
        changed = False
        Rs = set()
        for i in range(1, len(Gc)):
            if len(Gc[i]) == 1:
                Rs.add(list(Gc[i])[0])
                changed=True
                break
        Gc = remove_edge(Gc, Rs)
        R |= Rs
        if not changed:
            break
    return Gc, R



def vertex_cover(G):
    S = set()
    while True:
        G, RS = kernelize(G)
        S |= RS
        c = -1
        for i in range(len(G)):
            if len(G[i]) > 2 and (c == -1 or len(G[i]) > len(G[c])):
                c = i
        if c==-1:
            Sp = poly(G)
            return S|Sp
        G = remove_edge(G, {c})
        S=S|{c}

def solve_vertex_cover(G):
    S = vertex_cover(G)
    return S

if len(sys.argv) < 2:
    print("Specify graph")
    exit()
    
graph_file = sys.argv[1]
G = loadGraph("{0}".format(graph_file))
S = solve_vertex_cover(G)
saveSolution("{0}.sol".format(graph_file), S)

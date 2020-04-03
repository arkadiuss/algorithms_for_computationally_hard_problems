import sys
import random
from dimacs import *
from itertools import combinations

def remove_edge(G, S):
    Gc = G.copy()
    for i in range(0, len(G)):
        Gc[i] = G[i].copy() - S
    for s in S:
        Gc[s] = set()
    return Gc

def make_swap(Es, S):
    while True:
        v = random.randint(1, len(G))
        if v in S:
            Sc = S.copy() - {v}
        else:
            Sc = S.copy()|{v}
        if isVC(Es, Sc):
            return Sc, v

def undo_swap(S, v):
    if v not in S:
        return S.copy()|{v}
    return S.copy() - {v}

def sa(G):
    Es = edgeList(G)
    S = set(range(1,len(G)))
    steps = 100000
    st = 0
    p = 0.15
    while st < steps:
        Sp, v = make_swap(Es,S)
        cp = random.random()
        if len(Sp) > len(S) and cp >= p:
            Sp = undo_swap(Sp, v)
        if st%100==0:
            p*=0.99
        if st%10000==0:
            print(st)
        st += 1
        S = Sp
    return S

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
    S = sa(G)
    return S

if len(sys.argv) < 2:
    print("Specify graph")
    exit()
    
graph_file = sys.argv[1]
G = loadGraph("{0}".format(graph_file))
S = solve_vertex_cover(G)
saveSolution("{0}.sol".format(graph_file), S)

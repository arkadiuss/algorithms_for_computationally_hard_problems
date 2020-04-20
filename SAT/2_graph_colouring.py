import pycosat
from dimacs import *
import sys

def to_sat(graph, k):
    clauses = []
    for v in range(1, len(graph)):
        clauses.append([(v, i) for i in range(k)])
        for i in range(k):
            for j in range(i+1,k):
                clauses.append([(-v,i), (-v,j)])
    
    for u,v in edgeList(graph):
        for i in range(k):
            clauses.append([(-u,i), (-v, i)])
    return clauses

def sgn(a):
    if a == 0:
        return 0
    elif a > 0:
        return 1
    return -1

def flatten(clauses,k):
    return [ [ sgn(u)*(abs(u)*k+v) for u,v in i] for i in clauses]

def solution_colors(clauses, k):
    return [ x%k for x in clauses if x > 0]

def coloring(graph, k):
    clauses = to_sat(graph, k)
    rclauses = flatten(clauses, k)
    solution = pycosat.solve(rclauses)
    if solution == u'UNSAT':
        return solution
    return solution_colors(solution, k)

def verify(graph, coloring):
    for u,v in edgeList(graph):
        if coloring[u-1] == coloring[v-1]:
            return False
    return True

if len(sys.argv) < 3:
    print("Usage: python 2_graph_colouring.py graph_path k")

k = int(sys.argv[2])
graph = loadGraph(sys.argv[1])
c = coloring(graph, k)
if c != u'UNSAT':
    print(c)
    print(verify(graph, c))
else:
    print(c)

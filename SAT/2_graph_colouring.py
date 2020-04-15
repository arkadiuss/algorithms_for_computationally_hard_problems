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

def redimension(clauses):
    return clauses

def coloring(graph, k):
    clauses = to_sat(graph, k)
    rclauses = redimension(clauses)
    solution = pycosat.solve(rclauses)
    return solution != u'UNSAT'

if len(sys.argv) < 3:
    print("Usage: python 2_graph_colouring.py graph_path k")

k = int(sys.argv[2])
graph = loadGraph(sys.argv[1])
print(coloring())

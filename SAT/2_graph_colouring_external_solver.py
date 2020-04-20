import pycosat
from dimacs import *
import sys
import os

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

def verify(graph, coloring):
    for u,v in edgeList(graph):
        if coloring[u-1] == coloring[v-1]:
            return False
    return True

def coloring_save(graph, k, graphname):
    clauses = to_sat(graph, k)
    rclauses = flatten(clauses, k)
    gname = os.path.basename(graphname)
    filename = 'clauses/clauses_{0}_{1}'.format(gname, k)
    saveCNF(filename, rclauses)
    return filename

def invoke_solver(filename):
    sol_filename = "{0}.sol".format(filename)
    os.system("./glucose-syrup-4.1/simp/glucose_static {0} {1}".format(filename, sol_filename))
    with open(sol_filename, "r") as f:
        return f.read()

def convert_solution(result):
    if result == "UNSAT\n":
        return u'UNSAT'
    return [ int(x) for x in result.split(" ")]

if len(sys.argv) < 3:
    print("Usage: python 2_graph_colouring.py graph_path k")

k = int(sys.argv[2])
graph = loadGraph(sys.argv[1])
f = coloring_save(graph, k, sys.argv[1])
result = invoke_solver(f)
sol = convert_solution(result)
if sol != u'UNSAT':
    colors = solution_colors(sol, k)
    print(colors)
    print(verify(graph, colors))
else:
    print(sol)

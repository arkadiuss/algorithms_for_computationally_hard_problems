from pulp import *
from dimacs import *
import sys

def create_variables(graph, k):
    return [[LpVariable("x_{0}_{1}".format(v,i), cat="Binary") for i in range(1, k+1)] for v in range(len(graph))]

def create_model(name, graph, k):
    model = LpProblem(name, LpMinimize)
    variables = create_variables(graph, k)
    model += 0

    for v in range(len(graph)):
        vsum = variables[v][0]
        for i in range(1,k):
            vsum += variables[v][i]
        model += vsum == 1

    for (u,v) in edgeList(graph):
        for i in range(k):
            model += variables[u][i] + variables[v][i] <= 1
    
    return model

def solution_vertices(sol, k):
    return [ (i%k)+1 for i,v in enumerate(model.variables()) if v.value()==1 ]

if len(sys.argv) < 3:
    print("Usage: python program_name.py graph_path k")
    exit(1)

k = int(sys.argv[2])
graph = loadGraph(sys.argv[1])
print(len(graph))
model = create_model(sys.argv[1], graph, k)
print(model)
sol = model.solve(GLPK())
print(LpStatus[model.status])
vsol = solution_vertices(sol, k)
print("VERTICES")
print(len(vsol))
print(vsol)


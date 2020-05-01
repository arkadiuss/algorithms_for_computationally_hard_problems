from pulp import *
from dimacs import *
import sys

def create_variables(graph):
    return [ LpVariable("x"+str(v), cat="Binary") for v in range(len(graph)) ]

def create_model(name, graph):
    model = LpProblem(name, LpMinimize)
    variables = create_variables(graph)

    vsum = len(graph[0])*variables[0]
    for i in range(1,len(variables)):
        vsum += len(graph[i])*variables[i]

    model += vsum
    for (u,v) in edgeList(graph):
        model += variables[u] + variables[v] >= 1
    return model

def solution_vertices(sol):
    return [ i for i,v in enumerate(model.variables()) if v.value()==1.0 ]

if len(sys.argv) < 2:
    print("Usage: python program_name.py graph_path")
    exit(1)

graph = loadGraph(sys.argv[1])
model = create_model(sys.argv[1], graph)
print(model)
sol = model.solve(GLPK())
print("OBJECTIVE VALUE")
print(value(model.objective))
vsol = solution_vertices(sol)
print("VERTICES")
print(len(vsol))
print(vsol)


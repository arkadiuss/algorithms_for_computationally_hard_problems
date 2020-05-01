from pulp import *
from dimacs import *
import sys

def create_variables(graph):
    return [ LpVariable("x"+str(v), lowBound=0, upBound=1, cat="Continuous") for v in range(len(graph)) ]

def create_model(name, graph):
    model = LpProblem(name, LpMinimize)
    variables = create_variables(graph)

    vsum = variables[0]
    for i in range(1,len(variables)):
        vsum +=variables[i]

    model += vsum
    for (u,v) in edgeList(graph):
        model += variables[u] + variables[v] >= 1
    return model

def solution_vertices(sol):
    return [ i for i,v in enumerate(model.variables()) if v.value()>=0.5 ]

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


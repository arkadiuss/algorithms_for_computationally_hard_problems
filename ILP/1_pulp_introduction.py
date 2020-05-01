from pulp import *

model = LpProblem("test", LpMinimize)

x = LpVariable("x", lowBound=0, upBound=5, cat="Continuous")
y = LpVariable("y", lowBound=0, upBound=3, cat="Integer")
z = LpVariable("z", cat="Binary")


model += 5-x+2*y-z
model += x >= y
model += y >= z

print(model)

for (name, solver) in [ ("CBC solver", None), ("GLPK solver", GLPK()) ]:
    model.solve(solver)
    print(LpStatus[model.status])

    for var in model.variables():
          print(var.name, "=", var.varValue)
    print(value(model.objective))



import pycosat
import random
import numpy as np
import matplotlib.pyplot as plt

k = 3 # literals per clause
T = 100 # repetitions count
ns = [10, 50, 100] # variables counts
n = 10

def random_clause(n, k):
    chosen = np.array(random.choices(range(1,n+1), k=k))
    signs = np.array(random.choices([1,-1], k=k))
    return (signs*chosen).tolist()

x = []
y = []
for a in np.arange(1, 10, 0.1):  
    S = 0 # satisfied
    for t in range(T):
        formula = [random_clause(n,k) for i in range(int(a*n))]
        if pycosat.solve(formula) != u'UNSAT':
            S = S + 1
    x.append(a)
    y.append(S/T)

plt.plot(x, y)
plt.savefig('wykres.png')

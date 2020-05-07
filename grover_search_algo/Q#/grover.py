# -*- coding: utf-8 -*-
import qsharp
from Microsoft.Quantum.Tutorial.Grover import Search

# nQubits = 2, is just for showing a way to pass value
# as the example is just built for 2 qubit system,
# we must not change it to any other value
result = Search.simulate(nQubits=2)
print(result)
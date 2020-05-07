import cirq

q0, q1 = cirq.LineQubit.range(2)
# q0 = cirq.GridQubit(0, 0)
# q1 = cirq.GridQubit(0, 1)

circuit = cirq.Circuit()
circuit.append([cirq.H(q0), cirq.H(q1)])

# Oracle for |00⟩ :
circuit.append([cirq.X(q0), cirq.X(q1)])
circuit.append(cirq.CX(q0,q1))
circuit.append([cirq.X(q0), cirq.X(q1)])

circuit.append([cirq.H(q0), cirq.H(q1)])

# reflection circuit :
circuit.append([cirq.Z(q0), cirq.Z(q1)])
circuit.append(cirq.CX(q0,q1))

circuit.append([cirq.H(q0), cirq.H(q1)])
circuit.append([cirq.measure(q0), cirq.measure(q1)])

print(circuit)

simulator = cirq.Simulator()
result = simulator.simulate(circuit)
# result = simulator.run(circuit, repetitions=40) # NISQ computers
print(result)
import cirq

q0 = cirq.LineQubit(8)
q1 = cirq.LineQubit(-8)
circuit = cirq.Circuit()

gatesC = [cirq.H(q0), cirq.H(q1), cirq.CNOT(q0, q1)] #gates for a separate control circuit
gates = [cirq.H(q0), cirq.CNOT(q0, q1)]
measure = [cirq.measure(q0, key="m0"), cirq.measure(q1, key="m1")]

circuit.append(gates)
circuit.append(measure)

print(circuit)

sim = cirq.Simulator()
result = sim.run(circuit, repetitions=100000)

print(result.histogram(key="m0"))
print(result.histogram(key="m1"))
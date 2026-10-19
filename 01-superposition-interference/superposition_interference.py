import cirq

qubit = cirq.LineQubit(8) #creates the qubit; the 8 is just the x coordinate it's created at, nothing significant
circuit = cirq.Circuit() #creates the circuit

#the gates below describe the circuit i used for my third experiment (see 01-interference.md)
#my first and second experiments used a different list of gates (see 01-interference.md)
gates = [cirq.H(qubit), cirq.X(qubit)] #list of gates in order from left to right
measure = [cirq.measure(qubit, key="m1")] #only need one measurement for one qubit

#appends args to circuit
circuit.append(gates)
circuit.append(measure)

print(circuit) #visualizes the circuit

sim = cirq.Simulator() #initializes the simulation
result = sim.run(circuit, repetitions=100000) #starts the simulation

print(result.histogram(key="m1")) #expected result: 1, regardless of repetition/shot magnitude
#!/usr/bin/env python
# coding: utf-8

# In[31]:


import cirq


# In[32]:


print(cirq.google.Sycamore)


# In[64]:


"""Creating a circuit."""
# Define two qubits.
a = cirq.NamedQubit("a")
b = cirq.NamedQubit("b")

# Create a circuit from the list of operations.
circuit = cirq.Circuit(
cirq.H(a),
cirq.CNOT(a, b),
    cirq.measure(a,b)
)
print("Circuit:\n")
print(circuit)


# In[65]:


print("\nMoments in the circuit:\n")
for i, moment in enumerate(circuit):
    print('Moment {}: {}'.format(i, moment))


# In[66]:


print(repr(circuit))


# In[68]:


simulator = cirq.Simulator()
# Pass the circuit to the simulator.run method.
result = simulator.run(circuit, repetitions=20)
print("Measurement results:")
print(result)


# In[76]:


circuit2 = cirq.Circuit(
    cirq.H(a),
    cirq.X(b),
    cirq.CNOT(a, b),
    cirq.measure(a,b)
)
simulator = cirq.Simulator()
result = simulator.run(circuit2, repetitions=20)
print(circuit2)
print(result)


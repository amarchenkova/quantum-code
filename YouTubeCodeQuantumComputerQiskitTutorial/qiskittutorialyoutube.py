#!/usr/bin/env python
# coding: utf-8

# Anastasia's Qiskit Tutorial! github.com/amarchenkova for the code 

# In[1]:


from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, Aer, IBMQ
from qiskit.visualization import plot_histogram
provider = IBMQ.load_account()


# In[4]:


qreg = QuantumRegister(2, 'q')
creg = ClassicalRegister(2, 'c')

circuit = QuantumCircuit(qreg, creg)


# In[5]:


circuit.h(qreg[0])
circuit.cx(qreg[0], qreg[1])
circuit.measure(range(2), range(2))


# In[6]:


backend = Aer.get_backend('qasm_simulator')
counts = execute(circuit, backend).result().get_counts()
print(counts)
plot_histogram(counts)


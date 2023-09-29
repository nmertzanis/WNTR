"""
The following example demonstrates how to import WNTR, generate a water network 
model from an INP file, simulate hydraulics, and plot simulation results on the network.
"""
from matplotlib import pyplot as plt

import wntr

# Create a water network model
inp_file = 'networks/Tutorial.inp'
wn = wntr.network.WaterNetworkModel(inp_file)

# Graph the network
wntr.graphics.plot_network(wn, title=wn.name)

# Simulate hydraulics
sim = wntr.sim.EpanetSimulator(wn)
results = sim.run_sim()

# Plot results on the network

pressure_at_5hr = results.node['pressure'].loc[5 * 3600, :]
wntr.graphics.plot_network(wn, node_attribute=pressure_at_5hr, node_size=30,
                           title='Pressure at 5 hours')

# Theres demand, head, pressure and quality in results

# Get pressure per node
pressure_at_5hr = results.node['pressure'].loc[5 * 3600, :]
print('Pressure at 5 hr per node: \n', pressure_at_5hr)

# Get head per node
head_at_5hr = results.node['head'].loc[5 * 3600, :]
print('Head at 5 hr per node: \n', head_at_5hr)

plt.show()

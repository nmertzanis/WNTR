"""
The following example demonstrates how to import WNTR, generate a water network 
model from an INP file, simulate hydraulics, and plot simulation results on the network.
"""
from matplotlib import pyplot as plt

import wntr

# Create a water network model
inp_file = 'networks/FOS_pump_0.inp'
wn = wntr.network.WaterNetworkModel(inp_file)
wn.options.hydraulic.viscosity = 1.0
wn.options.hydraulic.specific_gravity = 1.0
wn.options.hydraulic.demand_multiplier = 1.0
wn.options.hydraulic.demand_model = 'DD'
wn.options.hydraulic.minimum_pressure = 0
wn.options.hydraulic.required_pressure = 1
wn.options.hydraulic.pressure_exponent = 0.5
wn.options.hydraulic.trials = 50
wn.options.hydraulic.accuracy = 0.001
wn.options.hydraulic.unbalanced = 'CONTINUE'
wn.options.hydraulic.unbalanced_value = 10
wn.options.hydraulic.checkfreq = 2
wn.options.hydraulic.maxcheck = 10
wn.options.hydraulic.damplimit = 0.0
wn.options.hydraulic.headerror = 0.0
wn.options.hydraulic.flowchange = 0.0
wn.options.hydraulic.inpfile_units = "LPS"
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

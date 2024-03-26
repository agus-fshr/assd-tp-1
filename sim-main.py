import snh as snh

# Create a new instance of the simulator
sim = snh.Sim()

# Make a circuit

# Create the components you want in the circuit
sim.square_wave = sim.gen_square_wave(7.5e3, 1, 0.75)
sim.filter = snh.Filter()
sim.zoh = snh.ZOH(f_sample=1e6, sim=sim)
sim.switch = snh.Switch(f_sample=1e6, sim=sim)
sim.recovery_filter = snh.Filter()

# Connect everything
sim.makeCircuit({
    'square_wave': True,
    'filter': True,
    'zoh': True,
    'switch': True,
    'recovery_filter': True
})


# Simulate the circuit
sim.simulate()
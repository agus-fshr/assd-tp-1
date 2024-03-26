import snh as snh

# Create a new instance of the simulator
sim = snh.Sim(1e-3, 1e-9)

# Create the components you want in the circuit
my_square_wave = sim.gen_square_wave(7.5e3, 1, 0.75)
my_filter = snh.Filter()
my_zoh = snh.ZOH(f_sample=1e6, sim=sim)
my_switch = snh.Switch(f_sample=1e6, sim=sim)
my_recovery_filter = snh.Filter()

# Connect everything
sim.makeCircuit({
    'square_wave': my_square_wave,
    'filter': my_filter,
    'zoh': my_zoh,
    'switch': my_switch,
    'recovery_filter': my_recovery_filter
})

# Simulate the circuit
sim.simulate()
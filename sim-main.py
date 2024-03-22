import snh as snh

# Create a new instance of the simulator
sim = snh.Sim()

# Make a circuit

sim.square_wave = sim.gen_square_wave(7.5e3, 1, 0.75)

filter = snh.Filter()

# Simulate the circuit
sim.simulate()
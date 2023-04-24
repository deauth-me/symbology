import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Initialize symbols
symbols = []

for i in range(10):
    symbol, = ax.plot([], [], lw=2)
    symbols.append(symbol)

# Initialize the symbols' positions and velocities
positions = np.random.rand(10, 2) * 100
velocities = np.random.randn(10, 2) * 0.5

# Define the interplay between the symbols (update function)
def update(frame):
    global positions, velocities

    # Update positions based on velocities
    positions += velocities

    # Reflect symbols off the boundaries
    velocities[positions < 0] *= -1
    velocities[positions > 100] *= -1

    # Update symbol's data on the plot
    for i in range(10):
        symbols[i].set_data(positions[i, 0], positions[i, 1])

    return symbols

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(200), interval=20, blit=True)

# Show the simulation
plt.show()

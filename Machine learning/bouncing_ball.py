import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Triangle, Rectangle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# Function to create a tree
def add_tree(x_pos, height):
    # Tree trunk
    trunk = Rectangle((x_pos - 0.1, -2), 0.2, height * 0.4, color='brown')
    ax.add_patch(trunk)
    
    # Tree foliage (three triangles for fuller look)
    triangle1 = Triangle((x_pos, -2 + height * 0.4), 0.4, 0.6, color='forestgreen')
    triangle2 = Triangle((x_pos, -2 + height * 0.6), 0.35, 0.5, color='forestgreen')
    triangle3 = Triangle((x_pos, -2 + height * 0.8), 0.3, 0.4, color='forestgreen')
    ax.add_patch(triangle1)
    ax.add_patch(triangle2)
    ax.add_patch(triangle3)

# Add multiple trees of different sizes
add_tree(-1.5, 2.5)
add_tree(-0.8, 2.2)
add_tree(0.7, 2.3)
add_tree(1.4, 2.4)

# Create the ball (a circle)
ball = plt.Circle((0, 0), 0.2, color='pink')
ax.add_patch(ball)

# Animation parameters
angle = 0
radius = 1

def update(frame):
    # Update the ball's position
    x = radius * np.cos(np.radians(frame))
    y = radius * np.sin(np.radians(frame))
    ball.center = (x, y)
    return ball,

# Create the animation
anim = FuncAnimation(fig, update, frames=np.linspace(0, 360, 128),
                    interval=20, blit=True, repeat=True)

# Set background color to light blue (sky)
ax.set_facecolor('lightblue')
fig.patch.set_facecolor('lightblue')

plt.title('Bouncing Ball Animation')
plt.show() 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# Setup figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.1, 1.1)
ax.set_xlabel('x')
ax.set_ylabel('$y = x^2$')
ax.set_title(r'Visualizing $-1 \leq x \leq 1$ implies $0 \leq x^2 \leq 1$')

# Plot parabola
x = np.linspace(-1.5, 1.5, 500)
y = x**2
ax.plot(x, y, color='gray', linestyle='--', label='$y = x^2$')

# Highlight the region -1 <= x <= 1
x_highlight = np.linspace(-1, 1, 200)
y_highlight = x_highlight**2
ax.plot(x_highlight, y_highlight, color='dodgerblue', linewidth=2, label='-1 ≤ x ≤ 1')

# Initialize point that will move
point, = ax.plot([], [], 'ro', markersize=8)

# Text to show the x and x^2 values
text = ax.text(-1, 0.8, '', fontsize=12, color='purple')

# Animation update function
def update(frame):
    x_val = -1 + 2*frame / 100  # x moves from -1 to 1
    y_val = x_val**2
    point.set_data([x_val], [y_val])  # FIXED HERE
    text.set_text(f'x = {x_val:.2f}, x² = {y_val:.2f}')
    text.set_position((x_val, y_val + 0.1))
    return point, text

# Animate
ani = FuncAnimation(fig, update, frames=101, interval=50, blit=True)

writer = FFMpegWriter(fps=20)
ani.save('x_squared_animation.mp4', writer=writer)

print("Animation saved as 'x_squared_animation.mp4'")


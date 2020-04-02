import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 8))
# plt.style.use('mystyle')
theta = np.arange(0, 2 * np.pi, np.pi /2000)
theta = theta[1:]
k = 3
r = 1 / (1 - (np.mod(theta * k / np.pi, 2) - 1) ** 2)
x = r * np.sin(theta)
y = r * np.cos(theta)
plt.plot(x, y )
plt.scatter([0],[0], facecolor='red')
plt.xlim(-40, 40)
plt.ylim(-40, 40)
plt.grid(True)
plt.show()
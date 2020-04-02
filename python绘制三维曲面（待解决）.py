import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(16, 16))
#plt.style.use('mystyle')
u = np.arange(0, 2 * np.pi, np.pi / 500)
v = np.linspace(0.5, 10, 50)
k = 5
a = np.mod(u * k / np.pi, 2) - 1
v = np.reshape(v, (50, 1))
r = np.multiply(v, 1 / (1 - a * a))
# 用于排除掉 无穷大的情况
r[r > 32] = 32
x = r * np.sin(u)
y = r * np.cos(u)
plt.scatter(0, 0, facecolor='red')
plt.plot(x, y)
plt.xlim(-40, 40)
plt.ylim(-40, 40)
plt.show()
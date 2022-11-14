import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 1, 20)
d =  (1 + 0.6*np.sin(2*np.pi*x/0.7)) + 0.3*np.sin(2*np.pi*x)/2
c = [0.19, 0.9]
r = [0.16, 0.22]
p = 0.1

w1 = np.random.rand()
w2 = np.random.rand()
b = np.random.rand()

F1 = np.exp(-(x-c[0])**2/(2*r[0]**2))
F2 = np.exp(-(x-c[1])**2/(2*r[1]**2))

for i in range(700):
    for j in range(len(x)):
        v = F1[j] * w1 + F2[j] * w2 + b
        e = d[j] - v
        w1 += p*e*F1[j]
        w2 += p*e*F2[j]
        b += p*e
    print(w1)

y =[]
for i in range(len(x)):
    y.append(F1[i] * w1 + F2[i] * w2 + b)

fig, ax = plt.subplots()
ax.plot(x, d, x, y)
plt.show()

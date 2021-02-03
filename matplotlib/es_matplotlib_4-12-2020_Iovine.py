import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 10])
ypoints = np.array([0, 20])

plt.ylabel('velocità v (m/s)')
plt.xlabel('istante di tempo t (s)')

plt.title('grafico velocità-tempo')

plt.plot(xpoints, ypoints)
plt.show()

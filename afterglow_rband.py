
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('C:/Users/Dell/Downloads/Dataset 1.txt', delimiter=',', skiprows=1)

#Extract the columns
x = data[:, 0]
y = data[:, 1]

#Plot the flux density versus time curve
plt.plot(x, y, 'o-', color='blue')
plt.xlabel('Time since trigger(s)')
plt.ylabel('Flux Density')
plt.title('Afterglow of GRB060614 in the R band')
plt.grid(True)
plt.show()

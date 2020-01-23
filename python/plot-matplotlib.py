import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-5, 5, 100)

# the function, which is y = x^2 here
y = x**3-3*x*x+2
# y = numpy.sin(x)
# y = numpy.sin(x)*numpy.exp(-0.1*x)

plt.plot(x, y)

# show the plot
plt.show()

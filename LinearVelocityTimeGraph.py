import DisplacementTimeGraph
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from math import sqrt
from math import pi
from math import sin
import pylab as pl

angGraph = DisplacementTimeGraph.angularGraph()

x_axis = angGraph.x_axis
y_axis = angGraph.the_newVelocity

pl.plot(x_axis, y_axis)
pl.plot(x_axis, y_axis, 'ro')

pl.title('Velocity-time graph')
pl.xlabel('Time')
pl.ylabel('Velocity')

pl.show()
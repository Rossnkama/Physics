import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from math import sqrt
from math import pi
from math import cos
import pylab as pl

class angularGraph():

    print(matplotlib.__version__)

    print("")

    y_axis = []
    newVelocity = []
    newAcceleration = []

    TIMES = [0, 0.25, 0.50, 0.75, 1, 1.25]

    AMPLITUDE = (40e-3)
    FREQUENCY = (0.5)
    ANGULAR_VELOCITY = (2 * pi * FREQUENCY)

    print("--------------------------")

    for i in range(len(TIMES)):

        DISPLACEMENT = (AMPLITUDE * cos(ANGULAR_VELOCITY * TIMES[i]))    # Displacement
        ACCELERATION = ((ANGULAR_VELOCITY ** 2) * DISPLACEMENT)
        VELOCITY = (ANGULAR_VELOCITY * sqrt((AMPLITUDE ** 2) - (DISPLACEMENT ** 2)))

        print("At time {0} the displacement is {1} mm!").format(TIMES[i], DISPLACEMENT)
        # (To debug) --> print("Sum is: {0} X {1} * {2}").format(AMPLITUDE, sin(ANGULAR_VELOCITY * TIMES[i]), TIMES[i])
        print("")
        print("At time {1} the velocity is also {0} mm s-1!").format(VELOCITY, TIMES[i])
        print("")
        print("At time {1} the Acceleration is {0} mm s-2!").format(ACCELERATION, TIMES[i])
        print("--------------------------")

        y_axis.append(DISPLACEMENT)
        newVelocity.append(VELOCITY)
        newAcceleration.append(ACCELERATION)

    new_y_axis = np.array(y_axis)
    the_newVelocity = np.array(newVelocity)
    the_newAcceleration = np.array(newAcceleration)

    x_axis = np.array(TIMES)

    pl.plot(x_axis, new_y_axis)
    pl.plot(x_axis, new_y_axis, 'ro')

    pl.title('Displacement-time graph')
    pl.xlabel('Time')
    pl.ylabel('Displacement')

    pl.show()
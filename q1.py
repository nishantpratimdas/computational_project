import math
import matplotlib.pyplot as plt
import random
import time

# function which generates a set of noOfWalks walks and noOfSteps steps


def randomWalk(noOfWalks, noOfSteps):

    # declaring variables(which keep track of each distance travelled) and arrays(which store coordinates)
    X = []
    Y = []
    radialTotal = 0
    arrayRadialDistance = []

    # seeding the randomiser
    random.seed(None)

    # loop to generate random walk
    for j in range(0, noOfWalks):

        x = 0.0
        y = 0.0
        radialTotal = 0.0

        X1 = []
        Y1 = []

        X1.append(x)
        Y1.append(y)

        for i in range(0, noOfSteps):
            # generate a random angle
            angle = 2 * math.pi * random.random()
            x1 = math.cos(angle)
            y1 = math.sin(angle)

            x = x + x1
            y = y + y1
            X1.append(x)
            Y1.append(y)

        X.append(X1)
        Y.append(Y1)

        radialTotal = x ** 2 + y ** 2
        arrayRadialDistance.append(radialTotal)

    sumRadial = 0
    for i in range(len(arrayRadialDistance)):
        sumRadial = sumRadial + arrayRadialDistance[i]

    radialRms = math.sqrt(sumRadial / len(arrayRadialDistance))

    sum_x = 0
    sum_y = 0
    for i in range(len(X)):
        sum_x = sum_x + X[i][len(X[i]) - 1]
        sum_y = sum_y + Y[i][len(Y[i]) - 1]

    # average x, y and radial distance of the walks in a set
    avgX = sum_x / len(X)
    avgY = sum_y / len(Y)
    radialDistance = math.sqrt(avgX ** 2 + avgY ** 2)

    return X, Y, radialRms, avgX, avgY, radialDistance


figure, axes = plt.subplots(nrows=2, ncols=5)

# initial values of the walk
noOfWalks = 100
noOfSteps = 250
add = 300

arrayRms = []
steps = []

# arrays which will hold different values of the walk for each walk
X = []
Y = []
radialRms = []
avgX = []
avgY = []
Radial_dis = []

#
for k in range(5):

    # a to e are unnecessary variables whose value will be appended to the above defined arrays
    a, b, c, d, e, f = randomWalk(
        noOfWalks, noOfSteps)

    X.append(a)
    Y.append(b)
    radialRms.append(c)
    avgX.append(d)
    avgY.append(e)
    Radial_dis.append(f)

    # prints output
    print("\n\nnumber of steps = " + str(noOfSteps))
    print("radial distance = ", round(Radial_dis[k], 2))
    print("rms radial distance = ", round(radialRms[k], 2))
    print("sqrt(N) = ", round(math.sqrt(noOfSteps), 2))
    print("average X = ", round(avgX[k], 2))
    print("average Y = ", round(avgY[k], 2))
    arrayRms.append(radialRms[k])
    steps.append(math.sqrt(noOfSteps))

    # code to plot first 5 random walks
    for i in range(5):
        axes[0, k].set_xlabel('X')
        axes[0, k].set_ylabel('Y')
        axes[0, k].grid(True)
        axes[0, k].set_title("For " +
                             str(noOfSteps) + " steps")
        axes[0, k].plot(X[k][i], Y[k][i])

    noOfSteps = noOfSteps + add

# code to plot rms radial distance vs sqrt(N)
plt.figure()
plt.title("rms radial distance vs sqrt(N) = 250, 350, 650, 950, 1250")
plt.ylabel('rms radial distance')
plt.xlabel('sqrt(N)')
plt.plot(steps, arrayRms)
plt.grid(True)
plt.show()


'''
//walk 1,2,3,4,5 were graphed

//begin output:

number of steps = 250
radial distance =  2.82
rms radial distance =  15.76
sqrt(N) =  15.81
average X =  1.8
average Y =  -2.18


number of steps = 550
radial distance =  2.7
rms radial distance =  23.76
sqrt(N) =  23.45
average X =  1.38
average Y =  -2.32


number of steps = 850
radial distance =  1.86
rms radial distance =  30.99
sqrt(N) =  29.15
average X =  0.97
average Y =  -1.59


number of steps = 1150
radial distance =  0.67
rms radial distance =  32.46
sqrt(N) =  33.91
average X =  -0.54
average Y =  -0.4


number of steps = 1450
radial distance =  3.85
rms radial distance =  37.63
sqrt(N) =  38.08
average X =  3.01
average Y =  2.39'''

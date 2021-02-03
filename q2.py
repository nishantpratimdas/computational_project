import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

analyticalValue = 12.5664

# function to calculate volume using monte carlo method


def monteCarlo(x1, x2, y1, y2, z1, z2, functionEllipsoid, N, analyticalValue):

    # volume of the cuboid enclosing the ellipsoid (it need not necessarily just enclose it)
    volumeCuboid = (x2 - x1)*(y2 - y1)*(z2 - z1)

    # array to store points which are inside the ellipsoid
    x = []
    y = []
    z = []

    volume = 0
    insideCount = 0

    for i in range(N):

        # randomly generate a point
        xRand = random.uniform(x1, x2)
        yRand = random.uniform(y1, y2)
        zRand = random.uniform(z1, z2)

        # if the point is inside the ellipsoid, store it in the arrays and increase counter by 1
        if (functionEllipsoid(xRand, yRand, zRand) <= 1):
            x.append(xRand)
            y.append(yRand)
            z.append(zRand)
            insideCount += 1

    # volume of the ellipsoid from the monte carlo idea
    volume = (volumeCuboid/float(N))*insideCount
    frac_err = abs(volume - analyticalValue)/analyticalValue

    return x, y, z, volume, frac_err


def functionEllipsoid(x, y, z):
    return ((x**2)/(1**2))+((y**2)/(1.5**2))+((z**2)/(2**2))


arrayVolume = []
arrayError = []
steps = []

print("{:<15}{:<20}".format("steps", "Volume of ellipsoid"))
N = 40000
i = 0

# loop to calculate volume and fractional error
while i < N:

    i += 200
    xDump, yDump, zDump, volume, FractionError = monteCarlo(
        -1, 1, -1.5, 1.5, -2, 2, functionEllipsoid, i, analyticalValue)

    steps.append(i)
    arrayVolume.append(volume)
    arrayError.append(FractionError)
    print("{:<15}{:<20}".format(i, round(volume, 2)))

print("\nvolume calculated from monte carlo (from final interation)= ",
      arrayVolume[-1])

# code for plots
plt.figure()
plt.plot(steps, arrayVolume)
plt.text(30000, 12.6, "Analytical value = 12.56637", size=16,
         va="baseline", ha="left", multialignment="left")
plt.axhline(12.5664, color='r')
plt.title("steps vs volume of ellipsoid")
plt.xlabel("steps")
plt.ylabel("Volume of ellipsoid")

plt.figure()
plt.plot(steps, arrayError)
plt.title("steps vs fractional error")
plt.xlabel("steps")
plt.ylabel("fractional error")

# For part D
x_plot, y_plot, z_plot, volume, fractionErrorDump = monteCarlo(
    -1, 1, -1.5, 1.5, -2, 2, functionEllipsoid, 40000, analyticalValue)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_plot, y_plot, z_plot)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

# output too long to attach
# volume calculated from monte carlo (from final interation)=  12.445199999999998

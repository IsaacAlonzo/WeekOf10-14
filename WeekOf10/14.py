# We are going to look at approximations of Pi
# as well as looking at the math Module

print(22/7)
print(355/113)

import math

print(9801 / (2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS =  oneHalfSideS * 2
    polygonCircumfernce = numSides * sideS
    pi = polygonCircumfernce / 2
    return pi

# returns gives you back an answer
print(archimedes(4))
print(archimedes(8))
print(archimedes(16))


for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# See the loop above. in addition to the value of pi print the difference
# between the values calculated bt the archimedes function by math.pi
# How many sides does it take to make the two close?

for sides in range(10, 360, 10):
    print(sides, archimedes(sides) - math.pi)

# Accumulators

acc = 0
for val in range(1, 6):
    acc = acc + val

print(acc)

# acc was 0 the added plus 1 then made acc = 1 and repeated process




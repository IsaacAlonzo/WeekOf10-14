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

# Compute the sum of the first 100 even numbers

acc = 0
for val in range(0, 201, 2):
    acc = acc + val
print(acc)
# Compute the sum of the first 50 odd numbers
acc = 0
for odd in range(1, 51, 2):
    acc = acc + odd
print(acc)

# Compute the average of the first 100 odd numbers
acc = 0
for odd in range(1, 200, 2):
    acc = acc + odd
print(acc/100)
# Write a function that returns the average of the first N numbers, where
#   N is a parameter
def averageofnumber(N):
    acc = 0
    for average in range(0, N, 1):
        acc = acc + average
    print(acc/N)
print(averageofnumber(50))


# Write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter
def product(N):
    acc = 0
    for product in range(0, N, 1):
        acc = acc * product
print(product(50))

product(50)
# Each number in the Fibonacci sequence is the sum of the previous two numbers.
#   The first two numbers in the sequence are 1 and 1.  Compute the 10th
#   Fibonacci number.
# Write a function to compute the Nth Fibonacci number, where N is a parameter.
#   You may assume that N will be greater than or equal to 3.
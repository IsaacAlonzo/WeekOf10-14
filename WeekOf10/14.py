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
averageofnumber(50)


# Write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter
def product(N):
    acc = 0
    for product in range(0, N, 1):
        acc = acc * product
    print(acc)
product(50)

# Each number in the Fibonacci sequence is the sum of the previous two numbers.
#   The first two numbers in the sequence are 1 and 1.  Compute the 10th
#   Fibonacci number.
acc = 0
for gold in range(1, 11):
    acc = acc + gold
print(acc)

# Write a function to compute the Nth Fibonacci number, where N is a parameter.
#   You may assume that N will be greater than or equal to 3.

def Fibon(N):
    acc = 0
    for Fibon in range(1, N):
        acc = acc + Fibon
    print(acc)

print(Fibon(11))

# not sure if right? I think it is wrong since it isn't adding the past 2 values

# v Was gone so I copied it off of repository.
# A Monte Carlo Simulation

# random numbers

import random

print(random.random())

# Boolean Expressions
# <, <=, >, >=, ==, !=
# Compound Boolean expressions
# and, or, not

dogWeight = 25
print(dogWeight < 25)
catWeight = 12
print(dogWeight > 25 or catWeight <= 10)
print(not catWeight <= 10)

# Decision making skills

alice = 20
bob = 15
carol = 25
ans = 0
if alice > 20:
    if bob < 50:
        ans = 150
    else:
        ans = 300
else:
    if carol > 500:
        ans = 200
    else:
        ans = 75
print(ans)

value = 75
if value > 100:
    print("bigger than 100")
elif value > 80:
    print("bigger than 80")
elif value > 45:
    print("bigger than 45")
else:
    print("not bigger than much")


def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        # ** = exponents

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi

print(montePi(10000))

import  turtle

def showMontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-2, -2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1, 0)
    inCircle = 0

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)
        t.goto(x, y)

        # ** = exponents

        if distance <= 1:
            inCircle = inCircle + 1
            t.color("green")
        else:
            t.color("black")

        t.dot()

    pi = inCircle / numDarts * 16
    scn.exitonclick()
    return pi
print(showMontePi(100))

# Assignment; Modify the simulation to plot points in the entire circle.
#    You will have to adjust teh calculated value for pi accordingly.

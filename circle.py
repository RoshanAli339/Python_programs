from swampy.TurtleWorld import *
import math

def circle(t, r, a):
    circumference = (2 * math.pi * r)
    n = int(circumference / 3) + 1
    len = circumference // n
    for i in range(a):
        fd(t, len)
        lt(bob, 1)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
r = int(input('Enter radius of arc: '))
a = int(input('Enter angle of arc: '))
circle(bob, r, a)

wait_for_user()
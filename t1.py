from swampy.TurtleWorld import *

def polygon(t, l, n):
    for i in range(n):
        fd (t, l)
        lt (t, (360//n))



world = TurtleWorld()
bob = Turtle()

len = int(input('Enter the length of polygon: '))
n = int(input('Enter the number of sides of the polygon: '))
polygon(bob, len, n)
wait_for_user()
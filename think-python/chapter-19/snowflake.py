def koch(turtle, n):
    if n<8:
        fd(turtle, n)
        return
    for angle in [-60, 120, -60, 0]:
        koch(turtle, n/3.0)
        rt(turtle, angle)

def snowflake(turtle):
    for i in range(3):
        koch(turtle, 300)
        rt(turtle, 120)

world.clear()
bob = Turtle()
bob.delay = 0
bob.pu()
bob.bk(150)
bob.lt()
bob.fd(90)
bob.rt()
bob.pd()
snowflake(bob)

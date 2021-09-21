import pixart
import turtle

def test_init():

    s=turtle.speed()
    assert(s==0)

    x=turtle.xcor()
    assert(x==-200)

    y=turtle.ycor()
    assert(y==0)


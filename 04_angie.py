import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("square")
    brad.color("blue")
    brad.speed(5)
    
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)    

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("green")
    angie.speed(10)
    
    angie.circle(100)

    
    window.exitonclick()

draw_square()

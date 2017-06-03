import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("square")
    brad.color("blue")
    brad.speed(10)
    
    brad.forward(200)
    brad.right(145)
    brad.forward(200)
    brad.right(145)
    brad.forward(200)
    brad.right(145)
    brad.forward(200)
    brad.right(145)    
    brad.forward(200)
    brad.right(145)

    
    window.exitonclick()

draw_square()

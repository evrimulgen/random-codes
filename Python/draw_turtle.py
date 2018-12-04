import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(8)
    counter = 0
    while counter < 36:
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(100)
        counter += 1

    window.exitonclick()

def draw_rectangle():
    window = turtle.Screen()
    window.bgcolor("green")

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color("white")
    brad.speed(15)
    counter = 0
    for i in range(36):
    	brad.begin_fill()
    	brad.forward(100)
    	brad.right(120)
    	brad.forward(100)
    	brad.right(120)
    	brad.forward(100)
    	brad.right(120)
    	# if i % 9 == 0:
    	# 	brad.end_fill()
    	brad.right(10)
        
    window.exitonclick()

def draw_triangle(side_length=5, depth=3):
    if depth == 0:
        return
    
    counter = 0
    while counter < 3:
        counter += 1
        brad.forward(side_length/2)
        if depth > 1:
            brad.left(120)
        draw_triangle(side_length/2, depth-1)
        brad.forward(side_length/2)
        
        brad.right(120)
        
    brad.left(240)

# if __name__ == "__main__":
#     window = turtle.Screen()
#     window.bgcolor("white")
    
#     brad = turtle.Turtle()
#     brad.shape("turtle")
#     brad.color("green", "green")
#     brad.speed(5)
    
#     brad.begin_fill()
#     brad.right(120)
#     brad.forward(128)
#     brad.left(120)
#     brad.forward(256)
#     brad.left(120)
#     brad.forward(256)
#     brad.left(120)
#     brad.forward(128)
#     brad.left(120)
#     brad.end_fill()
#     brad.color("green", "white")
#     brad.begin_fill()
#     draw_triangle(128, 3)
#     brad.end_fill()
    
#     window.exitonclick()

def shape(size=15, sides=8):
    j = 0
    import turtle
    window = turtle.Screen()
    window.bgcolor("black")

    turtle = turtle.Turtle()
    turtle.speed(0)
    turtle.color('yellow')
    turtle.shape("turtle")

    for i in range(1000):
        if i % 18 == 0:
            j += 1
            turtle.forward(size*6)
        # elif i % 20 == 0:
        #     turtle.right(360/size)
        #     turtle.forward(size + 10)


        turtle.left(i)
        for j in range(sides):
            turtle.forward(size)
            turtle.left(360/sides)

def race():
    import turtle
    window = turtle.Screen()
    window.bgcolor("yellow")

    turtle = turtle.Turtle()
    turtle.speed(0)
    turtle.color('purple')
    turtle.shape("turtle")
    square = turtle.Turtle()

def star():
    window = turtle.Screen()
    window.bgcolor("green")

    star = turtle.Turtle()
    star.speed(10)
    star.color('white')
    star.shape("turtle")
    #star.right(45)
    for i in range(200):
        # star.begin_fill()
    #while True:
        #star.left(90)
        #star.left(90)
        star.forward(75)
        star.right(90)
        star.forward(75)
        star.right(90)
        star.forward(25)
        star.right(90)
        star.forward(50)
        star.left(90)
        star.forward(50)
        star.left(90)
        if i % 4 == 0:
            star.forward(120)
            star.forward(100)
        if i % 8 == 0:
            star.right(120)
        # star.end_fill()
        # star.left(90)
        # star.forward(25)
        # star.left(90)
        # star.forward(50)
        # if i % 2 == 0:
        #     star.right(90)
        #     star.forward(25)
        # if i % 3 == 0:
        #     star.right(90)
        #     star.forward(75)
        # if i % 6 == 0 :
        #     star.forward(100)


        #star.right(10)
        
    turtle.done()
color = ["blue", "red", "orange", "yellow", "green", "pink", "purple"]

def tr():
    import random
    window = turtle.Screen()
    window.bgcolor("white")

    star = turtle.Turtle()
    star.speed(100)
    star.color('blue')
    star.shape("turtle")
    #star.right(45)
    for i in range(2000):
        if i % 10:
            star.color(random.choice(color))
        # star.begin_fill()
    #while True:
        #star.left(90)
        #star.left(90)
        star.forward(120)
        star.right(50)
        star.forward(90)
        star.right(90)
        star.forward(50)
        star.right(111)
        star.forward(50)
        star.right(103)
        star.forward(120)
        star.right(29)
        # if i % 11 == 0:
        #     star.left(90)
        #     star.forward(50)


if __name__ == "__main__":
    #race()
    #shape()
    while True:
        #draw_rectangle()
        #draw_square()
        #draw_triangle()
        star()
    #tr()
    #shape()
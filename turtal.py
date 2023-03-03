# import turtle
# turtle.bgcolor("black")
# turtle.speed(50)
# turtle.pensize(1)
# colors=("cyan","orange","white","dark green","blue")
# for i in range(200):
#     turtle.forward(i*4)
#     turtle.right(91)
#     turtle.color(colors[i%5])
    
#     for l in range(3):
#         turtle.forward(l*4)
#         turtle.right(91)

#         for k in range(2):
#             turtle.forward(k*4)
#             turtle.right(90)

#             for m in range(500):
#                 turtle.forward(m*4)
#                 turtle.right(600)

# import turtle

# turtle.bgcolor("black")
# turtle.speed(50)
# turtle.pensize(1)
# colors = ("cyan", "orange", "white", "dark green", "blue")

# for i in range(200):
#     turtle.pencolor(colors[i % 5])
#     turtle.circle(i)
# import turtle

# turtle.bgcolor("black")
# turtle.speed(50)
# turtle.pensize(1)
# colors=("cyan","orange","white","dark green","blue")

# for i in range(200):
#     turtle.color(colors[i%5])
#     turtle.circle(i, extent=360)
# import turtle

# turtle.bgcolor("black")
# turtle.speed(50)
# turtle.pensize(1)
# colors=("cyan","orange","white","dark green","blue")

# for i in range(200):
#     turtle.color(colors[i%5])
#     turtle.circle(i, extent=360)
import turtle

turtle.bgcolor("blue")
turtle.speed(50)
turtle.pensize(1)
colors=("cyan","orange","white","dark green","blue")

for i in range(200):
    turtle.forward(i)
    turtle.right(89)
    turtle.color(colors[i%5])

    for k in range(10):
        turtle.circle(k*5)
        turtle.right(20)

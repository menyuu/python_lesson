import turtle

# turtle.shape('turtle')
# turtle.color('red', 'yellow')
# turtle.begin_fill()
# for _ in range(100):
#     turtle.circle(100)
#     turtle.right(20)
# turtle.end_fill()
# turtle.done()

# turtle.color('red', 'yellow')
# turtle.begin_fill()
# for i in range(5 * 3):
#     turtle.forward(100 + i * 10)
#     turtle.right(360 / 5 * 2)
# turtle.end_fill()
# turtle.done()

# turtle.pencolor('green')
#
# for i in range(60):
#     turtle.fd(50)
#     turtle.left(360 / 3 + 10)
# # turtle.done()
#
# turtle.pencolor('red')
# for i in range(60):
#     turtle.fd(200)
#     turtle.left(360 / 3 + 10)
# turtle.done()

# for i in range(200):
#     turtle.fd(i)
#     turtle.left(360 / 4 + 10)
#
# turtle.done()

for i in range(200):
    if i % 2 == 0:
        turtle.pencolor('blue')
    else:
        turtle.pencolor('red')
    turtle.circle(i * 2)
    turtle.left(i * 3)
turtle.done()
import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.forward(100)

turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(45)
turtle_instance_2.forward(100)

turtle.done()
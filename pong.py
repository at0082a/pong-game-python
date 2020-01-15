import turtle
wn = turtle.Screen()
wn.title("Pong by AlexT03")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle a
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

#move paddle a up
def paddle_a_up():
  y= paddle_a.ycor()
  y += 20
  paddle_a.sety(y)

#move paddle a down
def paddle_a_down():
  y= paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)

#move paddle b up
def paddle_b_up():
  y= paddle_b.ycor()
  y += 20
  paddle_b.sety(y)

#move paddle b down
def paddle_b_down():
  y= paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "e")
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(paddle_b_down, "p")

while True:
  wn.update()
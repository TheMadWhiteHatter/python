
import turtle, random

colors  = ["red","green","blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from

turtle.width(10) #What does this line do?

length = 5

for count in range(100):
  color = random.choice(colors) #Choose a random color
  turtle.forward(length)
  turtle.right(135)
  turtle.color(color) # Why is color spelt like this?
  length = length + 5
  
import turtle 

painter = turtle.Turtle()

painter.pencolor("red")


ninja = turtle.Turtle()

ninja.speed(0)





for i in range(180):
    ninja.forward(100)
    ninja.right(10)
    ninja.forward(28)
    ninja.left(75)
    ninja.forward(55)
    ninja.right(75)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()

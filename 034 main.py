from random import randint
from tkinter import Canvas
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)

class GuiRect(Rectangle):
    def draw(self, canvas):
        myturtle.penup()
        myturtle.goto(self.point1.x, self.point1.y)
        myturtle.pendown()
        myturtle.forward(self.point2.x-self.point1.x)
        myturtle.left(90)
        myturtle.forward(self.point2.y-self.point1.y)
        myturtle.left(90)
        myturtle.forward(self.point2.x-self.point1.x)
        myturtle.left(90)
        myturtle.forward(self.point2.y-self.point1.y)

class GuiPoint(Point):
     def draw(self,canvas,size=10,color='red'):
         canvas.penup()
         canvas.goto(self.x,self.y)
         canvas.pendown()
         canvas.dot(size,color)
        
rectangle= GuiRect(Point(randint(0, 400), randint(0, 400)), Point(randint(0, 400), randint(0, 400)))


# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your area was off by: ", rectangle.area() - user_area)
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))


myturtle = turtle.Turtle()
rectangle.draw(canvas=turtle)
user_point.draw(canvas=turtle)
turtle.done()
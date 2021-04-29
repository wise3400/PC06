# -*- coding: utf-8 -*-

"""
Created on Fri Oct  9 12:02:31 2020
@author: Noah Hubbard and Wilson Seet

Description:
We created a simple click game that when you click on it,
you will need to match the bubble with the text that says
"Color" as many times as you can as it continues shrinking 
and dissapears. When the color matches to the bubble,
it will print that you have won. When it reaches the end
the game is finished...

"""
import turtle, random
w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners
turtle.listen() # for keyboard listening
# =========DEFINE VARIABLES BELOW=========
panel=turtle.Screen()
textturt = turtle.Turtle()
circleturt = turtle.Turtle()
style = ('Helvetica', 40)
size=20
running= True
colors= ["red","green","brown","pink","blue","orange"]
#======DEFINE FUNCTIONS===========
def func (x,y):

    global size, textcolor
    circleturt.color(random.choice(colors))
    circlecolor=circleturt.color()
    size -= 1
    circleturt.turtlesize(size)
    print(size)
    if size == 1:
      print("Game Finished!")
    if textcolor == circlecolor:
      print("You Won")

#======== DO SOME THINGS===========
textturt.up()
textturt.goto(0,200)
textturt.color(random.choice(colors))
textcolor=textturt.color()
textturt.write('Color', font=style, align='center')
textturt.hideturtle()

circleturt.up()
circleturt.turtlesize(size)
circleturt.color(random.choice(colors))
circleturt.shape("circle")
circleturt.goto(0,0)
circleturt.onclick(func)

panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.
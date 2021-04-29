"""
Created on Mon Oct  5 13:25:06 2020

@author: Dr. Z
@author: YOURNAME HERE

Start code for user interactions (Click game). 

                               STOP!             READ! 

                     THIS CODE IS DIFFERENT FROM OTHER START CODE!


This code is an EXAMPLE CODE which *MUST* be changed as you build your code.
This code demonstrates the expected organization, and gives you example functions
that animate a basic turtle. If you DO NOT change the code where indicated (MODIFY), 
                               YOU WILL LOSE POINTS.


1. Read the code THOROUGHLY (there's something new for everyone)
2. Run the code
3. Change where required FIRST then continue editing.

DESCRIBE YOUR CHANGES HERE
"""
import turtle, random 

turtle.tracer(0)
w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners
turtle.listen() # for keyboard listening

# =========DEFINE VARIABLES BELOW=========
panel=turtle.Screen()
running = True # for controlling the while loop

# this turtle is an example to demonstrate the functions below. You will likely
# have to DELETE OR MODIFY THIS TURTLE to get your game to work properly
testTudine = turtle.Turtle()

# =========DEFINE FUNCTIONS BELOW=========

# MODIFY - delete this comment block
# def replaceFunctionName(x,y):
#     '''This function is callback for a mouse click.'''
#     # add the code that you'd like to perform when clicking HERE
#     # if you want to do something at the location of the click, use the parameters x and y in your
#     # code wherever you need (ex: goto(x,y))
    
def byeTurt(x,y):
    '''Callback function to hide a SINGLE turtle when clicked. Takes x and y
    as parameters, which get values whenever the click happens.
    For deleting multiple turtles, see the listTurtles.example.'''
    testTudine.hideturtle() # MODIFY - you'll have to change this to your turtle's name.
    

# =========SET UP TURTLE(S) BELOW (color, size, shape, etc)=========

# INTERACTION FUNCTIONS BELOW 
# add onclick and onkey commands below. 

# notice that onclick is attached to the TURTLE, not the panel.
testTudine.onclick(byeTurt)


# =========ANIMATIONS BELOW=========
# code will execute in order within the loop
while running:
    
    #Your animation code goes here


    panel.update()


# =========LISTENERS & CLEANUP =========
panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.
"""
Created on Mon Oct  5 13:25:06 2020

@author: Dr. Z

Demonstrates how to animate multiple turtles in a list!
"""
import turtle, random 

# =========SETUP FOR LISTENERS=========
w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners
turtle.listen() # for keyboard listening

# =========DEFINE VARIABLES BELOW=========
panel=turtle.Screen()
running = True # for controlling the while loop
numTurt = 3


# Create an empty list. We'll add to this list in a for loop, using list functions
turtList = []

# STEP 1. Add turtles to your list using a for loop
for i in range(numTurt):
   turtList.append(turtle.Turtle()) # append adds a turtle to the end of the list.


# =========DEFINE FUNCTIONS BELOW=========


def delTurt(x,y):
    '''Callback function for onclick to delete the selected turtle''' 
    turt.hideturtle() # we can use variables that will come up later for callbacks ONLY
    
def randomMove(turtleName):
    '''This function, when called, moves the turtle entered in the command
    in a random path'''
    turtleName.seth(random.randint(-30,30)) 
    turtleName.forward(random.randint(-5,5))



# =========SET UP TURTLE(S) BELOW (color, size, shape, etc)=========

# STEP 2. Use a for loop to make changes to your turtles. Note how the loop is different from above!
# the function len gets the length of a list!
for i in range(len(turtList)):
    turtList[i].color('blue') # how would this line change if I want each turtle to be a diff color?
    turtList[i].up()
    turtList[i].goto(random.randint(-100,100),random.randint(-200,200))
    
    # we can add our click functions to each TURTLE as we make & modify them!
    turtList[i].onclick(delTurt)

# INTERACTION FUNCTIONS BELOW 


# =========ANIMATIONS BELOW=========
while running:

    # STEP 3. Use a for loop to apply the function to each turtle. Note how the loop is different AGAIN!
    for turt in turtList:
        randomMove(turt)

panel.mainloop() 
turtle.done() 
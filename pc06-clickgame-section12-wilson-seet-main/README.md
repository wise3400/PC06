[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=306465&assignment_repo_type=GroupAssignmentRepo)
# ClickGameRepo

Examples, snippets and start code for PC06!
<br>
<br>
In this start code repo, I've given you tools to accomplish your goals, regardless of the level of difficulty you're going after. <br>
<br>
* **bubbleStart.py** - This code is different from the start code we've used before. This code that can be run! Please take the time to read the description and comments BEFORE you run the code! You are REQUIRED to modify certain parts of this code or you'll lose points. Please note where these areas in the code are BEFORE starting to code.<br>
bubbleStart.py also shows you how you can create a turtle that _disappears when you click on it!_ 
Note: to do this, the onlcick() function is attached to  a TURTLE, not the SCREEN (panel). You use onclick with the object you want to give the click interaction to. For screen clicks: ```panel.onclick()```, but for turtle clicks: ```turtName.onclick()```.<br>
* **listTurtles.py** - This is an example script to show you how you can use <i> multiple turtles at once</i>! This is pretty advanced, and uses for loops and the new concept of list fuctions (```listname.append```) to add on elements to an empty list. Once you have turtles in a list, you can address them by the INDEX the same way you would a NAME. **For example:** ```myturt.color('red')``` will become ```turtList[idx].color('red')```. _Please read the comments carefully to understand how each use of the for loops changes with each activity._ We'll go over working with lists of turtles in class during Week 8 (Oct 12-16th).
<br>
<br>
<br>
**TIPS TO GET STARTED**

This is our first bigger project! :D
1. **Think about your game!** - Spend time _designing_ your game first. Consider the bubble movements, color schemes, and also the goal of the game. <b> Who is the game for? </b> Do you want high stress, high stakes? Then consider giving the bubble fast movements to challenge your player. Do you want something easy but satisfying? Then consider giving the bubble predictable movements. Do you want the user to click _in between_ a growing number of bubbles? Or click on a simple bubble and have it disappear? **Simple concepts are great!**
1. **Code the bubble movement first** - This is the easier of the new concepts for this assignment. So think of the bubble movement, talk with your partner, and then get that to work BEFORE ADDING ANYTHING ELSE.
1. **Code the click interaction outside of a function** - If you're struggling with functions, start here. Code the function task first, inside the while loop, so you can test to see if it does what you expect.
1. **Create the function and call it without the click<** - TEST your function by calling it. You may have to pass in "dummy arguments" so that your x, y or key parameters have some values and will run correctly. You may also first code your functions without parameters.
1. **Add the callback!** - Now that you have a function that does what you want and you've verified this, use the callback functions (onclick, onrelease, onkeypress) to get the mouse to click on it. Then run your code and test it out! <b>You may not see errors until you click!</b>

# Name: square_turtles.py
#
# Description:
#
# Draw 4 squares.
#
# Author: Rae Harbird
#
# Date: August 2018
#
# Here is a list of colours: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

from turtle import *

## Function to draw a square
# @param theTurtle a turtle object
# @param sideLength the side length of the square
#
def draw_square(theTurtle, sideLength) :
    
    for counter in range(4):
        theTurtle.fd(sideLength)
        theTurtle.lt(90)

## Create a turtle and set some attributes
#
# @pensize the turtle's pen size
# @penColor the pen color for the turtle
# @initialPosition a tuple representing the starting position for the turtle
# @return theTurtle a Turtle object
def setUpTurtle(penSize, penColor, initialPosition) :

    theTurtle = Turtle()
    theTurtle.pensize(penSize)
    theTurtle.pencolor(penColor)
    theTurtle.penup()
    theTurtle.setpos(initialPosition)
    theTurtle.pendown()
    
    return theTurtle

def main() :   
    # create biff the turtle
    biff = setUpTurtle(2, "red", (-225, 0) )

    # create chip the turtle      
    chip = setUpTurtle(4, "blue", (-150, 0))

    # make biff draw a square with a side length of 50 pixels
    draw_square(biff, 50)
    
    # make chip draw a square with a side length of 75 pixels
    draw_square(chip, 75)

    # leave the turtles on the screen until the user clicks in the screen
    exitonclick()    

if __name__ == '__main__':
    main()
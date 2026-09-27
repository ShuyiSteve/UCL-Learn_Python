# Name: pyramid.py
#
# Description:
#
# This program prompts the user for the height of a pyramid and prints it.
#
# Author: Rae Harbird
# This problem was created by Rob Miller, DIS, UCL for a Java course.
#
# Date: August 2018
#

MARGIN = 10


## Construct string representing a line of the pyramid
# @param    symbol the symbol from which the pyramid will be printed
# @param    lineNumber the lineNumber in the pyramid
# @param    height the height of the pyramid
# @return   line the string representing a line of the pyramid
# 
def pyramidLine(symbol, lineNumber, height) :
      line = ""
      line += spacesForPyramidLine(lineNumber, height)
      line += symbolsForPyramidLine(symbol, lineNumber)
      line += "\n"
      return line


## Construct string representing the symbols for a line of the pyramid
# @param    symbol the symbol from which the pyramid will be printed
# @param    lineNum the number of the line
# @return   lineSymbols the string representing the symbols in a line of the pyramid
# 
def symbolsForPyramidLine(symbol, lineNum) :
    lineSymbols = ""
    for symbolsCount in range((lineNum * 2) - 1) :
        lineSymbols += symbol
    return lineSymbols

 
## Construct string representing the spaces for a line of the pyramid
# @param    lineNum the number of the line
# @param    height the height of the pyramid
# @return   lineSpaces the string representing the spaces in a line of the pyramid
# 
def spacesForPyramidLine(lineNum, height) :
    lineSpaces = ""
    for spacesCount in range(MARGIN + height + 1 - lineNum) :
         lineSpaces += " "
    return lineSpaces
     
## Construct string representing the pyramid
# @param    character the symbol from which the pyramid will be printed
# @param    height the height of the pyramid
# @return the string representing the pyramid
#
def pyramidString(character, height) :
    pattern = "\n"
    for lineCount in range(height) :
        pattern += pyramidLine(character, lineCount, height)
    return pattern


def main() :
      height = int(input("\n\tEnter the number of lines for the pyramid: "))
      brickCharacter = input("\tEnter the character from which the pyramid should be made: ")
      print(brickCharacter)
      print(pyramidString(brickCharacter, height))


# Start the program
if __name__ == "__main__":
    main()
# Name: guess_two_numbers.py
#
# Description:
#
# This program prompts the user for two numbers and checks whether they match two
# randomly generated numbers
#
# Author: Rae Harbird
# This problem was created by Rob Miller, DIS, UCL for a Java course.
#
# Date: August 2018
#
import random

def main() :
    MIN = 1
    MAX = 3
    
    firstAnswer = random.randrange(MIN, MAX + 1)
    secondAnswer = random.randrange(MIN, MAX + 1)
    
    firstGuess = int(input("\n\tGuess the first number between {} and {}: ".format(MIN, MAX)))
    secondGuess = int(input("\n\tGuess the second number between {} and {}: ".format(MIN, MAX)))

    okSameOrder =  firstGuess == firstAnswer and secondGuess == secondAnswer
    okOtherOrder = firstGuess == secondAnswer and secondGuess == firstAnswer 

    if okSameOrder or okOtherOrder :
        print("\tCorrect - well done!\n")
    else :
        print("\tNo, the answers were {} and {}.\n".format(firstAnswer,secondAnswer))

# Start the program
if __name__ == "__main__":
    main()

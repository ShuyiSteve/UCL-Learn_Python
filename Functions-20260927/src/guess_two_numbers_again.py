# Name: guess_two_numbers_again.py
#
# Description:
#
# This program prompts the user for two numbers and checks whether they match two
# randomly generated numbers.
#
# Author: Rae Harbird
# This problem was created by Rob Miller, DIS, UCL for a Java course.
#
# Date: August 2018
#
import random

## Checks the two guesses entered by the user against the two randomly generated numbers.
# @params answerA the first answer
# @params answerB the second answer
# @params guessA the first guess
# @params guessB the second guess
# @return True or False
#
MIN = 1
MAX = 3

def guessesOk(answerA, answerB, guessA, guessB) :
    okSameOrder =  guessA == answerA and guessB == answerB
    okOtherOrder = guessA == answerB and guessB == answerA
    return okSameOrder or okOtherOrder
    

def main() :
    
    firstAnswer = random.randrange(MIN, MAX + 1)
    secondAnswer = random.randrange(MIN, MAX + 1)
    
    firstGuess = int(input("\n\tGuess the first number between {} and {}: ".format(MIN, MAX)))
    secondGuess = int(input("\n\tGuess the second number between {} and {}: ".format(MIN, MAX)))

    if guessesOk(firstAnswer, secondAnswer, firstGuess, secondGuess):
        print("\tCorrect - well done!\n")
    else:
        print("\tNo, the answers were {} and {}.\n".format(firstAnswer, secondAnswer))


# Start the program
if __name__ == "__main__":
    main()

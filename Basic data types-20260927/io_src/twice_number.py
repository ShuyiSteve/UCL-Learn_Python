# Name: twice_number.py
# Description:
#
# This program prompts the user to type in a number and prints the number and double the number. 
#
# Author: Rae Harbird
# This problem was created by Rob Miller, DIS, UCL for a Java course.
#
# Date: August 2018
#

def main():
    # Type your code in here
    num = int(input("Enter a value for \'number\': "))
    print(f"The value of \'number\' is {num}")
    print(f"The value of \'twice_number\' is {num * 2}")

if __name__ == "__main__":
    main()
# Name: age_calc.py
# Description:
#
# This program calculates how old someone will be in a given year,
#  after prompting for the current year and user's age. 
#
# Author: Rae Harbird
# This problem was created by Rob Miller, DIS, UCL for a Java course.
#
# Date: August 2018
#

def main():
    year_now = int(input("Enter the current year then press RETURN: "))
    age_now = int(input("Enter your current age in years: "))
    another_year = int(input("Enter the year in which you wish to know your age: "))
    another_age = another_year - (year_now - age_now)

    if another_age >= 0 and another_age <= 150:
        print("Your age in {0:d}: {1:d}".format(another_year, another_age))
    elif another_age < 0: 
        print(f"You weren't born in {year_now - age_now}. ")
    else: 
        print(f"Sorry, but you'll probably be dead by {another_year}!")
    
    


if __name__ == "__main__":
    main()
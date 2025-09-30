"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Generating random numbers and converting decimals to fractions

Assignment Information:
    Assignment:     7.2.2 Py1 Team 2
    Team ID:        LC5 - 06
    Author:         Milan Shah, shah1237@purdue.edu
    Date:           08/06/2025

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import random
from fractions import Fraction


def main():

    #set seed
    random.seed(int(input("Enter the seed: ")))

    #generate values for the four numbers
    first = round(random.uniform(0, 100), 3)
    second = round(random.uniform(10, 50), 3)
    third = round(random.uniform(20, 40), 3)
    fourth = round(random.uniform(100, 200), 3)

    #calculate decimal solution
    solOne = round(first + second + third + fourth, 3)

    #convert decimal numbers to fractions
    firstF = Fraction(first).limit_denominator()
    secondF = Fraction(second).limit_denominator()
    thirdF = Fraction(third).limit_denominator()
    fourthF = Fraction(fourth).limit_denominator()

    #calculate fractional solution
    solTwo = Fraction(first + second + third + fourth).limit_denominator()

    #print output
    print(f"First Random Number : {first}")
    print(f"Second Random Number : {second}")
    print(f"Third Random Number : {third}")
    print(f"Fourth Random Number : {fourth}")
    print(f"Sum from decimals: {first} + {second} + {third} + {fourth} = {solOne}")
    print(f"Sum from fractions: {firstF} + {secondF} + {thirdF} + {fourthF} = {solTwo}")
    


if __name__ == "__main__":
    main()

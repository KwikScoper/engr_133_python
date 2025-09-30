"""
Course Number: ENGR 13300
Semester: e.g. Fall 2025

Description:
    Practicing calculations with the math library.

Assignment Information:
    Assignment:     7.2.1 Py1 Team 1
    Team ID:        LC5 - 06
    Author:         Milan Shah, shah1237@purdue.edu
    Date:           09/05/2025

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

import math


def main():
    a, b, c = 20, 8, 9.81 #declaring and initializing variables a, b, c
    calc1 = a * math.cos(math.factorial(b)) #first calculation
    calc2 = (a**2 - (a * math.cos(b))**2) / (2 * c) #second calculation
    calc3 = (a * math.asin(1/2)) / c #third calculation

    #output block
    print(f"equation 1: {calc1:.4f}")
    print(f"equation 2: {calc2:.4f}")
    print(f"equation 3: {calc3:.4f}")

if __name__ == "__main__":
    main()

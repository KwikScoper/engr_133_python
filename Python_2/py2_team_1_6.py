"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Writing UDF to perform specific calculations

Assignment Information:
    Assignment:     8.1.2 Py2 Team 1
    Team ID:        Fall - 06
    Author:         Milan Shah, shah1237@purdue.edu
    Date:           09/13/2025

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

def calc_perform(a, b, c):
    #check a
    if a >= 5:
        #calculate solution if a >= 5
        sol =  (a**2 + math.cos(b) - math.log(c))/(b - a * c)
    else:
        #calculate other solution
        sol = (math.sqrt(a + b))/(c / a + math.sin(b))
    return sol


def main():
    #output
    a = float(input("Input a number for variable a (can be negative): ")) #take user input for a
    b, c = 104, 17 #define b and c
    output = round(calc_perform(a, b, c), 2)
    print(f"The result of the function was {output}")


if __name__ == "__main__":
    main()

"""
Course Number: ENGR 13300
Semester: e.g. Fall 2025

Description:
    This program calculates the equivalent capacitance of two capacitors given the first capacitance as user input and the second hardcoded.

Assignment Information:
    Assignment:     7.3.2 Py1 Ind 2
    Team ID:        LC5 - 06
    Author:         Milan Shah, shah1237@purdue.edu
    Date:           09/09/2025

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
    cap2 = math.e**3 * math.sqrt(5) #hardcoded capacitance 2
    cap1 = float(input("Input the capacitance of the first capacitor [μF]: ")) #user input for capacitance 1

    series = 1/(1/cap1 + 1/cap2) #calculating series capacitance
    parallel = cap1 + cap2 #calculating parallel capacitance

    #output block
    print(f"Type           First      Second      Total")
    print(f"Series{cap1:>11.1f} μF{cap2:>9.1f} μF{series:>9.1f} μF")
    print(f"Parallel{cap1:>9.1f} μF{cap2:>9.1f} μF{parallel:>9.1f} μF")

if __name__ == "__main__":
    main()
"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Iterating through a 2d matrix with for and while loops

Assignment Information:
    Assignment:     9.1.2 Py3 Pre 0
    Team ID:        LC5 - 06
    Author:         Milan Shah, shah1237@purdue.edu
    Date:           09/21/2025

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

import numpy as np


def main():
    #initialize array
    X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print("FOR loop:")

    #for loop
    for i, row in enumerate(X):
        for j, col in enumerate(row):
            print(f"X[{i},{j}] = {X[i, j]}")

    print("WHILE loop:")
    
    #while loop and while loop setup
    i = 0 #tracks the row
    while i < len(X):
        j = 0 #tracks the column
        while j < len(X[0]):
            print(f"X[{i},{j}] = {X[i, j]}")
            j += 1
        i += 1
        


if __name__ == "__main__":
    main()

"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Approximating e^x with Maclaurin series by specifying target error threshold

Assignment Information:
    Assignment:     9.2.3 Py3 Team 3 b
    Team ID:        LC5 - 06
    Author:         Milan Shah, shah1237@purdue.edu
    Date:           09/23/2025

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

from math import e

def my_factorial(n):
    if n < 0: #Returns error for negative n
        return -999
    result = 1 #init result value
    for i in range(2, n + 1): #iterates across all integers 1 -> n
        result *= i #Increment operator for multiplication
    return result


def main():
    x = float(input("Enter the value of x: "))
    target_error = float(input("Enter the target error threshold: "))
    actual = e**x
    approx = 0

    uplim = actual + (target_error / 100) * actual
    lowlim = actual - (target_error / 100) * actual
    
    count = 0
    while not(lowlim < approx < uplim):
        approx += (x**count)/(my_factorial(count))
        count += 1

    error = (approx - actual) / actual * 100

    print(f"Terms needed: {count}")
    print(f"Actual value: {actual:.2f}")
    print(f"Approximate value: {approx:.2f}")
    print(f"Target error threshold: {target_error:.1f}%")


if __name__ == "__main__":
    main()

"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    This program calculates the integral of sin(x)/x from a to b using a Maclaurin series. It takes in inputs of lower bound (a), upper bound (b), decimals to round to, and max terms to calculate. If the result converges to a value at a specified number of decimal places before the max term limit, the program ends early, and if it does not converge to said value by the max term limit, that is specified as well.

Assignment Information:
    Assignment:     9.3.2 Py3 Ind 2
    Team ID:        LC5 - 06
    Author:         Milan Shah, shah1237@purdue.edu
    Date:           09/24/2025

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

#Calculates a single term of the Maclaurin series
def calculate_term(a, b, n):
    return (((-1)**n) / ((2*n+1)*math.factorial(2*n+1))) * ((b**(2*n+1)) - (a**(2*n+1)))

#Calculates full series
def calculate_integral_series(a, b, decimals, max_terms):
    currsum = 0
    
    #Calculate first term
    currsum += calculate_term(a, b, 0)
    prevtwosum = round(currsum, decimals)
    print(f"n = 0: sum = {prevtwosum}")
    
    #Calculate second term
    currsum += calculate_term(a, b, 1)
    prevonesum = round(currsum, decimals)
    print(f"n = 1: sum = {prevonesum}")

    #Calculate third term
    currsum += calculate_term(a, b, 2)
    roundedcurr = round(currsum, decimals)
    print(f"n = 2: sum = {roundedcurr}")

    #Since first three terms are calculated, begin looping and calculate remaining
    for n in range(3, max_terms):
        if prevtwosum == prevonesum == roundedcurr:
            print(f"The integral from {a} to {b} is estimated to be {roundedcurr:.{decimals}f}.")
            print(f"Total number of terms: {n}")
            return
        
        prevtwosum = prevonesum #Update prevtwosum since the term has increased by 1
        prevonesum = roundedcurr #Update prevonesum since the term has increased by 1

        currsum += calculate_term(a, b, n) #Update currsum with new term
        roundedcurr = round(currsum, decimals)

        print(f"n = {n}: sum = {roundedcurr}")

            
    print(f"Error: The approximation did not converge to {decimals} decimal places with only {max_terms} terms.")

def main():
    a = float(input("Enter the lower limit of integration: "))
    b = float(input("Enter the upper limit of integration: "))
    decimals = int(input("Enter the number of decimal places for convergence: "))
    max_terms = int(input("Enter the maximum number of terms: "))

    #Check for invalid inputs
    if decimals <= 0 or max_terms <= 0:
        print("Error: Input a positive integer")
        return

    #Run actual integration sequence
    print("\nApproximations:")
    calculate_integral_series(a, b, decimals, max_terms)

if __name__ == "__main__":
    main()
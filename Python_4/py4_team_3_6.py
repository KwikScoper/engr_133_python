"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    This program reads a text file to organize data and do calculations of Beer's law, then outputs in a readable and understanable format

Assignment Information:
    Assignment:     10.2.3 Py4 Team 3
    Team ID:        LC5 - 06
    Author:         Milan Shah, shah1237@purdue.edu
    Date:           e.g. 01/23/2025

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


def absorb_calc(A, l, epsilon):
    concentration = A / (epsilon * l)
    return concentration

def main():
    #Initializing variables
    absorbencies = []
    
    # Read data from the input file
    with open('py4_task3_input.txt', 'r') as myfile:
        for line in myfile:
            # Split each line into a key and a value at the colon
            parts = line.strip().split(':', 1)

            key = parts[0].strip()
            value = parts[1].strip()

            # Assign values to the correct variables
            if key == "Name":
                substance_name = value
            elif key == "Path length":
                path_length = float(value)
            elif key == "Molar Extinction Coefficient":
                me_coeff = float(value)
            elif key == "Absorbancy":
                absorbencies.append(float(value))
    
    printstack = []
    printstack.append(f"The name of the substance is {substance_name}")
    for absorb_val in absorbencies:
        # Call the calculation function for each absorbency value
        concentration = absorb_calc(absorb_val, path_length, me_coeff)
        # Print the formatted output
        printstack.append(f"For {absorb_val} absorbency value, the concentration is {concentration:.7f}")

    line = 0
    while line < len(printstack):
        print(printstack[line])
        line += 1


if __name__ == "__main__":
    main()

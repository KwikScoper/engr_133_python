"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Reading and modifying csv data and plotting it with matplotlib

Assignment Information:
    Assignment:     10.1.2 Py4 Pre 0
    Team ID:        LC5 - 06
    Author:         Milan Shah, shah1237@purdue.edu
    Date:           09/27/2025

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

import os
import csv
import matplotlib.pyplot as plt

def main():
    with open('py4_pre_0_data.csv', 'r') as csvfile: # Starting reading of csv
        reader = csv.reader(csvfile)
        
        # Creating blank data arrays
        data = []

        x = []
        y = []

        for val in reader: # Adding csv data to the data array and also to the x and y arrays for graphing
            data.append([int(val[0]), int(val[1])])
            x.append(int(val[0]))
            y.append(int(val[1]) * 4)

        # Graphing stuffs
        plt.scatter(x, y)
        plt.title("Py4_Pre_0_data")
        plt.xlabel("Time (s)")
        plt.ylabel("Original Data * 4")
        plt.show()
    
    output = []
    for i in range(len(data)):
        output.append([x[i], y[i]])

    with open('py4_pre_0_shah1237.csv', 'w') as csvfile: # Starting writing of csv
        writer = csv.writer(csvfile)
        writer.writerows(output)

if __name__ == "__main__":
    main()
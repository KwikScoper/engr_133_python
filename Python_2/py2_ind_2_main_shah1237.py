"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     8.3.2 Py2 Ind 2 Main
    Team ID:        LC5 - 06
    Author:         Milan Shah, shah1237@purdue.edu
    Date:           09/15/2025

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

import py2_ind_2_functions_shah1237 as funcs

def main():
    func_name = input("Enter the name of the pool to calculate (Standard, Ramp, or Round): ") #input of function name

    if func_name in ("Standard", "Ramp", "Round"): #check for valid input
        l_one = int(input("Enter the surface length or radius. ")) #take l_one
        l_two = int(input("Enter the surface width or bottom radius. "))#take l_two
        ds = int(input("Enter the shallow end depth. "))#take ds
        dd = int(input("Enter the deep end depth. "))#take dd
    
        if func_name == "Standard": #check input and run standard if true
            funcs.standard(l_one, l_two, ds, dd)
        elif func_name == "Ramp": #check input and run ramp if true
            funcs.ramp(l_one, l_two, ds, dd)
        else: #run round since input isn't one of the other 2 options
            funcs.round(l_one, l_two, ds, dd)
    else:
        print("Please run the program again and enter a valid pool name.") #error handling


if __name__ == "__main__":
    main()

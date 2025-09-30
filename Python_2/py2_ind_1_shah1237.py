"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     8.3.1 Py2 Ind 1
    Team ID:        LC5 - 06
    Author:         Milan Shah, shah1237@purdue.edu
    Date:           09/09/2025

Contributors:
    Name, login@purdue [repeat for each]
    Alessandro Bonecchi, abonecch@purdue.edu
    

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

from sys import exit

def check_status(temp, pressure):
    crit_temp = 304.2
    crit_pressure = 73.8
    max_temp = 344.14
    max_pressure = 137
    safe_percent = .95

    uplim_temp = max_temp * safe_percent
    uplim_pressure = max_pressure * safe_percent

    #checking if temp & pressure are critical
    if (temp == crit_temp and pressure == crit_pressure):
        print("CO2 is at the critical point.")
        return None

    #checking temp
    if (temp < crit_temp):
        print("CO2 is below the critical temperature.")
        print(f"Increase the temperature by at least {(crit_temp - temp):.2f} Kelvin.") 
    elif(temp > uplim_temp):
        print("Warning! Reduce the temperature!")
        print(f"Decrease the temperature by at least {(temp - uplim_temp):.2f} Kelvin.")
    else:
        print("Temperature is within safe operating conditions.")

    #checking pressure
    if (pressure < crit_pressure):
        print("CO2 is below the critical pressure.")
        print(f"Increase the pressure by at least {(crit_pressure - pressure):.2f} bar.")
    elif (pressure > uplim_pressure):
        print("Warning! Reduce the pressure!")
        print(f"Decrease the pressure by at least {(pressure - uplim_pressure):.2f} bar.")
    else:
        print("Pressure is within safe operating conditions.")


def main():
    temp = float(input("Enter the temperature of carbon dioxide in Kelvin: "))
    if (temp < 0): #checking for invalid input
        print("Error: Please enter a valid temperature.")
        exit
    else:
        pressure = float(input("Enter the pressure of carbon dioxide in bar: "))
        if (pressure < 0): #checking for invalid input
            print("Error: Please enter a valid pressure.")
            exit
        else:
            check_status(temp, pressure)


if __name__ == "__main__":
    main()

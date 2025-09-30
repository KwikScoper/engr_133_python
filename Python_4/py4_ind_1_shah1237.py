"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    This program computes the average intensity of each channel in an image, and writes the results to a file.

Assignment Information:
    Assignment:     10.3.1 Py4 Ind 1
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
from PIL import Image
import numpy as np



def main():
    myfile = input("Image: ") # Get image filename

    img = Image.open(myfile)
    img_array = np.array(img)

    img_array = img_array / 255

    # Checking for grayscale
    if img_array.ndim == 3:
        reds = img_array[:, :, 0]
        greens = img_array[:, :, 1]
        blues = img_array[:, :, 2]

        # Remove gamma for RED
        mask_linear = reds <= 0.04045
        mask_power = reds > 0.04045
        reds[mask_linear] = reds[mask_linear] / 12.92
        reds[mask_power] = ((reds[mask_power] + 0.055) / 1.055) ** 2.4

        red_mean = reds.mean()
        
        # Remove gamma for GREEN
        mask_linear = greens <= 0.04045
        mask_power = greens > 0.04045
        greens[mask_linear] = greens[mask_linear] / 12.92
        greens[mask_power] = ((greens[mask_power] + 0.055) / 1.055) ** 2.4

        green_mean = greens.mean()
        
        # Remove gamma for BLUE
        mask_linear = blues <= 0.04045
        mask_power = blues > 0.04045
        blues[mask_linear] = blues[mask_linear] / 12.92
        blues[mask_power] = ((blues[mask_power] + 0.055) / 1.055) ** 2.4

        blue_mean = blues.mean()

    else:
        red_mean = 0
        green_mean = 0
        blue_mean = 0

    print(f"Red Channel Mean: {red_mean:.2f}")
    print(f"Green Channel Mean: {green_mean:.2f}")
    print(f"Blue Channel Mean: {blue_mean:.2f}")


if __name__ == "__main__":
    main()
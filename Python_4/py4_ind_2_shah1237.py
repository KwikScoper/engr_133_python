"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Calculates average luminance of selected image in images folder and dispalys the linearized image and histogram of relative channel intensities.

Assignment Information:
    Assignment:     10.3.2 Py4 Ind 2
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
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image

def main():
    while True:
        path = Path('images')
        suffixes = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp']
        #files = list(path.iterdir())
        files = [file for file in path.iterdir() if file.is_file() and file.suffix.lower() in suffixes]

        print("Available images:")
        for n, path in enumerate(files):
            print(f"{n + 1}. {path.name}")

        option = input("Select an image (q to quit): ")

        try:
            int(option)
            isInt = True
        except ValueError:
            isInt = False

        if option == "q":
            break

        try:
            choice = int(option)
            if 1 <= choice <= len(files):
                minipath = files[int(choice) - 1]
                img = Image.open(minipath)
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid choice, please try again.")
            continue

        img_array = np.array(img)

        try:
            img_array.dtype == np.uint8
        except ValueError:
            print("Image is not 8-bit.")

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

            luminance = 0.2126 * red_mean + 0.7152 * green_mean + 0.0722 * blue_mean

        else:
            grays = img_array

            mask_linear = grays <= 0.04045
            mask_power = grays > 0.04045
            grays[mask_linear] = grays[mask_linear] / 12.92
            grays[mask_power] = ((grays[mask_power] + 0.055) / 1.055) ** 2.4

            luminance = grays.mean()

        print(f"The average luminance of the image: {luminance:.3f}")
        
        fig, axes = plt.subplots(1, 2, figsize=(10, 5)) # 1 row, 2 columns

        print(img_array)

        if img_array.ndim == 2:
            axes[0].imshow(img_array, cmap='gray')
            axes[1].hist(img_array.flatten(), bins=256, color='gray', alpha=0.5)
            axes[1].set_title('Grayscale Intensity Histogram')
            
        else:
            axes[0].imshow(img_array)
            axes[1].hist(reds.flatten(), bins=256, color='red', alpha=0.5)
            axes[1].hist(greens.flatten(), bins=256, color='green', alpha=0.5)
            axes[1].hist(blues.flatten(), bins=256, color='blue', alpha=0.5)
            axes[1].set_title('RGB Intensity Histogram')
        
        axes[1].set_xlabel('Pixel Value (0-255)')
        axes[1].set_ylabel('Quantity')

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()
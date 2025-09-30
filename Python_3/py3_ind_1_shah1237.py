"""
Course Number: ENGR 13300
Semester: Fall 2025

Description:
    Given a feature name and genotype, this program returns the phenotype. Bioinformatics extra credit assignment

Assignment Information:
    Assignment:     9.3.3 Py3 Ind 1
    Team ID:        LC5 - 06
    Author:         Milan Shah, shah1237@purdue.edu
    Date:           09/29/2025

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

import csv
import numpy as np


def main():
    features = np.genfromtxt('list_of_features.csv', delimiter=',', dtype=str, skip_header=1) #import features
    pheno_map = {} #initialize hashmap for phenotypes

    curr_feature = ""
    for row in features: #fill hashmap
        feature_name = row[0]
        genotype = row[3]
        phenotype = row[5]

        if feature_name.strip():
            curr_feature = feature_name
            pheno_map[curr_feature] = {}

        pheno_map[curr_feature][genotype] = phenotype

    while True: #Made a loop so I can break out of the program during invalid inputs
        avail_features = list(pheno_map.keys()) #Available features are the keys in the hashmap
        print("AVAILABLE FEATURES:")
        for feature in avail_features:
            print(feature)
        
        selected_feature = input("Please select a feature: ") #User input
        if selected_feature not in avail_features:
            print("Invalid input.")
            break
        
        avail_genos = list(pheno_map[selected_feature].keys())
        print("POSSIBLE GENOTYPES:")
        for genotype in avail_genos:
            print(genotype)

        selected_geno = input("Please input the genotype: ") #User input
        if selected_geno not in avail_genos:
            print("Invalid input.")
            break

        chosen_pheno = pheno_map[selected_feature][selected_geno] #Chosen phenotype
        print(f"This corresponds to the physical attribute: {chosen_pheno}")
        break
    
    play_again = input("Would you like to run again? (y or n): ") #Run program again (probably not ideal bc recursive)
    if play_again == 'y':
        main()
        



if __name__ == "__main__":
    main()

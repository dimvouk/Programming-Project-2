import numpy as np
from roundGrade import roundGrade

def computeFinalGrades(grades):
    gradesFinal = np.zeros(grades.shape[0])
    #create a vector of zeros with size equal to the number of rows of matrix grades
    for i in range(grades.shape[0]):
        # run through rows 
        row = grades[i,:]
        if np.any(row == -3):
            # If there is a -3 grade, use -3 as the final grade
            gradesFinal[i] = -3
        elif len(row) == 1:
            # If only there is only one assignment, use it as the final grade
            gradesFinal[i] = grades[i]
        elif len(row) > 1:
            # If there are multiple assignments, drop the lowest grade and compute the mean of the rest
            if np.all(row == row[0]):
              gradesFinal[i] = row[0]
            else:
                # Sort the row in ascending order
                sorted_row = np.sort(row)
                # Remove the first occurrence of the minimum value
                min_val = sorted_row[0]
                min_index = np.where(row == min_val)[0][0]
                sorted_row = np.delete(sorted_row, 0)
                # Calculate the mean of the remaining values
                mean = np.mean(sorted_row)
                mean = np.array([mean])
                print(mean)
                # Round the final grade using the roundGrade function
                gradesFinal[i] = roundGrade(mean)
    return gradesFinal

#TESTING 

a =np.array([[7], [12], [-3]])

 
print(computeFinalGrades(a))
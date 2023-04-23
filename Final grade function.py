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
                row_without_min = row[row != np.nanmin(row)]
                mean = np.mean(row_without_min)
                mean = np.array([mean])
                # Round the final grade using the roundGrade function
                gradesFinal[i] = roundGrade(mean)
    return gradesFinal

#TESTING 

# a =np.array([[7, 10, 7, 4], [12, 10, 10, 10], [7, -3, 7, 7]])

 
# print(computeFinalGrades(a))
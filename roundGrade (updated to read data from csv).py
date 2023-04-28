import numpy as np

def roundGrade(grades): 
    #create an empty vector of zeros with same length as the input vector
    gradesRounded = np.zeros(len(grades))
    #run through array
    for i in range(len(grades)):
        if grades[i] > 11:
            gradesRounded[i] = 12
        elif grades[i] > 8.5:
            gradesRounded[i] = 10
        elif grades[i] > 5.5:
            gradesRounded[i] = 7
        elif grades[i] > 3:
            gradesRounded[i] = 4
        elif grades[i] > 1:
            gradesRounded[i] = 2
        elif grades[i] > -1.5:
            gradesRounded[i] = 0
        else:
            gradesRounded[i] = -3
    return gradesRounded
 
#Load data from csv as strings
data = np.loadtxt("gradesTest.csv", delimiter=";", dtype = str)

#Keep only grade values
grades = data[1:, 2:]

#Keep the shape of the grades array
shape = grades.shape

#Flatten the grades array to apply rounding
grades = grades.flatten()

#Turn the flattened array of strings into array of floats
grades = grades.astype(float)

#Apply rounding
grades_rounded = roundGrade(grades)

#Reshape the rouned flattened array to previous shape
grades_rounded = np.reshape(grades_rounded, (shape[0], shape[1]))

print(grades_rounded)

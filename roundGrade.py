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
 
print(roundGrade([11.1, 8.6,0,2.3,-1.4,-2.5,1.1,1.6,4.1,6.7]))

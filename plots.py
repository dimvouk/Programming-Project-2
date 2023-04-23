import numpy as np
import matplotlib.pyplot as plt


def gradesPlot(grades):

    # Load csv with rounded grades
    grades = np.loadtxt("gradesTest.csv", delimiter=";", skiprows=1, usecols=range(1,8))

    
    ## FIGURE 1: Final Grades
    
    # Find the number the occurences of each unique element
    elements, counts = np.unique(grades, return_counts=True)
    elements = elements.astype(int)

    # Convert unique elements to strings
    grades_str = list(map(str, elements))

    #Print the number of occurrences of each element
    #for element, count in zip(elements, counts):
        #   print(f"{element}: {count}")

    # Create a bar plot of the counts
    plt.bar(grades_str, counts, color = "seagreen", width = 0.5)

    # Set the labels for the x-axis and y-axis
    plt.xlabel("Grades")
    plt.ylabel("Occurrences")
    
    # Set the title of the plot
    plt.title("Final Grades")

    # Display the plot
    plt.show()
  
gradesPlot(grades)

## Τρέξε μέχρι εδώ για να βγει το 1ο Plot (που δεν είναι σωστό αλλα θα το αλλάξω)


    ## FIGURE 2: Grades per assignment    

    for i in grades[i]
        count = np.count_nonzero(grades[i] == elements[0])
        print(count)        
        
    for i in range(grades.shape[0]):
        count = np.count_nonzero(grades[i] == elements[0])
        print("Row {}: {} occurrences".format(i, count))
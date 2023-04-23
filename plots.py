import numpy as np
import matplotlib.pyplot as plt


def gradesPlot(grades):

    # Load csv with rounded grades
    data = np.loadtxt("gradesTest.csv", delimiter=";", dtype = str)
    grades = data[1:, 1:]
    
    
    ## FIGURE 1: Final Grades
    
    # Find the number the occurences of each unique element
    elements, counts = np.unique(grades, return_counts=True)

    # Turn unique elements to floats
    elements_floats = list(map(float, elements))
    
    # Sort unique elements
    elements_floats = np.sort(elements_floats)
    
    #Turn unique elements back to strings
    elements = list(map(int, elements_floats))
    elements = list(map(str, elements))
    

    # Create a bar plot 1. Final Grades
    plt.bar(elements, counts, color = "seagreen", width = 0.5)

    # Set the labels for the x-axis and y-axis
    plt.xlabel("Grades")
    plt.ylabel("Occurrences")
    
    # Set the title of the plot
    plt.title("Final Grades")

    # Display the plot
    plt.show()

gradesPlot(grades)

    ## FIGURE 2: Grades per assignment
        
    # Load csv with grades
    # data = np.loadtxt("gradesTest.csv", delimiter=";", dtype = str)
    assignments = data[0, 1:]
    
    # convert the grades to integers
    grades = grades.astype(int)
    
    noise_x = np.random.uniform(low=-0.1, high=0.1, size=(len(grades), len(grades[0])))
    noise_y = np.random.uniform(low=-0.1, high=0.1, size=(len(assignments)))
    
   
    
    # Create plot 2. Grades per assignment
    x = assignments
    y = grades + noise_x
    
    #plot the grades as dots with unique colors for each row
    fig, ax = plt.subplots()
    ax.scatter(x, y, c=colors, cmap='jet')
    
    plt.xticks(ticks = (range(0, len(assignments))), labels = assignments, rotation = 60)
    plt.yticks(ticks = (range(0, len(elements))), labels = elements)
    plt.show()
    
    return gradesPlot(grades)




import numpy as np
import matplotlib.pyplot as plt

# define the assignments and grades arrays
assignments = np.array(['Assignment 1', 'Assignment 2', 'Assignment 3', 'Assignment 4', 'Assignment 5', 'Assignment 7', 'Assignment 8'])
grades = np.array([['-3', '7', '4', '2', '12', '12', '4'],
                   ['7', '0', '-3', '0', '10', '0', '4'],
                   ['12', '4', '2', '7', '7', '4', '12'],
                   ['7', '0', '7', '10', '4', '-3', '12'],
                   ['7', '-3', '12', '12', '4', '4', '7'],
                   ['0', '2', '4', '0', '2', '12', '0'],
                   ['0', '12', '0', '2', '4', '0', '7'],
                   ['0', '-3', '12', '4', '-3', '10', '12'],
                   ['7', '4', '2', '10', '10', '-3', '0']], dtype=int)

# convert the grades to integers
grades = grades.astype(int)

# assign a unique color to each row of the grades array
colors = np.linspace(0, 1, len(grades))
colors = np.repeat(colors[:, np.newaxis], len(assignments), axis=1)

# add a small random number to the x- and y-coordinates of each dot
x = np.tile(np.arange(1, len(assignments) + 1), (len(grades), 1)).flatten() + np.random.uniform(-0.1, 0.1, len(assignments) * len(grades))
y = grades.flatten() + np.random.uniform(-0.1, 0.1, len(assignments) * len(grades))

# plot the grades as dots with unique colors for each row
fig, ax = plt.subplots()
ax.scatter(x, y, c=colors, cmap='jet')

# plot the average grades as a line with a black color
avg_grades = np.mean(grades, axis=0)
ax.plot(np.arange(1, len(assignments) + 1), avg_grades, 'k-')

# set the x- and y-axis limits and labels
ax.set_xlim(0.5, len(assignments) + 0.5)
ax.set_ylim(-3.5, 12.5)
ax.set_xticks(np.arange(1, len(assignments) + 1))
ax.set_xticklabels(assignments, rotation=45, ha='right')
ax.set_xlabel('Assignments')
ax.set_ylabel('Grades')

# show the plot
plt.show()


import os.path
import csv
import numpy as np 

# Ask user for the name of the CSV file
file_name = input("Please enter the name of the CSV file: ")


# Check if the file exists
if not  os.path.exists(file_name):
        print("File not found.")
    
#Load data from csv as strings
data = np.loadtxt("gradesTest.csv", delimiter=";", dtype = str)

#Keep only grade values
grades = data[1:, 2:]

#Keep the shape of the grades array
shape = grades.shape

#Print the number of students and assignments

num_students=shape[0]
num_ass=shape[1]
print("The number of students is:", num_students)
print("The number of assignments is:", num_ass)

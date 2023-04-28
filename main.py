import os.path
import csv
import numpy as np 

# Ask user for the name of the CSV file
file_name = input("Please enter the name of the CSV file: ")


# Check if the file exists
if not  os.path.exists(file_name):
        print("File not found.")
    
#Load data from csv as strings
data = np.loadtxt(file_name, delimiter=";", dtype = str)

#Keep only grade values
grades = data[1:, 2:]

#Keep the shape of the grades array
shape = grades.shape

#Print the number of students and assignments

num_students=shape[0]
num_ass=shape[1]
print("The number of students is:", num_students)
print("The number of assignments is:", num_ass)





menuItems = np.array(["Load data", "Check for data errors", "Generate plots", "Display list of grades","Quit"])

# Start of UI
Script_bool = True
while Script_bool == True:
    # Display menu options and ask user to choose a menu item
    option = input(f"Choose one option\n1-Load data \n2-Check for data errors \n3-Generate plots \n4-Display list of grades \n5-Quit \nType the number of your option\n-->")
    if option.isdigit() and int(option) in range(1, 6):
        # Convert the user input to integer and get the corresponding menu item
        option = menuItems[int(option) - 1]
    if option in menuItems:
        # 1. Load data
       if option == menuItems[0]:
           max_attempts = 3
           for attempt in range(max_attempts):
               file_name = input("Please enter the file name: ")
               if not os.path.exists(file_name):
                   print("File not found.")
               else:
                    try:
                        data = np.loadtxt(file_name, delimiter=";", dtype=str)
                        #Keep only grade values
                        grades = data[1:, 2:]

                        #Keep the shape of the grades array
                        shape = grades.shape
                        break  # Exit the for loop if a valid filename is entered
                    except FileNotFoundError:
                           print("File not found. Please try again.")
               if attempt == max_attempts - 1:
                    print(f"Maximum attempts ({max_attempts}) reached. Exiting...")
                    break  # Exit the for loop if the maximum number of attempts is reached
        # 2.Check for data errors
       if option == menuItems[1]:
                        
            #Keep the students Id in an array
            studentsid=data[1:,:1]
            
            # Check if there are repeated elements
            unique_arr = np.unique(studentsid)
            if unique_arr.size < studentsid.size: 
                print("There is an error. Some students have the same ID.")
            else:
                print("No errors appeared")
                
            # Check if the grades are on the right scale 
            gradesscale = np.array(['-3', '0', '2', '4', '7', '10', '12'])
            error = True
            
            for i in range(shape[0]):
                for j in range(shape[1]):
                    if grades[i,j] not in gradesscale:
                        print(f"There is an error. The grade {grades[i,j]} is not on the 7-step-scale.")
                        error = False
               
            if error == True :
                print("All  grades are on the right scale")
            
            

            
            
            
            
    else: 
      print("Spelling wrong")
        

"""
Start
create a list storing 5 numbers
capture 5 of the inputs
each input appends the list
sort list into ascending order, splice items starting at index 2
3 highest numbers are summed up and divided by 3
output message to user
end

"""

"""
create list

capture input
append number to list

capture input
append number to list 

capture input
append number to list 

capture input
append number to list 

capture input
append number to list 

print
"""

grades = []

grade = input("Enter the 1st Grade: ")
grades.append(float(grade))

grade = input("Enter the 2nd Grade: ")
grades.append(float(grade))

grade = input("Enter the 3rd Grade: ")
grades.append(float(grade))

grade = input("Enter the 4th Grade: ")
grades.append(float(grade))

grade = input("Enter the 5th Grade: ")
grades.append(float(grade))

grades.sort()

grades=grades[2:]

grades = sum(grades)

result = grades / 3

print ("Average Grade  {0:.2f}%".format(result))

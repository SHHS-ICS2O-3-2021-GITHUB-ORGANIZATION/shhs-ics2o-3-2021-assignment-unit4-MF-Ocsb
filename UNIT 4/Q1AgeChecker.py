# NAME OF AUTHOR: Matthew F
# NAME OF THE PROGRAM:  Q1 Age Checker
# DATE OF CREATION: 01/24/2022
# PURPOSE OF PROGRAM: Determine school level from age

# VARIABLE DEFINITION
age = 0
school = 'n'

# INPUT
age = int(input("Please enter your age to determine your school level: "))

# PROCESSING
# Group different school ages to set the variable
if (age > 5) & (age <= 11):
    school = 'elementary'
if (age > 11) & (age <= 14):
    school = 'middle'
if (age > 14) & (age < 19):
    school = 'high'
if age >= 19:
    school = 'job'

# OUTPUT
# Use the previously established variable and group other ages for unique responses
if (age > 5) & (age < 19):
    print(("You are in ") + school + (" school"))
elif (age >= 19) & (age < 80):
    print("You are working.")
elif (age < 122) & (age >= 80):
    print("You are retired")
elif age >= 122:
    print("You are not alive")
else:
    print("You are not in school.")

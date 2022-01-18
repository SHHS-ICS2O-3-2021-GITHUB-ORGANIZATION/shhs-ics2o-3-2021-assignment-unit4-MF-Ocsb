# NAME OF AUTHOR: Matthew F
# NAME OF THE PROGRAM:  Q1 Counting
# DATE OF CREATION: 01/18/2022
# PURPOSE OF PROGRAM: Count up to number given

# VARIABLE DEFINITION
ans = 0
given = 0

# INPUT
print("Enter a number")
given = int(input())

# PROCESSING
while ans != given:
  ans = 1 + ans
  print(ans)
input()
while ans != 0:
  ans = ans - 1
  print(ans)

# OUTPUT
print("Complete")

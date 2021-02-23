"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  Computes wha

Author: Khatchadourian.N

Created:  23/02/2021
------------------------------------------------------------------------------
"""
print("******* Triangle Detector ********")

#Gets the side lengths from the user
first_side = int(input("Enter the length of the first side: "))
second_side = int(input("Enter the length of the second side: "))
third_side = int(input("Enter the length of the third side: "))

#Checks which side is the biggest then checks if two sides add up to be greater than the side that is the biggest
if third_side > first_side and second_side:
  if first_side + second_side > third_side:
    print("This is a triangle")
  else:
    print("This is not a triangle")

elif second_side > first_side and third_side:
  if first_side + third_side > second_side:
    print("This is a triangle")
  else:
    print("This is not a triangle")

elif first_side > second_side and third_side:
  if second_side + third_side > first_side:
    print("This is a triangle")
  else:
    print("This is not a triangle")

#If none meet the criteria then it's definitely not a triangle
else:
  print("This is not a triangle")
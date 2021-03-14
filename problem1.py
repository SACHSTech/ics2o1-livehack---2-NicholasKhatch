"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  Computes what life form a Mars rover saw

Author: Khatchadourian.N

Created:  23/02/2021
------------------------------------------------------------------------------
"""
print("******* Life Form Detector ********")

#Input from the user of what features the rover saw saw
antenna_amount = int(input("How many antennas did the martian have? "))
eye_amount = int(input("How many eyes did the martian have? "))

#Uses criteria to determine what life form was seen based on the amounts of antennas and eyes
if antenna_amount >= 3 and eye_amount <= 4:
  print("Life form detected: AudreyMartian")
elif antenna_amount == 0 and eye_amount == 2:
  print("Life form detected: MattDamonMartian, MaxMartian, BrooklynMartian")
elif antenna_amount <= 6 and eye_amount >= 2:
  print("Life form detected: MaxMartian")
elif antenna_amount <= 2 and eye_amount <= 3:
  print("Life form detected: BrooklynMartian")
else:
  print("No life form detected")
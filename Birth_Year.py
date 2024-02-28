#Create a variable that stores the user's birth year.
birth_year = int(input("What year were you born? (YYYY) "))

#Use if-else statements to determine the user's generation.
if birth_year >= 2013:
  print("You are a member of Generation Alpha.")
elif birth_year >= 1997:
  print("You are a member of Generation Z.")
elif birth_year >= 1981:
  print("You are a millennial.")
elif birth_year >= 1965:
  print("You are a member of Generation X.")
elif birth_year >= 1946:
  print("You are a baby boomer.")

#if the user enters anything that does not fall within this range, 
#respond: "Error. Please enter a four-digit year, 1946 or later."
else:
  print("Error. Please enter a four-digit year, 1946 or later.")

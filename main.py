import car 
from userdata import user1 


# Create a Identity Check or fill up form to rent a car 

# We need to use my flowchart first a simple car rental 

# First Log in a user 

question_log = input("Do you want to login? (y/n): ")

if question_log == "y" or question_log == "Y" :
  print("Continue")
elif question_log == "n" or question_log == "N": 
  print("Thank you for visiting")
  exit()
else: 
  print(f"Your input is not available: {question_log}")
  
  


user_log = input("Input your username: ")

# Create a while loop for inputting username

while not user_log :
  user_log = input("Input your username: ")


if user_log in user1["username"] : 
  print("Hello?")
else : 
  print("Who are you?")
  exit()

user_pass = input("Enter your password: ") 
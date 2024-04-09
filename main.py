import car 
import userdata 


# Create a Identity Check or fill up form to rent a car 

# We need to use my flowchart first a simple car rental 

# First Log in a user 



user_log = input("Input your username: ")

# Create a while loop for inputting username

while not user_log :
  user_log = input("Input your username: ")


user1 = userdata.user1

if user_log in user1["username"] : 
  print("Who are you?")


user_pass = input("Enter your password: ") 
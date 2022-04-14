str(input("What is your problem? "))
user_response = str(input("Have you had this problem before (yes or no)? "))
if user_response.upper() == "YES":
    print("Well, you have it again!")
elif user_response.upper() == "NO":
    print("Well , you have it now!")
else:
    print("I don't get what you are talking about!")

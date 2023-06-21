theater_name = "XYZ"
rated_r_age_limit = 17

print(f"Welcome to {theater_name} theater!!!")

user_input = int(input("Enter your ege: "))
print(f"User input is: {user_input}")

if user_input >= rated_r_age_limit:
    print("Enjoy the movie")
else:
    adult_present = int(input("Is another adult with you? yes or no").lower())
    if adult_present == "yes":
        print("Enjoy the movie")
    else:
        print("Your must be 17 to watch the movie")
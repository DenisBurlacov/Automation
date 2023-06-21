theater_name = "XYZ"
rated_r_age_limit = 17

print(f"Welcome to {theater_name} theater!!!")

user_input = int(input("Enter your ege: "))
print(f"User input is: {user_input}")

if user_input >= rated_r_age_limit:
    print("Enjoy the movie")
else:
    print("You must be 17 to watch a movie")
current_users = ['Dumac', "April", "Hendy", "Andy", "Maxwell"]
new_users = ["April", "dumac", "Philips", "Felix", "Rahman"]

curr_users_lower = [xy.lower() for xy in current_users]

for new_user in new_users:
    if new_user.lower() in curr_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")

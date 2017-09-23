users = []
if users:
    for users in users:
        if users == "admin":
            print("hello admin,would you like to see some status report?")
        else:
            print("hello "+users+" thanks for logging in again")
else:
    print("we need to find some users!")
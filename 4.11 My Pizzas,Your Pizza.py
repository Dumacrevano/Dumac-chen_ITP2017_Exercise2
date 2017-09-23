pizza=["peperoni pizza", "carbonara pizza","seafood pizza"]
friend_pizza=["peperoni pizza", "carbonara pizza","seafood pizza"]
pizza=friend_pizza[:]
pizza.append("Hawaian Pizza")
friend_pizza.append("Vegetarian Pizza")
print("my favourite pizza are:")
for pizza in pizza:
    print(pizza)
print("\nmy friend's favourite pizza are:")
for pizza in friend_pizza:
    print(pizza)


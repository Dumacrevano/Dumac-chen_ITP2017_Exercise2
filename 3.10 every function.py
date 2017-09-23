list=["Indonesia","singapore","Thailand","Kamboja"]
print(list[1])
print(list[-2])
list[1]="Vietnam"
list.append("Laos")
list.insert(0,"Malaysia")
del list[3]
winner=list.pop()
print("the winner is "+winner)
list.remove("Malaysia")
print(list)
print(sorted(list,reverse=True))
list.sort()
print(list)
list.reverse()
print(list)

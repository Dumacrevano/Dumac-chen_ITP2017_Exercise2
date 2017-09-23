guest=["suri","Hendy","Andy"]
message="please! come to my dinner party tonight, "
print(message+guest[0])
print(message+guest[1])
print(message+guest[2])
print(guest[2]+" cannot come to the party")
guest[2]="Happy"
print(message+guest[0])
print(message+guest[1])
print(message+guest[2])
guest.insert(0,"Siriwan")
guest.insert(1,"Darwin")
guest.append("Dilon")
print(message+guest[0])
print(message+guest[1])
print(message+guest[2])
print(message+guest[3])#invited guest
print(message+guest[4])
print(message+guest[5])
print("sorry i can only invite two people")#invited after decreased
guest.pop(0)
guest.pop(1)
guest.pop(3)
guest.pop(2)
print(message+guest[0])
print(message+guest[1])
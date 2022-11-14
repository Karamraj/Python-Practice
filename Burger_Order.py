print("Welcome To Our Burger Shop!")
size = input("What size of burger do you want? M, N or L")
add_mushroom = input("Do you want mushroom? Y or N")
extra_cheese = input("Do you want to add cheese? Y or N")

bill = 0
if size=="M":
    bill = bill+5
elif size=="N":
    bill = bill+8
else:
    bill = bill+10

if add_mushroom == "Y":
    if size=="L":
        bill += 2
    else:
        bill += 1

if extra_cheese == "Y":
    bill += 1

print("Your final bill is: {}".format(bill))
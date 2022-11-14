from re import U


print("Welcome To Love Calculator!")
name1 = input("Enter First Name: ")
name2 = input("Enter Second Name: ")
combined_name = name1+name2
lower_case_name = combined_name.lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))


if love_score < 10 or love_score > 85:
    print("Your love score is {}, you go together like coke and mentos.".format(love_score))
elif love_score >= 40 and love_score <=70:
    print("Your love score is {}, you are alright together.".format(love_score))
else:
    print("Your Love score is: {}".format(love_score))
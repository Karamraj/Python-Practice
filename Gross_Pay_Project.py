hour = input("Enter The No. Of Hours: ")
rate = input("Enter Rate: ")
hour = float(hour)
rate = float(rate)

if hour < 40:
    pay = round(hour*rate,2)
else:
    overtime = hour - 40
    pay = round(40 * rate + overtime * rate * 1.5,2)
print("Pay: {}".format(pay))
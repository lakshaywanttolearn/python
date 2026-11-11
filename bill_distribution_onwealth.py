n1 = eval(input("enter the unit consume for electricity "))
if n1<=200:
    print("NO amount is to be paid")
elif 200<n1<=400:
    amt = n1*4
    print("amount paid to be ",amt)
elif 400<n1<=600:
    amt = n1*6
    print("amount paid to be ",amt)
else:
    amt = n1*8
    print("amount paid to be ",amt)

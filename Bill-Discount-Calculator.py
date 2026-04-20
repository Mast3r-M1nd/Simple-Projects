bill = float(input("enter bill price: "))
if bill <= 0:
    print("then why are you here?")
elif bill >= 100:
    print("you get a 20% discount!")
    print("your total is " ,bill*0.8)
elif bill >= 50:
    print("you get a 10% discount!")
    print("your total is ",bill*0.9)
elif bill < 50:
    print("your total is " ,bill)
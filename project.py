money = 50000
pin = 9090
print("Default pin is 9090")
while(True):
    print("\n \n")
    print("Welcome Mr. John")
    print("1 for Balance Inquiry\n2 for Fast Cash\n3 for Cash Deposit\n4 for Cash Withdrawn\n5 for money transfer\n6 for Pin Change")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Enter your Pin")
        Balance_pin=int(input("Enter here: "))
        if Balance_pin==pin:
            print("The available balance is:",money)
        else:
            print("Wrong pin")
    elif choice==2:
        print("do you want to withdrawn 5000\npress 0 for Yes\npress 1 for No")
        fast_cash_chioce=int(input("Enter here: "))
        if fast_cash_chioce==0:
            fast_cash_pin=int(input("Enter the pin here: "))
            if fast_cash_pin==pin:
                money=money-5000
                print("The available balance is:",money)
            else:
                print("Wrong pin")
        elif fast_cash_chioce==1:
            print("Thank you for using our services")
        else:
            print("please press correct option")
    elif choice==3:
        print("Enter amount to Deposit")
        amount=int(input("Enter here: "))
        print("Enter the Pin")
        amount_pin=int(input("Enter here: "))
        if amount_pin==pin:
            money=money+amount
            print("The available balance is:",money)
        
        else:
            print("Wrong Pin")
    elif choice==4:
        print("Enter amount to Withdrawn")
        amount=int(input("Enter here: "))
        print("Enter the Pin")
        amount_pin=int(input("Enter here: "))
        if amount_pin==pin:
            if amount<=money:
                money=money-amount
                print("The available balance is:",money)

            else:
                print("Insufficient Balance")
        else:
            print("Wrong Pin")
    elif choice==5:
        print("This service is not available yet")
    elif choice==6:
        print("Enter your current Pin")
        choice_pin = int(input("Enter here: "))
        if choice_pin==pin:
            print("Enter your new Pin")
            new_pin=int(input("Enter here: "))
            pin = new_pin
            print("Your pin has succesfully changed")
        else:
            print("Wrong pin")
    else:
        print("Please Enter correct Option")
    continue
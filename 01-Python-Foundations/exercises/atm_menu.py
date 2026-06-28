balance = 1000 
while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice:(1-4) "))
    if choice==1: 
        print("Your current balance is: ",balance)
    elif choice==2:
        amount = float(input("Enter amount you want to deposit: "))
        balance+= amount
        print("Amount deposited successfully! ")
        print("New balance is: ", balance)
    elif choice==3:
        amount = float(input("Enter the amount you want to withdraw: "))
        if amount<=balance:
            balance-=amount
            print("Amount withdraw successfully! ")
        else:
            print("Insufficient balance. ")
    elif choice ==4:
        print("Thank you for using this ATM! ")
    else: 
        print("Invalid Choice, please enter a number between 1 and 4 ")

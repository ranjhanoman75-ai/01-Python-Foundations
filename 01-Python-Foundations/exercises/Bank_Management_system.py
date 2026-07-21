print("============Bank Management System========")
import logging
import logging_config
class Bank:
    def __init__(self,account_no,holder_name,balance):
        self.__account_no = account_no
        self.__holder_name = holder_name
        self.__balance = balance
    def deposit(self,amount):
        print("Your balance before deposit is: ",self.__balance)
        if amount>0:
            self.__balance +=amount
            print("Amount deposited successfully")
            logging.info(
    "Amount deposited successfully: %.2f. Your balance is now: %.2f",
    amount,
    self.__balance
)
            print("Your balance after deposit is: ",self.__balance)
        else:
            print("Invalid amount")
            logging.error("Wrong amount : {amount} must be positive {balance}")
    def withdraw(self,amount):
        print("Your current balance is: ",self.__balance)
        if amount<= self.__balance:
            self.__balance -=amount
            print("Amount withdraw successfully")
            logging.info("Amount : %2f withdrawn successfully. ")
            print("Your balance after withdraw is: ",self.__balance)
        else:
            print("Invalid inputs")
            logging.error("Invalid amount: %.2f.available balance: %2f", amount,self.__balance)
    def check_balance(self):
        logging.info("Your balance is: %2f ",self.__balance)
        return self.__balance
    def display_info(self):
        print("Account Number:", self.__account_no)
        print("Holder Name:", self.__holder_name)
        print("Balance:", self.__balance)
        logging.info("Acount Number is: '{account_no}' added")
bank = Bank(123456, "John Doe", 1000)

while True:
    print("1: Check balance")
    print("2: Deposit")
    print("3: Withdraw")
    print("4:Display Info ")
    print("5: Exit Program")

    choice = int(input("Enter your choice: (1-5) "))
    if choice == 1:
        print("Your current balance is:", bank.check_balance())
    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        bank.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        bank.withdraw(amount)
    elif choice == 4:
       bank.display_info()
    elif choice ==5:
        print("Exiting program")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 4.")        
        
from src.Customers import Customers

class Deposit :

    def Deposit(self):
        print("=================")
        print("You can now deposit money into your University account.")
        print("=================")
        while True:
            try:
                amount = float(input("How much would you like to add to your wallet?: "))
                print("\n Amount Deposited: £", amount)
                break
            except ValueError:
                print("\n This is not a number. Please try again.")
                print()

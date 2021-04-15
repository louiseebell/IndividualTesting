from src.LogIn import LogIn
from src.Deposit import Deposit

class Main:
    def main():
        logIn = LogIn()
        logIn.logIn()
        deposit = Deposit()
        deposit.Deposit()

if __name__ == '__main__':
    Main.main()
from src.Customers import Customers


class LogIn:
    def getPassword(self,userName):
        customers = Customers()
        customerData = customers.loadCustomers()
        password = ""
        counter = 0
        while password == "" and counter < len(customerData):
            if userName == customerData[counter][0]:
                password = customerData[counter][3]
            counter += 1
        return password

    def logIn(self):
        userName = input("Welcome to Glasgow University bank. Please enter your username. ")
        password = self.getPassword(userName)
        if password == "":
            print("Your username is incorrect.")
        else:
            if input("Enter password ") == password:
                print("Welcome", userName, ". You are now logged on.")
            else:
                print("This is the incorrect password.")
                quit()

from src.ReadCSVFile import ReadCSVFile


class Customers:

    def loadCustomers(self):
        readCSVFile = ReadCSVFile()
        customerData = readCSVFile.getFileData("customer")
        return customerData

    def formatCustomers(self):
        display = ""
        customerData = self.loadCustomers()
        for counter in range(1, len(customerData)):
            display += customerData[counter] + " \n"
        return display

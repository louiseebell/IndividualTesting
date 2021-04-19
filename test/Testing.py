import unittest
from unittest.mock import MagicMock
from unittest.test.test_result import __init__

from src.main import Main
from src.LogIn import LogIn
from src.Customers import Customers
from src.ReadCSVFile import ReadCSVFile


class Test_LogIn(unittest.TestCase):
    logIn = LogIn()
    main = Main()
    Customers = Customers()

    fakeUsers = ['csmi', 'aarc']

    def __init__(self, methodName: str = ...):
        __init__(methodName)
        self.ReadCSVFile = None

    def test_CustomerInfo(self):
        customerInfo = self.ReadCSVFile.getFileData("Customer/", "customer.csv")
        customerColumns = customerInfo[0]
        self.assertEqual(customerColumns, ["Customers", ])

    def test_mockSingleResult(self):
        propertyData = []
        propertyData.append("Customers")
        propertyData.append("csmi, aarc")

        self.logIn.property = []
        self.logIn.config.getConfig = MagicMock(return_value=propertyData)
        result = self.logIn.getCustomers()

        self.assertEqual(['Customers'], result)


    def test_mockEnterUserPassword(self):
        LogIn.getUserInfo = MagicMock(return_value='aarc')
        self.assertEqual('Enter password', self.logIn())

   def test_getCustomerDataFromStub(self):
        self.main.setConfig(CSVStub)
        customerData = self.main.property
        customerColumns = customerData[0]
        self.assertEqual(customerColumns, "User Name")


if __name__ == '__main__':
    unittest.main()
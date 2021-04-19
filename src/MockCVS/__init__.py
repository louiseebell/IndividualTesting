class ReadInterface:
    def getConfig(self): pass


class CSVStub(ReadInterface):

    def getConfig(self):
        stubData = []
        stubData.append("UserName")
        stubData.append("dsom")
        stubData.append("mbar")
        stubData.append("lbel")
        return stubData
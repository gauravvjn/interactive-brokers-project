from ibapi.client import *
from ibapi.wrapper import *


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        mycontract = Contract()
        mycontract.symbol = "AAPL"
        mycontract.secType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"

        self.reqHistoricalData(orderId, mycontract, "20221010 15:00:00 US/Eastern", "1 D", "1 hour", "TRADES", 0, 1, 0,
                               [])

    def historicalData(self, reqId, bar):
        print(f"Historical Data: {bar}")

    def historicalDataEnd(self, reqId, start, end):
        print(f"End of HistoricalData")
        print(f"Start: {start}, End: {end}")

def main():
    app = TestApp()
    app.connect("127.0.0.1", 7497, 1000)
    app.run()


if __name__ == "__main__":
    main()

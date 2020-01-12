import yfinance as yf



class Info:
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = yf.Ticker("AAPL")
        
    def get_actions(self):
        #data = yf.download("LAZ", start="2009-09-10", end="2019-12-11")
        #print(data.to_json())
        print(self.ticker.info)
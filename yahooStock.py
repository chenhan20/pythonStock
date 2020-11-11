import yfinance as yf
import pandas as pd

# 台灣大盤代號 "^TWII"
# 台灣股票代號  代號.TW 例如: 2330.TW
defaultStockList = ['SQ','PLTR','TSLA','AAPL','AMD','APPS','BYND','PINS','GRMN','NKE','ORCL','WORK','PTON','SNE','WMT','CRM','LMT','VFC','ASML','GPRO','DIS','COST','AMZN'
,'FB','ZM','SPOT','NVDA','INTC','BRK-B','GOOG','UBER','TSM','UMC','MU','NFLX']

# defaultStockList = ['APPS','2330.TW']



def getStockInfo(ticker):
    print("symbol : " + ticker)
    data = yf.Ticker(ticker)
    return data

def getStockList(symbolList):
    symbolString = ' '.join(symbolList)
    print(symbolString)
    stockList = yf.Tickers(symbolString)
    # print(stockList.tickers.MSFT.info)
    for stock in stockList.tickers:
        print(stock.info['shortName'])
        print(stock.history(start="2020-11-09",end="2020-11-15",interval="5m"))
        print(stock.history(start="2020-11-08", end="2020-11-08", interval="1m"))

def downloadStock(symbolList):
    symbolString = ' '.join(symbolList)
    data = yf.download(symbolString ,start="2020-01-01", end="2020-12-30")
    print(data)
    # for stock in data:
    #     print(stock)

def getActivesStockList():
    # 貼上連結
    url = 'https://finance.yahoo.com/most-active?offset=0&count=30'
    data = pd.read_html(url)[0]
    stk_list = data.Symbol
    # print(pd.DataFrame(data))
    print(stk_list)





# getStockList(defaultStockList)
# downloadStock(defaultStockList)
# getActivesStockList()



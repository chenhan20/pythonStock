import getStockThree as three
import yahooStock as ys
import datetime
import time

now = datetime.datetime.now()


def getNewThree():
    fail = True
    date = now
    while fail:
        fail = three.getThree(date)
        date = date - datetime.timedelta(days=1)
        time.sleep(3) # 五秒內只能call三次 否則會被鎖

def getDateThree(date):
    fail = True
    while fail:
        three.getThree(date)
        date = date - datetime.timedelta(days=1)
        time.sleep(3) # 五秒內只能call三次 否則會被鎖

def getYahooData():
    stockData = ys.getStockInfo("MSFT")
    print(stockData.info)

# getDateThree(datetime.datetime(2020,7,31))
# getNewThree()
getYahooData()
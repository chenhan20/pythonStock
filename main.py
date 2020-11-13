import getStockThree as three
import yahooStock as ys
import datetime
import time
import pandas as pd

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

def getStockDetail():
    stockNumList = ['2330','2454','2337','2303']
    stockList = []
    for stockNum in stockNumList:
        tStart = time.time()#計時開始
        stockData = three.getThreeBuyDetail(now, stockNum)
        stockList.extend([[stockNum,"抓取時間：%f 秒" % (time.time() - tStart)]])
        stockList.extend(stockData['data'])
        fields=stockData['fields']
        time.sleep(3) # 五秒內只能call三次 否則會被鎖
    
    df = pd.DataFrame(stockList,columns=fields)
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)
    print(df)


def getYahooData():
    stockData = ys.getStockInfo("MSFT")
    print(stockData.info)

# getDateThree(datetime.datetime(2020,7,31))
# getNewThree()
# getYahooData()
getStockDetail()
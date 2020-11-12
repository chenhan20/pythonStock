import pandas as pd
import json
import requests 

# 偽瀏覽器
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def converterNumber(num):
    numberLength = len(str(num))
    converterNumber =num
    if(numberLength > 12):
        converterNumber = str(round(num / 1000000000000,2)) + '兆'
    elif(numberLength > 8 and numberLength <= 12):
        converterNumber = str(round(num / 100000000,2)) + '億'
    elif(numberLength > 4 and numberLength <= 8):
        converterNumber = str(round(num / 10000,2)) + '萬'
    return converterNumber

def converter(data):
    for i in range(len(data)):
        for d in range(len(data[i])):
            result = data[i][d].replace(',','')
            if result.lstrip('-').isdigit():
                result = converterNumber(int(result))
            data[i][d] = result

def getThree(date):
    print('日期:'+ date.strftime("%Y%m%d"))

    url = 'https://www.twse.com.tw/fund/BFI82U?response=json&dayDate=' + date.strftime("%Y%m%d") + '&type=day'

    res = requests.get(url, headers=headers)
    stockData=json.loads(res.text)
    print(stockData)

    if stockData['stat']=='OK':
        converter(stockData['data'])
        df = pd.DataFrame(stockData['data'],columns=stockData['fields'])
        pd.set_option('display.unicode.ambiguous_as_wide', True)
        pd.set_option('display.unicode.east_asian_width', True)
        print(df)
        fail = False
    else:
        print(stockData['stat'])
        fail = True
    
    return fail

def getThreeBuyDetail(date, stockNum):
    # url = 'https://www.twse.com.tw/fund/T86?response=json&date=20201111&selectType=ALL'
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?date='+date.strftime("%Y%m%d")+'&stockNo=' + stockNum

    res = requests.get(url, headers=headers)
    stockData=json.loads(res.text)

    if stockData['stat']=='OK':
        converter(stockData['data'])
        df = pd.DataFrame(stockData['data'],columns=stockData['fields'])
        pd.set_option('display.unicode.ambiguous_as_wide', True)
        pd.set_option('display.unicode.east_asian_width', True)
        return df
    else:
        print(stockData['stat'])
        return pd.DataFrame()


def test():
    stockList = ['2330','2337']
    for i in stockList:
        print(i)


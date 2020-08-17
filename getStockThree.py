import pandas as pd
import json
import requests 
import datetime

now = datetime.datetime.now()

# stock_no = input('輸入你想查找股票關鍵字或代號: ')
url = 'https://www.twse.com.tw/fund/BFI82U?response=json&dayDate=' + now.strftime("%Y%m%d") + '&type=day'

# 偽瀏覽器
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def converter(data):
    for i in range(len(data)):
        for d in range(len(data[i])):
            converterNumber = data[i][d].replace(',','')
            if converterNumber.isdigit():
                converterNumber = int(converterNumber)
            data[i][d] = converterNumber


res = requests.get(url, headers=headers)

stockData=json.loads(res.text)

if stockData['stat']=='OK':
    converter(stockData['data'])
    df = pd.DataFrame(stockData['data'],columns=stockData['fields'])
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)
    print(df)
else:
    print(stockData['stat'])




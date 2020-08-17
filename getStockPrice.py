import pandas as pd
import json
import requests 
import datetime

now = datetime.datetime.now()

stock_no = input('輸入你想查找股票關鍵字或代號: ')

url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?date=' + now.strftime("%Y%m%d") +'&stockNo='+ stock_no
# 偽瀏覽器
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


res  = requests.get(url, headers=headers)

# df = pd.DataFrame(res.text)
# df
stockData=json.loads(res.text)

# print(stockData['stat'])
if stockData['stat']=='OK':
    df = pd.DataFrame(stockData['data'],columns=stockData['fields'])
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)
    print(df)
else:
    print(stockData['stat'])




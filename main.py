import getStockThree as three
import datetime
import time

now = datetime.datetime.now()
date = now

fail = True

while fail:
    fail = three.getThree(date)
    date = date - datetime.timedelta(days=1)
    time.sleep(3) # 五秒內只能call三次 否則會被鎖

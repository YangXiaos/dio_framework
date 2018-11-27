# @Time         : 18-11-11 下午8:10
# @Author       : DioMryang
# @File         : test_other.py
# @Description  :
from DioCore.Downloader.Downloader import Setting

from DioCore.Downloader import Downloader


def test_proex():

    url = "https://www.google.com/"

    proxies = [("35.199.102.178", "8118"),
               ("40.78.102.88", "80"), ("38.98.171.2", "60490"), ("38.64.180.133", "8080"), ("38.127.88.6", "53281"),
               ("38.128.236.229", "3128"), ("35.240.29.142", "3128"), ("35.236.52.2", "80"),
               ("207.176.218.178", "1337"), ("216.183.54.132", "60683")]
    for proxy in proxies:
        setting = Setting()
        setting.setProxies(ip=proxy[0], port=proxy[1])
        res = Downloader.get(url, setting=setting)
        if res is not None:
            print(res.text)


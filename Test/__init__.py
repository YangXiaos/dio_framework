# @Time         : 18-3-12 下午8:25
# @Author       : DioMryang
# @File         : Const.py.py
# @Description  :
from DioCore.Downloader import Downloader


host = "101.50.1.2"
port = "80"
http = "http://{}:{}".format(host, port)
https = "https://{}:{}".format(host, port)
url = "https://www.xvideos.com/video36488893/alexis_jane_my_little_sister_slutty_roommate"
res, soup = Downloader.getSoup(url, proxies={"http": http, "https": https})
print(soup.text)
# @Time         : 18-10-28 下午6:36
# @Author       : DioMryang
# @File         : test_localMultiThreadSpiderTestTool.py
import logging
import uuid

from DioCore.Downloader.Downloader import Downloader, Setting

from DioFramework.Base.Spider.LocalSpider import LocalRegexSpider
from DioFramework.Base.Message import Message
from DioFramework.Tool.LocalMultiThreadSpiderTestTool import LocalMultiThreadSpiderTestTool


class ContentSpider(LocalRegexSpider):
    """导航爬虫"""
    regex = "http://www.meineihan.la/\w+/\d+-\d+-\d+/\d+_\d+.html"

    def crawl(self, enterUrl, info):
        setting = Setting()
        setting.htmlParse = True
        res = Downloader.get(enterUrl, setting)

        for aTag in res.soup.select(".neihan-content img, .contentText img"):
            yield Message(info={"enter_url": aTag["src"]})

        for aTag in res.soup.select(".neihan-content-page a"):
            if "href" in aTag.attrs:
                yield Message(info={"enter_url": "http://www.meineihan.la" + aTag["href"]})


class ImgSpider(LocalRegexSpider):
    """图片爬虫"""
    regex = "http://ww\d+.sinaimg.cn/.*?.gif"

    def crawl(self, enterUrl, info):
        res = Downloader.get(enterUrl)
        with open('/home/mryang/Project/dio_framework/Test/gif/{}.gif'.format(uuid.uuid4().__str__()), 'wb') as file:
            file.write(res.content)
        return []


# @Description  :
# class TestLocalMultiThreadSpiderTestTool(TestCase):
#     def test_run(self):
#         print("begin")
#         logging.basicConfig(level=logging.INFO)
#         print("begin")
#         tool = LocalMultiThreadSpiderTestTool([ContentSpider(), ImgSpider()])
#         print("begin")
#         tool.queue.put(Message(info={"enter_url": "http://www.meineihan.la/gifsgifs/2014-02-20/12139_15.html"}))
#         print("begin")
#         tool.run()
#
#     def test_Spider(self):
#         logging.basicConfig(level=logging.INFO)
#         print(list(ContentSpider().crawl("http://www.meineihan.la/gifsgifs/2014-02-20/12139_15.html", {})))
#

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s[thread:%(thread)s] - %(levelname)s: %(message)s')
    tool = LocalMultiThreadSpiderTestTool([ContentSpider(), ImgSpider()])
    tool.queue.put(Message(info={"enter_url": "http://www.meineihan.la/gifsgifs/2014-02-20/12139_15.html"}))
    tool.run()

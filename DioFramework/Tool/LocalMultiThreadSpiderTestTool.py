# @Time         : 18-9-10 下午10:51
# @Author       : DioMryang
# @File         : LocalMultiThreadSpiderTestTool.py
# @Description  :
import logging
from queue import Queue

from DioCore.Units import ThreadUnit, TimeUnit

from DioFramework.Base.LocalSpider import LocalRegexSpider
from build.lib.DioCore.Units.ThreadUnit import getCurrentThreadName


class LocalMultiThreadSpiderTestTool(object):
    """

    """
    def __init__(self, spiders: [LocalRegexSpider], threadSize: int=5):
        self.queue = Queue()
        self.messageSet = set()
        self.spiders = spiders
        self.threadSize = threadSize
        self.threadStopState = {}
        self.logger = logging.getLogger(self.__class__.__name__)

    def match(self, message):
        for spider in self.spiders:
            if spider.match(message):
                return spider
        return None

    def run(self):
        ThreadUnit.multiThreadingRun(self.execute, threadNum=4)

    def execute(self, num):
        """
        执行
        :return:
        """
        self.threadStopState[getCurrentThreadName()] = False
        while True:
            if all(self.threadStopState.values()):
                break

            # 判断是否需要线程
            if self.queue.empty():
                self.threadStopState[getCurrentThreadName()] = True
                TimeUnit.sleep(5)
                continue
            self.threadStopState[getCurrentThreadName()] = False

            message = self.queue.get()

            # 去重
            if message.getFullUrl() in self.messageSet:
                continue
            self.messageSet.add(message.getFullUrl())

            # 获取匹配爬虫并跑数
            spider = self.match(message)
            msgs = spider.execute(message)
            for msg in msgs:
                if msg.getFullUrl() not in self.messageSet:
                    self.queue.put(msg)

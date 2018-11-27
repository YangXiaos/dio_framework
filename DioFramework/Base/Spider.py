# @Time         : 18-7-8 下午7:51
# @Author       : DioMryang
# @File         : Spider.py
# @Description  :
import logging

from typing import List

from DioFramework.Base.Message import Message


class Spider(object):
    """
    Spider

    爬虫抓取类
    """
    def __init__(self):
        self.taskId = -1
        self.jobId = ""
        self.context = {}
        self.logger = logging.getLogger(self.__class__.__name__)

    def getFullUrl(self, info):
        """
        获取 fullUrl
        :return:
        """
        return info.get("full_url")

    def crawl(self, fullUrl, info) -> List[Message]:
        """
        爬虫逻辑编写处
        :param fullUrl: 入口url
        :param info: 信息
        :return:
        """
        pass

    def execute(self, message, job):
        """
        跑数
        :param job:
        :param message:
        :return:
        """
        fullUrl = self.getFullUrl(message.getInfo())
        self.jobId = job.jobId
        self.taskId = job.taskId
        self.context = job.context
        messages = self.crawl(fullUrl, message.getInfo())
        self.setInfoSpiderName(messages)
        return list(messages)

    @classmethod
    def setInfoSpiderName(cls, messages):
        for message in messages:
            message.getInfo()["__spider__"] = cls.__name__



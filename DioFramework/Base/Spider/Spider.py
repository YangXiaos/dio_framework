# @Time         : 18-7-8 下午7:51
# @Author       : DioMryang
# @File         : Spider.py
# @Description  :
import logging

from DioFramework.Base.Message import Message
from DioFramework.Const import MSG_FIELD


class Spider(object):
    """
    Spider

    用于处理数据
    """
    def __init__(self):
        self.taskId = -1
        self.jobId = ""
        self.context = {}
        self.logger = logging.getLogger(self.__class__.__name__)

    def getEnterUrl(self, info):
        """
        获取 enterUrl
        :return:
        """
        return info.get(MSG_FIELD.ENTER_URL)

    def crawl(self, enterUrl, info):
        """
        爬虫逻辑编写处
        :param enterUrl: 入口url
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
        enterUrl = self.getEnterUrl(message.getInfo())
        self.jobId = job.jobId
        self.taskId = job.taskId
        self.context = job.context

        for msg in self.crawl(enterUrl, message.getInfo()):
            self.setInfoSpiderName(msg)
            yield msg

    @classmethod
    def setInfoSpiderName(cls, messages):
        for message in messages:
            message.getInfo().update({MSG_FIELD.SPIDER_NAME, cls.__name__})

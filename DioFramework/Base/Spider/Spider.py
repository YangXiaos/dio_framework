# @Time         : 18-7-8 下午7:51
# @Author       : DioMryang
# @File         : Spider.py
# @Description  :
import abc
import logging

from typing import Iterable

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Const import MSG_FIELD


class Spider(metaclass=abc.ABCMeta):
    """
    Spider

    用于处理数据
    """
    def __init__(self, *args, **kwargs):
        self.taskId = -1
        self.jobId = ""
        self.context = {}
        self.logger = logging.getLogger(self.__class__.__name__)

    @classmethod
    def getEnterUrl(cls, info):
        """
        获取 enterUrl
        :return:
        """
        return info.get(MSG_FIELD.ENTER_URL)

    @abc.abstractmethod
    def crawl(self, enterUrl, info) -> Iterable[Message]:
        """
        爬虫逻辑编写处
        :param enterUrl: 入口url
        :param info: 信息
        :return:
        """
        pass

    def execute(self, message, job: Job):
        """
        跑数
        :param job:
        :param message:
        :return:
        """
        self.logger.info("[{}]: {}".format(self.__class__.__name__, message.getEnterUrl()))

        enterUrl = self.getEnterUrl(message.getInfo())
        self.jobId = job.id
        self.taskId = job.taskId
        self.context = job.context

        for msg in self.crawl(enterUrl, message.getInfo()):
            self.setInfoSpiderName(msg)
            yield msg

    @classmethod
    def setInfoSpiderName(cls, msg: Message):
        msg.getInfo().update({MSG_FIELD.SPIDER_NAME: cls.__name__})

# @Time         : 18-8-22 下午10:04
# @Author       : DioMryang
# @File         : BaseDistributor.py
# @Description  :
import abc
import logging

from typing import List

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message


class BaseDistributor(metaclass=abc.ABCMeta):
    """
    分发工具基类

    Attributes:
        params: 配置参数

    Methods:
        distribute: 分发
    """
    def __init__(self, params: dict):
        self.params = params
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info(" init message distributor")

    @abc.abstractclassmethod
    def distribute(self, job: Job, messages: List[Message]):
        """
        分发
        :param job: 爬虫作业
        :param messages: message 列表
        :return:
        """
        pass

# @Time         : 18-8-22 下午10:04
# @Author       : DioMryang
# @File         : BaseDistributor.py
# @Description  :
import abc
import logging

from typing import List

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Mixin.LoadClassToolMixin import LoadClassToolMixin


class BaseDistributor(metaclass=abc.ABCMeta):
    """
    分发工具基类
    通过 msgMatchStrategy 匹配成功，传入writer 分发 msg

    Attributes:
        params: 配置参数
        ```
        [
            {
                "msg_match_strategy": {
                    "class_name": "",
                    "params": {
                    }
                },
                "msg_writer": {
                    "class_name": "",
                    "params": {

                    }
                }
            }
        ]
        ```
        strategyWriterMap: msg策略, writer 匹配

    Methods:
        distribute: 分发

    """
    def __init__(self, params: list):
        self.params = params
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info(" init message distributor")
        self.strategyWriterMap = {}

        for mapping in params:
            msgMatchStrategy = LoadClassToolMixin.initObjByConfig(mapping["msg_match_strategy"])
            msgWriter = LoadClassToolMixin.initObjByConfig(mapping["msg_writer"])
            self.strategyWriterMap[msgMatchStrategy] = msgWriter

    @abc.abstractmethod
    def distribute(self, job: Job, messages: List[Message]):
        """
        分发
        :param job: 爬虫作业
        :param messages: message 列表
        :return:
        """
        pass

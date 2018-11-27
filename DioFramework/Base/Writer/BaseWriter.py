# @Time         : 18-8-22 下午10:13
# @Author       : DioMryang
# @File         : BaseWriter.py
# @Description  :
import abc
import logging

from DioFramework.Base import Message
from DioFramework.Base.Job.Job import Job


class BaseWriter(metaclass=abc.ABCMeta):
    """
    base writer

    Attributes:
        logger: 日志工具

    Methods:
        write: 写入函数
    """
    def __init__(self, params: dict):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.params = params

    @abc.abstractclassmethod
    def write(self, job: Job, message: Message):
        """写入message"""
        pass

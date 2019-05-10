# @Time         : 18-8-4 下午3:01
# @Author       : DioMryang
# @File         : ThreadStateManager.py
# @Description  :
import abc
import logging

from DioCore.DB.RedisClient import Hash

from DioCore.Utils.ThreadUtil import getCurrentThreadName
from DioFramework.Const import JobThreadState
from DioFramework.DB.Const import Connection


class BaseThreadStateManager(metaclass=abc.ABCMeta):
    """
    线程状态管理器基类

    Methods

    """
    KEY_FORMAT = "{curRunnerId}_{jobId}_{threadName}"
    RUNNING = "RUNNING"
    OVER = "OVER"
    DONE = "DONE"

    @abc.abstractclassmethod
    def getState(self) -> str:
        """获取当前线程状态"""
        pass

    @abc.abstractclassmethod
    def setStateRunning(self):
        """设置当前线程状态"""
        pass

    @abc.abstractclassmethod
    def setStateOver(self):
        """设置当前线程结束"""
        pass

    @abc.abstractclassmethod
    def isAllThreadsOver(self):
        """是否所有 的线程状态为结束"""
        pass

    @abc.abstractclassmethod
    def finish(self):
        """终结"""
        pass


class RedisThreadStateManager(BaseThreadStateManager):
    """
    线程状态 Manager 负责管理job的线程状态

    MetaClass:
        abc.ABCMeta

    Attributes:
        logger： logger

    GlobalAttributes:
        format：{str} "{runnerId}_{jobId}" 键名

    Methods:
        __init__: 初始化，打logger
            curRunnerId：当前runner 状态
            jobId：作业 id
            format: 字典key 渲染
            getState：获取当前线程job状态

        getState: 获取当前线程状态
        setRunning：设置threadState 当前线程状态为RUNNING
        setOver：设置threadState  当前线程为OVER。
        isAllThreadsOver：迭代StateHash判断所有线程是否结束。
        getKeyName：根据format 设置键名
    """

    def __init__(self, curRunnerId: str, jobId: str):
        self.jobId = jobId
        self.curRunnerId = curRunnerId
        self.logger = logging.getLogger(self.__class__.__name__)
        self.threadStateHash = Hash(Connection.REDIS_DEFAULT, jobId)
        self.logger.info(" init threadStateManager success: runner ->{} , job ->{}".format(curRunnerId, jobId))

    def getState(self) -> str:
        """获取当前线程状态"""
        return self.threadStateHash.hget(self.getKeyName())

    def setStateRunning(self) -> None:
        """设置threadState 当前线程状态为RUNNING"""

        self.threadStateHash.hset(self.getKeyName(), self.RUNNING)

    def setStateOver(self) -> None:
        """设置threadState 当前线程状态为 OVER"""
        self.threadStateHash.hset(self.getKeyName(), self.OVER)

    def isAllThreadsOver(self) -> bool:
        """判断所有线程是否结束"""
        return all(map(lambda val: val == JobThreadState.OVER, self.threadStateHash.hvals()))

    def getKeyName(self) -> str:
        """获取当前线程键名"""
        return self.KEY_FORMAT.format(**{"curRunnerId": self.curRunnerId, "jobId": self.jobId,
                                         "threadName": getCurrentThreadName()})

    def finish(self):
        """结束"""
        pass


class CacheThreadStateManager(BaseThreadStateManager):
    """
    内存 线程状态manager
    """
    def __init__(self, curRunnerId: str, jobId: str):
        self.jobId = jobId
        self.curRunnerId = curRunnerId
        self.logger = logging.getLogger(self.__class__.__name__)
        self.threadStateHash = {}
        self.logger.info(" init CacheThreadStateManager success: runner ->{} , job ->{}".format(curRunnerId, jobId))

    def setStateDone(self):
        self.threadStateHash[getCurrentThreadName()] = self.DONE

    def getState(self) -> str:
        return self.threadStateHash[getCurrentThreadName()]

    def setStateOver(self):
        self.threadStateHash[getCurrentThreadName()] = self.OVER

    def isAllThreadsOver(self):
        return all(map(lambda val: val == JobThreadState.OVER, self.threadStateHash.values()))

    def setStateRunning(self):
        self.threadStateHash[getCurrentThreadName()] = self.RUNNING

    def finish(self):
        del self.threadStateHash

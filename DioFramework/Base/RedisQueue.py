# @Time         : 18-7-9 下午9:53
# @Author       : DioMryang
# @File         : RedisQueue.py
# @Description  :
from queue import Empty

from DioCore.DB.RedisClient import List

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message


class RedisEmpty(Empty):
    """redis 下的 Empty异常"""
    pass


class RunnerRedisQueue(List):
    """
    封装Queue， put, get 函数功能。
    """
    def qsize(self):
        return self.llen()

    def put(self, item, block=True):
        """
        将元素插入队列尾
        :param block:
        :param item:
        :return:
        """
        self.lpush(self.toRedis(item))

    def get(self, block=True):
        """
        获取队头 元素
        :return:
        """
        item = self.rpop()
        if item is not None:
            return self.toPython(item)
        if not block:
            raise RedisEmpty("list is None")

    @staticmethod
    def toRedis(item):
        """构造插入redis队列 的对象"""
        return item

    @staticmethod
    def toPython(item):
        """生成从redis队列获取的item python对象"""
        return item


class MessageRedisQueue(RunnerRedisQueue):
    """
    Message redis 队列 封装
    """
    @staticmethod
    def toRedis(item):
        """解析成json字符串 插入 redis队列"""
        return item.toJson()

    @staticmethod
    def toPython(item):
        """解析成 Message返回"""
        return Message.form(item)


class JobRedisQueue(RunnerRedisQueue):
    """
    Job redis 队列封装
    """
    @staticmethod
    def toRedis(item):
        """解析成 json 字符串对象"""
        return item.toJson()

    @staticmethod
    def toPython(item):
        """构造成 Job对象"""
        return Job.form(item)


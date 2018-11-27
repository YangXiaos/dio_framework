# @Time         : 18-10-20 下午9:49
# @Author       : DioMryang
# @File         : test_baseThreadStateManager.py
from unittest import TestCase


# @Description  :
from DioFramework.Base.Job.ThreadStateManager import CacheThreadStateManager, RedisThreadStateManager


class TestBaseThreadStateManager(TestCase):
    def test_finish(self):
        manager = CacheThreadStateManager()
        manager.setStateRunning()
        print(manager.getState())
        manager.setStateDone()
        print(manager.getState())

    def test_redis_manager(self):
        manager = RedisThreadStateManager("dio_miao", jobId="dio_miao_miao")
        manager.setStateRunning()
        print(manager.threadStateHash.keyName)


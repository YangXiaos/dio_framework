# @Time         : 18-8-25 下午3:26
# @Author       : DioMryang
# @File         : CommonDistributor.py
# @Description  :
from typing import List

from DioFramework.Base.Distributor.BaseDistributor import BaseDistributor
from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message


class CommonDistributor(BaseDistributor):
    """
    通用分发工具

    且关系
    """
    def __init__(self, params: list):
        super().__init__(params)
        self.logger.info("CommonDistributor params: {}".format(params))
        self.logger.info("init CommonDistributor success")

    def distribute(self, job: Job, messages: List[Message]):
        """
        迭代messages 匹配Mapping strategy 匹配成功写入
        :param job:
        :param messages:
        :return:
        """
        for message in messages:
            for strategy, writer in self.strategyWriterMap.items():
                if strategy.match(message):
                    writer.write(job, message)

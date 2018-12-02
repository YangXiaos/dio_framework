# @Time         : 18-8-25 下午3:26
# @Author       : DioMryang
# @File         : CommonDistributor.py
# @Description  :
from typing import List

from DioFramework.Base.Distributor.BaseDistributor import BaseDistributor
from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Mixin.LoadClassToolMixin import LoadClassToolMixin


class CommonDistributor(BaseDistributor):
    """
    通用分发工具

    Attributes:
        msgMatchStrategy2writerMapping: 消息匹配策略 writer 匹配

    """
    def __init__(self, params: dict):
        super().__init__(params)
        self.msgMatchStrategy2writerMapCfgList = params.get("strategy_writer_mappings")
        self.msgMatchStrategy2writerMapping = {}

        for cfg in self.msgMatchStrategy2writerMapCfgList:
            msgMatchStrategy = LoadClassToolMixin.initObjByConfig(cfg.get("message_match_strategy"))
            writer = LoadClassToolMixin.initObjByConfig(cfg.get("writer"))
            self.msgMatchStrategy2writerMapping[msgMatchStrategy] = writer

    def distribute(self, job: Job, messages: List[Message]):
        """
        迭代messages 匹配Mapping strategy 匹配成功写入
        :param job:
        :param messages:
        :return:
        """
        for message in messages:
            for msgMatchStrategy, writer in self.msgMatchStrategy2writerMapping.items():
                if msgMatchStrategy.match(message):
                    writer.write(job, message)
                    continue

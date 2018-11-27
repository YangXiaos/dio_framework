# @Time         : 18-7-12 下午11:38
# @Author       : DioMryang
# @File         : MessageSender.py
# @Description  : 
from typing import List

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Processor.MessageProcessor import MessageProcessor


class MessageSender(MessageProcessor):
    """
    消息 分发处理器
    """
    def run(self, job: Job, messages: List[Message]):
        """执行"""
        job.distributor.distribute(job, messages)
        return []

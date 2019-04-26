# @Time         : 18-7-12 下午11:37
# @Author       : DioMryang
# @File         : MessageFilter.py
# @Description  :
from typing import List
from DioCore.DB.RedisClient import Set

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Processor.MessageProcessor import MessageProcessor
from DioFramework.DB import Connection


class MessageFilter(MessageProcessor):
    """
    message 过滤器

    `config`:
    {
        `id`: 6,
        `params`: {
            "key_name": ""
        }
    }
    """
    def __init__(self, **kwargs):
        super(MessageFilter, self).__init__(**kwargs)
        # self.
        self.filter = Set(Connection.REDIS_DEFAULT, self.params.get("key_name"))

    def run(self, job: Job, messages: List[Message]):
        for message in messages:
            if not self.filter.sismember(message.getEnterUrl()):
                yield message

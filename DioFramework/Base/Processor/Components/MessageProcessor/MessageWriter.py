# @Time         : 18-12-2 上午11:41
# @Author       : DioMryang
# @File         : MessageWriter.py
# @Description  :
from typing import List

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Processor.MessageProcessor import MessageProcessor
from DioFramework.Base.Writer.MongodbWriter import MongodbWriter


class MessageMongodbWriter(MessageProcessor):
    """
    message 过滤器

    `config`:
    {
        `id`: 6,
        `params`: {
            "db_name": "db",
            "collection_name": "tb"
        }
    }
    """
    def __init__(self, **kwargs):
        super(MessageMongodbWriter, self).__init__(**kwargs)
        # self.
        self.writer = MongodbWriter(params=self.params)

    def run(self, job: Job, messages: List[Message]):
        self.writer.writeMany(job, messages)

if __name__ == '__main__':
    params = {
        "db_name": "test",
        "collection_name": "miao"
    }
    MessageMongodbWriter()
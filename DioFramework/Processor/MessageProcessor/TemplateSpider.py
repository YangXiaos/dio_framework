# @Time         : 18-7-12 下午11:37
# @Author       : DioMryang
# @File         : TemplateSpider.py
# @Description  :
from typing import List

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Processor.MessageProcessor import MessageProcessor


class MessageReader(MessageProcessor):
    """
    message 读取 processor

    `config`:
    {
        `id`: 6,
        `params`: {
            "waiting_time": 5
        }
    }

    """

    def run(self, job: Job, messages: List[Message]):
        """执行"""
        result = []
        for message in messages:
            for templateLoader in job.templateLoaderMapping.values():
                if templateLoader.match(message):
                    result += templateLoader.execute(job, messages)
                    break
        return result

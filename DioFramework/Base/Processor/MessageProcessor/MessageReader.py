# @Time         : 18-7-12 下午10:49
# @Author       : DioMryang
# @File         : MessageReader.py
# @Description  :
from typing import List

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message

from DioFramework.Base.Processor.MessageProcessor import MessageProcessor
from DioFramework.Error import Over


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
    def run(self, job: Job, message: List[Message]):
        """执行"""
        message = job.queue.get()

        # 判断是否有message, 有则返回msgs 无则
        if message is not None:
            return [message]
        raise Over()

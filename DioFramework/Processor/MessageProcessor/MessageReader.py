# @Time         : 18-7-12 下午10:49
# @Author       : DioMryang
# @File         : MessageReader.py
# @Description  :
from typing import List

from DioCore.Units import TimeUnit
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
        while True:
            message = job.queue.get()

            # 判断是否有message， 有设置线程RUNNING，返回message ，没有设置为OVER
            if message is not None:
                job.threadStateManager.setRunning()
                return [message]
            else:
                job.threadStateManager.setOver()

            # 判断所有线程是否结束
            if job.threadStateManager.isAllThreadsOver():
                raise Over()

            TimeUnit.sleep(int(self.params.get("waiting_time", )))

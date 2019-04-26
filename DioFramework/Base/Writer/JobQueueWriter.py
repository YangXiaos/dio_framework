# @Time         : 18-8-23 下午9:52
# @Author       : DioMryang
# @File         : JobQueueWriter.py
# @Description  :
from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Writer.BaseWriter import BaseWriter


class JobQueueWriter(BaseWriter):
    """
    job queue 分发
    {
        "db_name": "db",
        "collection_name": "coll"
    }

    """
    def write(self, job: Job, message: Message):
        self.logger.info(" job_queue_writer distribute {}".format(message.info))
        job.queue.put(message)

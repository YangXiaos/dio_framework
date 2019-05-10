# @Time         : 18-7-9 下午10:52
# @Author       : DioMryang
# @File         : JobMultiThreadProcessor.py
# @Description  : 多线程跑数处理器
from DioCore.Utils import ThreadUtil, TimeUtil

from DioFramework.Base.Processor.JobProcessor import JobProcessor
from DioFramework.Error import Over


class JobMultiThreadProcessor(JobProcessor):
    """
    多线程跑数 processor

    `id`: 4

    `config`:
    ```
    {
        "id" : 2,
        "params": {
            "thread_num": 3,
            "match_all": true,
            "thread_waiting_time": "5"
        }
    }

    `thread_num`: 默认线程数
    """

    def __init__(self, *args, **kwargs):
        super(JobMultiThreadProcessor, self).__init__(*args, **kwargs)
        self.threadNum = self.params.get("thread_num", )
        self.processorList = []

    def run(self, job):
        """跑数"""
        jobProcessorParams = job.taskConfig.getJobProcessorParams()
        self.processorList = [self.loadProcessorByConfig(cfg)
                              for cfg in job.taskConfig.getMessageProcessorConfig()]
        threadNum = int(jobProcessorParams.get("threadNum", )) if "threadNum" in jobProcessorParams else self.threadNum
        ThreadUtil.multiThreadingRun(self.crawlWithSingleThread, threadNum=threadNum, commonArgs=[job])
        self.logger.info("thread is over ")

    def crawlWithSingleThread(self, job):
        """
        单线程执行作业
        :param job: 作业
        :return:
        """
        # 设置线程running
        job.threadStateManager.setStateRunning()

        while job.threadStateManager.isAllThreadsOver():
            messages = []
            try:
                job.threadStateManager.setStateRunning()
                for processor in self.processorList:
                    messages = processor.run(job, messages)

            except Over:
                self.logger.info(" threadSpider[{threadName}] is done"
                                 .format(**{"threadName": ThreadUtil.getCurrentThreadName()}))
                job.threadStateManager.setStateOver()
                TimeUtil.sleep("thread_waiting_time")
            except Exception as ignored:
                pass

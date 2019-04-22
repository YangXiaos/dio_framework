# @Time         : 19-1-20 下午5:38
# @Author       : DioMryang
# @File         : EasyJobCrawlerHandler.py
# @Description  :
from DioCore.Utils.ModuleUtil import loadClass

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Mixin.LoadClassToolMixin import LoadClassToolMixin
from DioFramework.Base.Processor.JobProcessor import JobProcessor


class EasyJobCrawlerHandler(JobProcessor):
    """
    适配 mongo db writer快速写入
    配置参数
    {
        "id": x,
        "params": {
            "spiders": ['', ''],
            "writer" : { writer config }
        }
    }

    """

    def __init__(self, *args, **kwargs):
        super(EasyJobCrawlerHandler, self).__init__(*args, **kwargs)

    def run(self, job) -> Job:
        """
        释放资源
        :return:
        """
        # 加载爬虫, writer处理器
        spiders = [loadClass(spider)() for spider in self.params.get("spiders", [])]
        writer = LoadClassToolMixin.loadProcessorByConfig(self.params.get("writer"))

        msgs = job.initMsgs

        # 每个爬虫跑一次
        for spider in spiders:
            temp = []
            for msg in msgs:
                temp += spider.execute(msg, job)
            msgs = temp

        # 爬虫msg save
        writer.execute(job=job, messages=msgs)
        return job

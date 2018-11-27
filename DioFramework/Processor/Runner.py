# @Time         : 18-6-6 下午9:04
# @Author       : DioMryang
# @File         : Runner.py
# @Description  :
import uuid

from DioFramework.Base.Processor.Processor import Processor
from DioFramework.DB.Const import Connection


class Runner(Processor):
    """
    Runner

    跑数处理器

    Attributes:
        uuid: 唯一id
        config: 配置参数
        {
            "id": 1,
            // job处理器配置
            "job_processor_config": [
                {
                    id: "1"
                }
            ]
        }
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.runnerId = uuid.uuid4()

        # 初始化处理器
        self.processorList = []
        for cfg in self.config.get("job_processor_config", ):
            self.processorList.append(self.loadProcessorByConfig(cfg))

    def run(self, *args, **kwargs):
        """
        开始跑数
        :return:
        """
        job = {"runner_id": self.runnerId}
        self.logger.info("start handle runner[{}] job ".format(self.runnerId))

        for processor in self.processorList:
            job = processor.execute(job=job)

    def finish(self, *args, **kwargs):
        """
        清除 redis runner状态
        :param args: 爬虫结束
        :param kwargs:
        :return:
        """
        # 清空redis runner状态
        Connection.REDIS_DEFAULT.hdel("dio.crwaler.runner", str(self.runnerId))

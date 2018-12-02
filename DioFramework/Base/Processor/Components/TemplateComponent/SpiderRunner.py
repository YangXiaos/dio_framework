# @Time         : 18-10-15 下午11:05
# @Author       : DioMryang
# @File         : SpiderRunner.py
# @Description  :
from typing import List

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Mixin.LoadClassToolMixin import LoadClassToolMixin
from DioFramework.Base.Processor.TemplateComponent import TemplateComponent


class SpiderRunner(TemplateComponent):
    """

    """
    def __init__(self, **kwargs):
        super(SpiderRunner, self).__init__(**kwargs)
        self.spider = LoadClassToolMixin.initObjByConfig(self.params.get("spider"))

    def run(self, job: Job, messages: List[Message]):
        """执行"""
        result = []
        for message in messages:
            result.append(self.spider.execute(message, job))
        return result

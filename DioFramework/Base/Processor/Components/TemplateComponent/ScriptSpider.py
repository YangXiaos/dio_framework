# @Time         : 18-10-15 下午11:05
# @Author       : DioMryang
# @File         : ScriptSpider.py
# @Description  :
from typing import List, Iterable

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Mixin.LoadClassToolMixin import LoadClassToolMixin
from DioFramework.Base.Processor.TemplateComponent import TemplateComponent


class ScriptSpider(TemplateComponent):
    """
    脚本爬虫处理组件, 执行指定spider类

    json配置:
    {
        `id`: 15,
        `params`: {
            "spider": {             # spider 配置
                "class_name": "DioSpider.OldSpider.Boss.BossJobSpider.BossJobSpider",
                "params": {}
            }
        }
    }
    """
    def __init__(self, **kwargs):
        super(ScriptSpider, self).__init__(**kwargs)
        self.spider = LoadClassToolMixin.initObjByConfig(self.params.get("spider"))

    def run(self, job: Job, messages: List[Message]) -> Iterable[Message]:
        """执行组件"""
        result = []
        for message in messages:
            result += self.spider.execute(message, job)
        return result

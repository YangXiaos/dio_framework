# @Time         : 18-7-16 下午9:42
# @Author       : DioMryang
# @File         : TemplateLoader.py
# @Description  :
import logging

from typing import List

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Mixin.LoadClassToolMixin import LoadClassToolMixin
from DioFramework.DB.Dao.MysqlDao.TemplateConfigDao import TemplateConfig


class TemplateLoader(LoadClassToolMixin):
    """
    模板加载类

    Attributes:
        componentsConfig: 组件配置
        messageMatchStrategyConfig: 匹配策略
        componentList: 组件列表
        messageMatchStrategy: message 匹配策略

        tpId: 模板id
        desc: 模板desc
        type: 模板类型

    Methods:
        execute: 执行该模板
        match: 调用msgMatchStrategy 进行匹配
        getTemplateId: 获取模板id

    """
    def __init__(self, tpConfig: TemplateConfig):
        self.componentsConfig = tpConfig.template_component_config
        self.messageMatchStrategyConfig = tpConfig.getMessageMatchStrategyConfig()
        self.tpId = tpConfig.id
        self.desc = tpConfig.desc
        self.type = tpConfig.type
        self.logger = logging.getLogger(self.__class__.__name__)

        self.componentList = []
        for cpConfig in tpConfig.getTemplateComponentConfig():
            cpConfig.update({"tpId": self.tpId, "tpDesc": self.desc, "tpType": self.type})
            self.loadProcessorByConfig(config=cpConfig)

        self.messageMatchStrategy = self.initObjByConfig(self.messageMatchStrategyConfig)
        self.logger.info("init TemplateLoader {}".format(self.tpId))

    def execute(self, job: Job, message: Message) -> List[Message]:
        """
        调用模板进行跑数
        :param message: 消息
        :param job: 爬虫作业
        :return:
        """
        messages = [message]
        for component in self.componentList:
            messages = component.execute(job=job, messages=messages)

        return messages

    def match(self, message: Message) -> bool:
        """
        匹配message
        :param message:
        :return:
        """
        return self.messageMatchStrategy.match(message)

    def getTemplateId(self) -> int:
        """获取模板id"""
        return self.tpId

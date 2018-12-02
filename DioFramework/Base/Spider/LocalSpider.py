# @Time         : 18-10-28 下午2:12
# @Author       : DioMryang
# @File         : LocalSpider.py
# @Description  :
import re

from DioFramework.Base.Message import Message
from DioFramework.Base.Spider.Spider import Spider


class LocalRegexSpider(Spider):
    """
    正则匹配爬虫
    """
    regex = ""

    def match(self, message: Message):
        return re.match(self.regex, message.getEnterUrl()) is not None

    def execute(self, message, job=None):
        """
        跑数
        :param job:
        :param message:
        :return:
        """
        self.logger.info("[{}] {}".format(self.__class__.__name__, message.getEnterUrl()))
        enterUrl = self.getEnterUrl(message.getInfo())
        messages = list(self.crawl(enterUrl, message.getInfo()))
        self.setInfoSpiderName(messages)
        return messages

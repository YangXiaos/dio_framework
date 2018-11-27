# @Time         : 18-10-28 下午2:12
# @Author       : DioMryang
# @File         : LocalSpider.py
# @Description  :
import re

from DioFramework.Base.Message import Message
from DioFramework.Base.Spider import Spider


class LocalRegexSpider(Spider):
    """

    """
    regex = ""

    def match(self, message: Message):
        return re.match(self.regex, message.getFullUrl()) is not None

    def execute(self, message, job=None):
        """
        跑数
        :param job:
        :param message:
        :return:
        """
        self.logger.info("[{}] {}".format(self.__class__.__name__, message.getFullUrl()))
        fullUrl = self.getFullUrl(message.getInfo())
        messages = list(self.crawl(fullUrl, message.getInfo()))
        self.setInfoSpiderName(messages)
        return messages

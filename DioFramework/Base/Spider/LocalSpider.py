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

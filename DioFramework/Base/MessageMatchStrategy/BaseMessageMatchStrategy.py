# @Time         : 18-8-12 下午1:23
# @Author       : DioMryang
# @File         : MessageMatchStrategy.py
# @Description  :
import abc

from DioFramework.Base.Message import Message
from DioFramework.Base.MessageMatchStrategy import MatchRuleFunction


class MessageMatchStrategy(metaclass=abc.ABCMeta):
    """
    模板匹配基类

    Attributes:
        config: list 参数，列表元素为多个字段组合的匹配规则。
            ```

              {
                "full_url": {
                  "regex": ".*"
                },
                "spider_ids": {
                  "equals": "12321"
                }
              }
            ```

    GlobalAttributes:
        matchRuleFunction: 匹配函数方法

    Methods:
        match: 匹配函数判断是否匹配正确

    """
    matchRuleFunction = {
        "contain": MatchRuleFunction.contain,
        "equal": MatchRuleFunction.equal,
        "partialRegex": MatchRuleFunction.partialRegex,
        "perfectRegex": MatchRuleFunction.perfectRegex,
    }

    def __init__(self, params: dict):
        """
        设置 config
        :param params: 匹配策略参数
        """
        self.params = params

    @abc.abstractclassmethod
    def match(self, message: Message) -> bool:
        """
        迭代字段 判断message 是否匹配正确
        :param message: message
        :return:
        """

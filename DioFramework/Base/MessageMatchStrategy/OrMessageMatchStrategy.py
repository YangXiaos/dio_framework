# @Time         : 18-8-12 下午3:11
# @Author       : DioMryang
# @File         : OrMessageMatchStrategy.py
# @Description  :
from DioFramework.Base import Message
from DioFramework.Base.MessageMatchStrategy import MessageMatchStrategy


class OrMessageMatchStrategy(MessageMatchStrategy):
    """
    或匹配策略，一个字段判断成功返回True
    """

    def match(self, message: Message) -> bool:
        """
        || 匹配第一个验证成功的
        :param message:
        :return:
        """
        for fieldName, matchRule in self.params.items():
            value = message.info.get(fieldName)
            fucName, rule = list(matchRule.items())[0]

            if self.validate(rule, value, fucName):
                return True
        return False

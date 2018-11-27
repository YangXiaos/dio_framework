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
        只有　一个
        :param message:
        :return:
        """
        for fieldName, matchRule in self.params.items():
            value = message.info.get(fieldName, )
            fucName, rule = matchRule.items().get(0, )

            if self.matchRuleFunction[fucName](rule, value):
                return True

        return False

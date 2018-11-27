# @Time         : 18-8-12 下午3:37
# @Author       : DioMryang
# @File         : MatchRuleFunction.py
# @Description  :
import re


class MatchRuleFunction(object):
    """
    匹配规则 策略函数
    """

    @staticmethod
    def equal(rule: str, value: str) -> bool:
        """
        全等匹配函数，value 与 rule 完全相等则退出
        :param rule: 匹配规则
        :param value:  匹配值
        :return: True/False
        """
        if rule == value:
            return True
        else:
            return False

    @staticmethod
    def partialRegex(rule: str, value: str) -> bool:
        """
        部分匹配函数
        :param rule:
        :param value:
        :return:
        """
        return True if re.search(rule, value) is not None else False

    @staticmethod
    def perfectRegex(rule: str, value: str) -> bool:
        """
        完全匹配函数
        :param rule: 匹配规则 正则表达是
        :param value:
        :return:
        """
        return True if re.match(rule, value) is not None else False

    @staticmethod
    def contain(rule: list, value: str) -> bool:
        """
        判断是否包含
        :param rule: 参数列表
        :param value: 匹配值
        :return: Ｔｒｕｅ/False
        """
        return value in map(str, rule)
# @Time         : 18-7-13 下午11:21
# @Author       : DioMryang
# @File         : StandardizeMixin.py
# @Description  :
from DioCore.Units import JsonUnit


class StandardizeMixin(object):

    def toJson(self):
        """
        返回 json字符串形式
        :return:
        """
        return JsonUnit.toJson(self.toPython())

    @classmethod
    def form(cls, json):
        """
        字符串 生成 job
        :param json:
        :return:
        """
        return cls(**JsonUnit.toPython(json))

    def toPython(self):
        """
        返回python对象
        :return:
        """
        pass

    def __str__(self):
        """
        标准输出
        :return:
        """
        return self.toJson()

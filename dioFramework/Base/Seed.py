# @Time         : 18-3-12 下午9:31
# @Author       : DioMryang
# @File         : Seed.py
# @Description  : 元素种子


class Seed(object):
    """
    爬虫架构基本元素, 种子

    Attribute:
        data: 信息
        depth: 爬虫深度
        type: 爬虫类型, seed, data,

    Method:
        getInfo: 获取Info
        getDepth: 获取深度
        getType: 获取类型
        setDepth: 设置爬虫种子深度
        inicDepth: 种子深度 +1
        updateData: 更新data
    """
    def __init__(self, data, type_):
        self.data = data
        self.type_ = type_
        self.depth = 0

    def setDepth(self, depth):
        """
        设置种子深度
        :param depth: 深度
        :return:
        """
        self.depth = depth

    def inicDepth(self):
        """
        种子深度 +1
        :return:
        """
        self.depth += 1

    def updateData(self, data):
        """
        更新 data
        :param data: 额外数据
        :return: 
        """
        self.data.update(data)


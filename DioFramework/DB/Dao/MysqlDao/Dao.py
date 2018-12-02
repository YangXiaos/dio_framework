# @Time         : 18-7-8 下午3:16
# @Author       : DioMryang
# @File         : Dao.py
# @Description  : dao 层封装

from DioFramework.DB.Const import Connection


class Dao(object):
    """
    接口
    """

    @staticmethod
    def save():
        """
        保存当前提交
        :return:
        """
        Connection.MYSQL_DEFAULT.commit()

    @classmethod
    def getById(cls, _id):
        """
        通过 id获取
        :param _id: id
        :return:
        """
        return Connection.MYSQL_DEFAULT.query(cls).filter(cls.id == _id).one()


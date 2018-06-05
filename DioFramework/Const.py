# @Time         : 18-3-12 下午9:56
# @Author       : DioMryang
# @File         : Const.py
# @Description  :
from enum import Enum, unique


@unique
class SeedType(Enum):
    """
    种子类型

    link 用于继续跑数的种子
    content 已经获取数据的种子
    linkAndContent 用于跑数且插入数据的种子
    """
    link = 1
    content = 2
    linkAndContent = 3


MYSQL_CONFIG = {"driver": "pymysql",
                "user": "root",
                "password": "123456",
                "host": "localhost",
                "port": "3306",
                "db_name": "dio"}

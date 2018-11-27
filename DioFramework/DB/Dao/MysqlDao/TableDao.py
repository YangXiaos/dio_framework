# @Time         : 18-6-5 下午9:26
# @Author       : DioMryang
# @File         : TableDao.py
# @Description  :
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from DioFramework.DB.Dao.MysqlDao.Dao import Dao


class Table(declarative_base(), Dao):
    """
    数据库写入表 接口
    """
    __tablename__ = 'dio.table'

    id = Column(Integer, primary_key=True, autoincrement=True)
    table_name = Column(String)
    db_type = Column(String)
    writer = Column(Integer)
    fields = Column(String)

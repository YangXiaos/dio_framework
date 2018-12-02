# @Time         : 18-6-5 下午9:05
# @Author       : DioMryang
# @File         : ProcessorDao.py
# @Description  : 处理器数据库接口
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from DioFramework.DB.Dao.MysqlDao.Dao import Dao


class ProcessorDao(declarative_base(), Dao):
    """
    处理器接口
    """
    __tablename__ = 'dio.processor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_path = Column(String)
    desc = Column(String)




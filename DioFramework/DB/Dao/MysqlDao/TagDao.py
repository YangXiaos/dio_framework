# @Time         : 18-6-5 下午10:51
# @Author       : DioMryang
# @File         : TagDao.py
# @Description  :

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from DioFramework.DB.Dao.MysqlDao.Dao import Dao


class Tag(declarative_base(), Dao):
    """
    模板配置 数据库接口
    """
    __tablename__ = 'dio.tag'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

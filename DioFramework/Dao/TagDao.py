# @Time         : 18-6-5 下午10:51
# @Author       : DioMryang
# @File         : TagDao.py
# @Description  :

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


class TemplateConfigDao(declarative_base()):
    """
    模板配置 数据库接口
    """
    __tablename__ = 'dio.table'

    id = Column(Integer, primary_key=True, autoincrement=True)
    desc = Column(String)
    type = Column(String)
    site_ids = Column(String)
    spider_config = Column(String)

    match_config = Column(Integer)


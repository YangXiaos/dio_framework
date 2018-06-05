# @Time         : 18-6-5 下午9:26
# @Author       : DioMryang
# @File         : TableDao.py
# @Description  :
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


class TableDao(declarative_base()):
    """
    数据库写入表 接口
    """
    __tablename__ = 'dio.table'

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(String)
    template_ids = Column(String)
    state = Column(String)
    report = Column(String)

    crawl_num = Column(Integer)
    fail_num = Column(Integer)
    link_num = Column(Integer)
    content_num = Column(Integer)

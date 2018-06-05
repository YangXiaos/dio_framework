# @Time         : 18-6-5 下午9:16
# @Author       : DioMryang
# @File         : JobDao.py
# @Description  :
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


class JobDao(declarative_base()):
    """
    作业 接口
    """
    __tablename__ = 'dio.job'

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(String)
    template_ids = Column(String)
    state = Column(String)
    report = Column(String)

    crawl_num = Column(Integer)
    fail_num = Column(Integer)
    link_num = Column(Integer)
    content_num = Column(Integer)

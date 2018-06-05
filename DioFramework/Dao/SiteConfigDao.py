# @Time         : 18-5-26 下午8:01
# @Author       : DioMryang
# @File         : SiteConfigDao.py
# @Description  :
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


class SiteConfig(declarative_base()):

    __tablename__ = 'dio.site.config'
    id = Column(Integer, primary_key=True, autoincrement=True)
    desc = Column(String)
    domain = Column(String)
    parend_id = Column(Integer)
    tag = Column(String)
    status = Column(Integer, default=0)


if __name__ == '__main__':
    from DioFramework import Const
    from DioCore.DB import MysqlUnit
    conn = MysqlUnit.createConnect(**Const.MYSQL_CONFIG)

    site = SiteConfig(desc="baidu - 导航页", domain="baidu.com", parend_id=None, tag=0, status=0)
    conn.add(site)
    conn.commit()
    conn.close()
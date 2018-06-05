# @Time         : 18-6-3 下午9:14
# @Author       : DioMryang
# @File         : TaskConfigDao.py
# @Description  :


from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from DioFramework import Const
from DioCore.Units import JsonUnit

class TaskConfig(declarative_base()):

    __tablename__ = 'dio.task.config'

    id = Column(Integer, primary_key=True, autoincrement=True)
    site_ids = Column(String)
    spider_config = Column(String)
    job_config = Column(String)
    status = Column(String, default=0)
    template_ids = Column(String)
    desc = Column(String)
    type = Column(String, default="incr")
    cycle_time = Column(Integer, default=20)

    def getSpiderConfig(self):
        """获取json"""
        return JsonUnit.formJson(self.job_config)


if __name__ == '__main__':
    from DioCore.DB import MysqlUnit
    conn = MysqlUnit.createConnect(**Const.MYSQL_CONFIG)

    task = TaskConfig(desc="baidu - 站点", spider_config="[{\"1\": \"type\"}]",
                      job_config="{\"1\": \"type\"}", template_ids="1,2", type="incr", site_ids="1", status=0)
    conn.add(task)
    conn.commit()
    print(task.getSpiderConfig())
    conn.close()

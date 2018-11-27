# @Time         : 18-6-3 下午9:14
# @Author       : DioMryang
# @File         : TaskConfigDao.py
# @Description  :
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from DioCore.Units import JsonUnit
from DioFramework.DB.Dao.MysqlDao.Dao import Dao
from DioFramework.DB.Dao.MysqlDao.TemplateConfigDao import TemplateConfig


class TaskConfig(declarative_base(), Dao):

    __tablename__ = 'dio.task.config'

    id = Column(Integer, primary_key=True, autoincrement=True)
    site_ids = Column(String)

    job_processor_params = Column(String)
    message_processor_config = Column(String)
    job_params = Column(String)

    is_available = Column(String, default=0)
    template_ids = Column(String)
    desc = Column(String)
    type = Column(String, default="incr")
    cycle_time = Column(Integer, default=20)

    def getMessageProcessorConfig(self) -> list:
        """获取json"""
        return JsonUnit.toPython(self.message_processor_config)

    def getJobProcessorParams(self) -> list:
        """获取jobConfig json"""
        return JsonUnit.toPython(self.job_processor_params)

    def getTemplateIdConfigMapping(self) -> dict:
        """获取模板 id 配置 匹配"""
        return {int(_id.strip()): TemplateConfig.getById(int(_id.strip()))
                for _id in self.template_ids.split(",") if _id.isdigit()}

    def getJobParams(self) -> dict:
        """获取job的参数"""
        return JsonUnit.toPython(self.job_params)


if __name__ == '__main__':
    from DioCore.DB import MysqlUnit
    from DioFramework import Const

    conn = MysqlUnit.createConnect(**Const.MYSQL_CONFIG)

    task = TaskConfig(desc="baidu - 站点", spider_config="[{\"1\": \"type\"}]",
                      job_config="{\"1\": \"type\"}", template_ids="1,2", type="incr", site_ids="1", status=0)
    conn.add(task)
    conn.commit()
    print(task.getSpiderConfig())
    conn.close()

# @Time         : 18-6-5 下午9:29
# @Author       : DioMryang
# @File         : TemplateConfigDao.py
# @Description  :
from sqlalchemy.ext.declarative import declarative_base

from DioCore.Units import JsonUnit
from sqlalchemy import Column, String, Integer

from DioCore.Units.ModuleUnit import loadClass
from DioFramework.DB.Dao.MysqlDao.Dao import Dao
from DioFramework.DB.Dao.MysqlDao.ProcessorDao import ProcessorDao


class TemplateConfig(declarative_base(), Dao):
    """
    模板配置 数据库接口
    """
    __tablename__ = 'dio.table'

    id = Column(Integer, primary_key=True, autoincrement=True)
    desc = Column(String)
    type = Column(String)
    site_ids = Column(String)

    template_component_config = Column(String)
    message_match_strategy_config = Column(Integer)

    def getTemplateComponentConfig(self) -> list:
        """获取模板 config"""
        return JsonUnit.toPython(self.template_component_config)

    def getComponentList(self) -> list:
        """
        获取组件列表
        :return:
        """
        tpCpCfgList = self.getTemplateComponentConfig()
        for cpCfg in tpCpCfgList:
            cpClassPath = ProcessorDao.getById(cpCfg.get("id", )).class_path
            cls = loadClass(cpClassPath)
            yield cls(cofig=cpCfg, tpId=self.id, desc=self.desc, type=self.type)

    def getMessageMatchStrategyConfig(self) -> dict:
        """获取 message 匹配策略"""
        return JsonUnit.toJson(self.message_match_strategy_config)

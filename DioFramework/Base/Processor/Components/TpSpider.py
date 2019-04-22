# @Time         : 18-6-6 下午9:04
# @Author       : DioMryang
# @File         : TpSpider.py
# @Description  :
from DioCore.Utils import JsonUtil

from DioFramework.Base.Processor.Processor import Processor
from DioFramework.DB.Dao.MysqlDao import TemplateConfigDao


class TpSpider(Processor):
    """
    模板加载处理器

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger.info("load {} {}: {}".format(TpSpider.__name__, self.pid, str(self.config)))

        conn = kwargs.get("runner").conn
        tp = conn.query(TemplateConfigDao).filter(TemplateConfigDao.id == self.pid).one()

        self.spiderConfig = JsonUtil.toPython(tp.spider_config)
        self.matchConfig = JsonUtil.toPython(tp.match_config)

        self.components = []

    def match(self):
        """
        匹配模板
        :return:
        """

    def run(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        seeds = kwargs.get("seeds", [])
        self.logger.info("handle seeds {}".format(seeds.seedString))

        for component in self.components:
            pass


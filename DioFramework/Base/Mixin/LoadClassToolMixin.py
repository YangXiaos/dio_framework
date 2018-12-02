# @Time         : 18-7-29 下午1:37
# @Author       : DioMryang
# @File         : LoadClassToolMixin.py
# @Description  :
from DioCore.Utils.ModuleUtil import loadClass

from DioFramework.DB.Dao.MysqlDao.ProcessorDao import ProcessorDao


class LoadClassToolMixin(object):
    """
    处理器工具函数 Mixin
    """

    @staticmethod
    def loadProcessorCls(pid: int):
        """
        加载处理器
        :param pid: 处理器id
        :return:
        """
        return loadClass(ProcessorDao.getById(pid).class_path)

    @staticmethod
    def loadProcessorByConfig(config: dict, **kwargs):
        """
        根据配置
        :param kwargs:
        :param config:
        :return:
        """
        cls = loadClass(ProcessorDao.getById(config.get("id")).class_path)
        return cls(config=config, **kwargs)

    @staticmethod
    def initObjByConfig(config: dict):
        """
        通过配置参数，初始化对象

        可序列化的对象配置
        ```
        {
            "class_name": "queue",  # 加载的类路径
            "params": {...}         # 初始化对象参数
        }
        ```
        :param config: 对象参数
        :return:
        """
        cls = loadClass(config.get("class_name"))
        params = config.get("params", {})
        return cls(params=params)


if __name__ == '__main__':

    cfg = {
        "id": 1,
        "params": {
            "waiting_time": 5,
            "runner_job_match_name": "dio.crawler.runner.job"
        }
    }
    LoadClassToolMixin.loadProcessorByConfig(cfg)

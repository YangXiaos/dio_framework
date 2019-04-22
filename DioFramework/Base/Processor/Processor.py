# @Time         : 18-3-12 下午9:31
# @Author       : DioMryang
# @File         : Processor.py
# @Description  :
import logging


from DioFramework.Base.Mixin.LoadClassToolMixin import LoadClassToolMixin


class Processor(LoadClassToolMixin):
    """
    处理器通用继承类

    处理json配置：
    ```
    {
        "id": 1,                        # 处理器对应id
        "before_middleware": [2, 3, 4], # 处理前 middle 对应id数组
        "after_middleware": [5, 6, 7]   # 处理后 middle 对应id数组
        "params": {...}                 # 处理器参数
    }
    ```

    MetaClass:
        LoadClassToolMixin:

    Attributes:
        `logger`: logger
        `config`: 配置参数
        `pid`: 处理器id
        `params`: 处理器参数

    Methods:
        `execute`: 内置初始跑数函数
        `run`: 处理器的主要处理逻辑函数
        `beforeRun`: 跑数之前的加载处理
        `afterRun`: 跑数之后的加载处理
        `handleError`: 处理跑数异常
    """

    # 处理器初始化format
    processorInitFormat = "load {} {}: {}"

    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.config = kwargs.get("config", {})
        self.params = self.config.get("params", {})
        self.pid = self.config.get("id", -1)

        # 打印处理器初始化
        self.logger.info(self.processorInitFormat.format(self.__class__.__name__, self.pid, str(self.config)))

    def execute(self, *args, **kwargs):
        """
        程序默认运行函数
        :param args:
        :param kwargs:
        :return:
        """
        try:
            self.beforeExecute(*args, **kwargs)
            result = self.run(*args, **kwargs)
            self.afterExecute(result, *args, **kwargs)
        except Exception as e:
            self.handleError(error=e, *args, **kwargs)
            raise e
        return result

    def run(self, *args, **kwargs):
        """
        处理标准数据流函数
        :return:
        """
        pass

    def beforeExecute(self, *args, **kwargs):
        """
        Middleware插入位置
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def afterExecute(self, *args, **kwargs):
        """
        处理器
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def handleError(self, *args, **kwargs):
        """
        处理异常middleware
        :param args:
        :param kwargs:
        :return:
        """
        self.logger.error(kwargs.get("error").__class__.__name__)


if __name__ == '__main__':
    class DioProcessor(Processor):
        pass

    dio = DioProcessor("喵喵")

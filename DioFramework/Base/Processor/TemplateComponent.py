# @Time         : 18-6-6 下午9:05
# @Author       : DioMryang
# @File         : TemplateComponent.py
# @Description  :
from DioFramework.Base.Processor import Processor


class TemplateComponent(Processor):
    """
    爬虫模板 组件
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.templateLoader = kwargs.get("templateLoader")
        self.desc = self.templateLoader.desc
        self.type = self.templateLoader.type
        self.tpId = self.templateLoader.tpId

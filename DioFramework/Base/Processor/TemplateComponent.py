# @Time         : 18-6-6 下午9:05
# @Author       : DioMryang
# @File         : TemplateComponent.py
# @Description  :
from DioFramework.Base.Processor.Processor import Processor


class TemplateComponent(Processor):
    """
    爬虫模板 组件
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tpDesc = self.config.get("tpDesc")
        self.tpType = self.config.get("tpType")
        self.tpId = self.config.get("tpId")

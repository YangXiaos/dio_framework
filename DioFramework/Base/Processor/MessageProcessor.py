# @Time         : 18-6-25 下午10:21
# @Author       : DioMryang
# @File         : SpiderProcessor.py
# @Description  :
from DioFramework.Base.Processor.Processor import Processor


class MessageProcessor(Processor):
    """
    爬虫模板 组件
    """
    def __init__(self, *args, **kwargs):
        super(MessageProcessor, self).__init__(*args, **kwargs)



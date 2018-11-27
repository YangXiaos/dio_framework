# @Time         : 18-7-12 下午11:37
# @Author       : DioMryang
# @File         : MessageFilter.py
# @Description  :
from DioFramework.Base.Processor.MessageProcessor import MessageProcessor


class MessageFilter(MessageProcessor):
    """
    message 过滤器


    """
    def __init__(self, **kwargs):
        super(MessageFilter, self).__init__(**kwargs)
        # self.


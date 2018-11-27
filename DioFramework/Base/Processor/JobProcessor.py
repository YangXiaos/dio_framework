# @Time         : 18-6-25 下午10:17
# @Author       : DioMryang
# @File         : JobProcessor.py
# @Description  :
from DioFramework.Base.Processor.Processor import Processor


class JobProcessor(Processor):
    """
    job 处理器
    """
    def __init__(self, *args, **kwargs):
        super(JobProcessor, self).__init__(*args, **kwargs)
        self.processorLevel = "job"


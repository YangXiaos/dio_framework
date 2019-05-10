from DioFramework.Base.Processor.JobProcessor.JobProcessor import JobProcessor
from DioFramework.DB.Dao.MysqlDao.TaskConfigDao import TaskConfig


class JobInitProcessor(JobProcessor):
    """
    job 初始化处理器


    """
    def __init__(self, *args, **kwargs):
        super(JobInitProcessor, self).__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        TaskConfig.getById()

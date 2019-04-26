# @Time         : 18-7-29 下午5:33
# @Author       : DioMryang
# @File         : JobFinishProcessor.py
# @Description  :
from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Processor.JobProcessor import JobProcessor
from DioFramework.Const import JobState, RunnerState


class JobFinishProcessor(JobProcessor):
    """
    作业 结束 processor


    """
    def __init__(self, *args, **kwargs):
        super(JobFinishProcessor, self).__init__(*args, **kwargs)

    def run(self, job) -> Job:
        """
        释放资源
        :return:
        """
        job.setJobState(JobState.OVER)
        job.setRunnerState(RunnerState.WAITING)
        return job

# @Time         : 18-6-9 上午11:35
# @Author       : DioMryang
# @File         : JobSeedReader.py
# @Description  :
from typing import Union, Dict

from DioCore.DB.RedisClient import Hash
from DioCore.Utils import TimeUtil

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Processor.JobProcessor import JobProcessor
from DioFramework.Const import RunnerState, JobState
from DioFramework.DB.Const import Connection


class JobSeedReader(JobProcessor):
    """
    Job 读取 处理器

    循环查看 runnerJob 是否分配job
    ```
    {
        "id" : 2,
        "params": {
            "waiting_time": 5,
            "runner_job_match_name": "dio.crawler.runner.job"
        }
    }
    ```

    MetaClass:
        DioFramework.Base.Processor.JobProcessor.JobProcessor

    Attributes:
        `id`: 2
        `config`:
        `params`:
        `waiting_time`: 重复读取时间
        `runner_job_match_name`: runner_job_match_name匹配名

    """
    def __init__(self, *args, **kwargs):
        super(JobSeedReader, self).__init__(*args, **kwargs)

        self.waitingTime = self.params.get("waiting_time", )
        self.runnerJobMatchName = self.params.get("runner_job_match_name", )

    def run(self, job: Union[Job, Dict[str, str]]) -> Job:
        """
        跑数
        :param job:
        :return:
        """
        runnerId = job.get("runner_id")

        while True:
            # 获取json
            runnerJobMatch = Hash(Connection.REDIS_DEFAULT, self.runnerJobMatchName)
            jobJsonStr = runnerJobMatch.hget(runnerId)

            # 生成job
            if job is not None:
                job = Job.form(jobJsonStr)
                job.runnerId = runnerId

                self.logger.info("{} get job {}".format(runnerId, jobJsonStr))

                # 设置runner，job 状态
                job.setRunnerState(RunnerState.RUNNING)
                job.setJobState(JobState.RUNNING)
                return job

            # 暂停数秒
            TimeUtil.sleep(self.waitingTime)


if __name__ == '__main__':
    cfg = {
        "id": 1,
        "params": {
            "waiting_time": 5,
            "runner_job_match_name": "dio.crawler.runner.job"
        }
    }
    JobSeedReader(config=cfg)

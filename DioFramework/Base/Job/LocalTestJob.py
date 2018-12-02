# @Time         : 18-9-8 下午5:56
# @Author       : DioMryang
# @File         : LocalSpiderJob.py
# @Description  :
from queue import Queue

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Job.ThreadStateManager import CacheThreadStateManager


class LocalTestJob(Job):
    """
    爬虫任务作业种子

    Job 序列化格式
    {
        "job_id": "xxxxx",      # jobId
        "task_id": 3,        # task id
        "site_id": 3,        # site id
        "runner_id": "cio-1",# runner id

        "record": {                         # 爬虫记录
            "cio1-1": {                     # runnerId + 线程id
                "crawl_num": 0,             # 输入种子数
                "output_crawl_num": 0,      # 输出种子数
                "crawl_fail_num": 1,        # 种子失败数
                "crawl_success_num": 2,     # 种子成功数
                "link_num": 3,              # link类型种子
                "content_num": 4,           # 内容类型种子
                "filter_num": 5             # 过滤掉的种子数
            }
        },

        "init_msgs": [...]                   # 初始化msg
        "state": "waiting",                 # job state
        "createTime": "20141218072222",     # 创建时间
        "startTime": "20141218072222",      # 开始处理时间
        "endTime": "20141218072222"         # 结束时间
    }

    Attributes:
        `jobId`: 爬虫job名
        `queue`: 队列类 queue.Queue
        `seeds`: 种子数

        `record`: 记录Hash
        `taskId`:  任务id
        `taskConfig`: 当前Job的任务配置

        `runnerId`: 当前 job 分配到的 runnerId
        `runnerConfig`: 爬虫配置
        `record`： 爬虫作业线程记录
        `state`： 爬虫作业状态, waiting, running, finish, killed

        `createTime`: 爬虫job创建时间
        `startTime`: 爬虫job跑数时间
        `endTime`: 爬虫job结束时间

    GlobalAttributes:

    """

    def __init__(self, **kwargs):
        super(LocalTestJob, self).__init__(**kwargs)
        self.queue = Queue()
        self.threadStateManager = CacheThreadStateManager()

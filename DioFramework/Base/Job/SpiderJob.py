# @Time         : 18-9-8 下午5:56
# @Author       : DioMryang
# @File         : SpiderJob.py
# @Description  :

from DioCore.Utils import JsonUtil
from DioCore.Utils import DateTimeUtil
from DioFramework.Base.Distributor.CommonDistributor import CommonDistributor

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.TemplateLoader.TemplateLoader import TemplateLoader
from DioFramework.Const import JobState, RunnerState
from DioFramework.DB.Const import Connection, RedisKey
from DioFramework.DB.Dao.MysqlDao.JobDao import Job as JobORM
from DioFramework.DB.Dao.MysqlDao.TaskConfigDao import TaskConfig
from DioFramework.DB.Dao.RedisInterface import Interface


class SpiderJob(Job):
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
        super(SpiderJob, self).__init__(**kwargs)

        self.taskConfig = TaskConfig.getById(self.taskId)
        self.templateIdConfigMapping = self.taskConfig.getTemplateIdConfigMapping()

        # 获取job 参数
        self.jobParams = self.taskConfig.getJobParams()

        # 设置内存队列,线程状态管理器,分发处理器,
        self.queue = self.initObjByConfig(self.jobParams.get("queue_config"))
        self.threadStateManager = self.initObjByConfig(self.jobParams.get("thread_state_manager_config"))
        self.templateLoaderMapping = {tpId: TemplateLoader(templateCfg)
                                      for tpId, templateCfg in self.taskConfig.getTemplateIdConfigMapping().items()}
        self.distributor = self.initObjByConfig(self.jobParams.get("distributor_config"))

        # 将队列插入队列
        for msg in self.initMsgs:
            self.queue.put(msg)

    def setQueue(self, queue):
        """
        设置任务队列
        :param queue: 跑数队列
        :return:
        """
        self.queue = queue

    def finish(self):
        """
        结束
        :return:
        """

    def toPython(self):
        """
        转化为字典形态
        :return: 返回字典形态的对象
        """
        return {
            "id": self.id,
            "task_id": self.taskId,
            "site_id": self.siteId,
            "runner_id": self.runnerId,
            "state": self.state,

            "create_time": self.createTime,
            "start_time": self.startTime,
            "end_time": self.endTime
        }

    def getFormatParams(self) -> dict:
        """获取渲染参数"""
        return {"job_id": self.id, "task_id": self.taskId, "site_id": self.siteId, "runner_id": self.runnerId}

    @classmethod
    def form(cls, json: str):
        """序列化"""
        params = JsonUtil.toPython(json)
        kwargs = {
            "id": params["job_id"],
            "taskId": params["task_id"],
            "siteId": params["site_id"],
            "state": params["state"],

            "createTime": params["create_time"],
            "startTime": params["start_time"],
            "endTime": params["end_time"],
            "runnerId": params["runner_id"],
            "initMsgs": params["init_msgs"]
        }
        return cls(**kwargs)

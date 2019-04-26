# @Time         : 18-6-13 下午9:54
# @Author       : DioMryang
# @File         : Job.py
# @Description  :
import uuid

from DioCore.Utils import JsonUtil
from DioCore.Utils import DateTimeUtil
from DioFramework.Base.Message import Message
from DioFramework.Base.Mixin.LoadClassToolMixin import LoadClassToolMixin
from DioFramework.Base.Mixin.StandardizeMixin import StandardizeMixin
from DioFramework.Const import JobState


class Job(StandardizeMixin, LoadClassToolMixin):
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
    def __init__(self, id="", taskId=-1, siteId=-1, runnerId=-1, state=JobState.WAITING,
            createTime="", startTime="", endTime="", initMsgs=None):
        self.id = uuid.uuid4().__str__() if id is "" else id

        self.state = state
        self.siteId = siteId
        self.taskId = taskId
        self.runnerId = runnerId

        self.createTime = DateTimeUtil.getCurStandardDate() if createTime is "" else createTime
        self.startTime = DateTimeUtil.getCurStandardDate() if startTime is "" else startTime
        self.endTime = endTime

        self.threadStateManager = None
        self.templateLoaderMapping = {}
        self.distributor = None

        # 初始化种子
        self.initMsgs = []
        for msg in initMsgs if initMsgs is not None else []:
            if isinstance(msg, dict):
                self.initMsgs.append(Message(**msg))
            elif isinstance(msg, Message):
                self.initMsgs.append(msg)
            else:
                raise TypeError("error Message type".format(msg.__class__.__name__))

        self.queue = None
        self.context = {
            "create_time": self.createTime,
            "start_time": self.startTime,

        }

    # def setDistributor(self, distributor: ):


    def setTemplateLoaderMapping(self, tpMapping: dict):
        """设置模板匹配"""
        self.templateLoaderMapping = tpMapping

    def setQueue(self, queue):
        """设置任务队列"""
        self.queue = queue

    def finish(self):
        """结束"""
        self.state = JobState.FINISH
        self.endTime = DateTimeUtil.getCurStandardDate()

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

    def toJson(self):
        """
        返回 json字符串形式
        :return:
        """
        return JsonUtil.toJson(self.toPython())


if __name__ == '__main__':
    job = Job()
    print(job.toJson())

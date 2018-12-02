# @Time         : 18-3-12 下午9:56
# @Author       : DioMryang
# @File         : Const.py
# @Description  :


class SeedType(object):
    """
    种子类型

    link 用于继续跑数的种子
    content 已经获取数据的种子
    linkAndContent 用于跑数且插入数据的种子
    """
    link = 0
    content = 1
    linkAndContent = 2


class JobQueueType(object):
    """
    job 队列类型
    """
    cache = "cache"
    redis = "redis"


class JobState(object):
    """
    作业状态

    WAITING: 等待状态
    RUNNING: 跑数状态
    FINISH: 结束
    KILLED: 任务被强制结束
    """
    WAITING = "WAITING"
    RUNNING = "RUNNING"
    OVER = "OVER"
    FINISH = "FINISH"
    KILLED = "KILLED"


class RunnerState(object):
    """
    跑数状态
    """
    WAITING = "WAITING"
    RUNNING = "RUNNING"


class JobThreadState(object):
    """
    作业进程状态
    """
    RUNNING = "RUNNING"
    OVER = "OVER"


# 默认mysql 配置
DEFAULT_MYSQL_CONFIG = {
    "driver": "pymysql",
    "user": "root",
    "password": "123456",
    "host": "localhost",
    "port": "3306",
    "db_name": "dio"
}


# 默认mongodb 配置
DEFAULT_MONGODB_CONFIG = {
}


# 默认redis 配置
DEFAULT_REDIS_CONFIG ={
    "host": "localhost",
    "port": 6379
}


#
class MSG_FIELD(object):

    ENTER_URL = "enter_url"
    URL = "url"
    SPIDER_NAME = "__spider__"
    CONTENT = "content"


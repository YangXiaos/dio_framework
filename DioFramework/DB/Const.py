# @Time         : 18-6-24 下午5:37
# @Author       : DioMryang
# @File         : Const.py.py
# @Description  :

from DioCore.DB import MysqlUtil, MongoUtil, RedisUtil
from DioFramework.Const import DEFAULT_MYSQL_CONFIG, DEFAULT_MONGODB_CONFIG, DEFAULT_REDIS_CONFIG


class Connection(object):
    """
    数据库连接
    """
    MYSQL_DEFAULT = MysqlUtil.createConnect(**DEFAULT_MYSQL_CONFIG)
    MONGODB_DEFAULT = MongoUtil.createConnect(**DEFAULT_MONGODB_CONFIG)
    REDIS_DEFAULT = RedisUtil.createConnect(**DEFAULT_REDIS_CONFIG)


class RedisKey(object):
    """
    redis 键名
    """
    # scheduler key name
    AynSeedsSet = "dio.scheduler.task.async.queue"     # 提交异步任务信息队列
    IncTaskRecordHash = "dio.scheduler.task.inc.record"     # 增量任务的 {任务id: 时间戳}

    # crawler key name
    GlobalFilterSet = "dio.crawler.global.seeds.set"        # 全局级别过滤列表
    SiteFilterSet = "dio.crawler.site.seeds.set.{site_id}"  # 站点级别过滤列表
    TaskFilterSet = "dio.crawler.task.seeds.set.{task_id}"  # 任务级别过滤列表

    # runner key name
    RunnerStateHash = "dio.crawler.runner.state"            # runner的状态
    RunnerJobHash = "dio.crawler.runner.job"                # runner 分配的jobId

    # 任务种子队列,job state
    JobSeedsSet = "dio.{job_id}.seeds"        # 作业种子队列

    # job 进度监控
    JobThreadStateHash = "dio.job.thread.state.{job_id}"        # job线程状态


if __name__ == '__main__':
    import logging

    logger = logging.getLogger('dio')
    logger.setLevel(logging.DEBUG)

    conn = Connection.MYSQL_DEFAULT
    print(id(conn))
    conn = Connection.MYSQL_DEFAULT
    print(id(conn))


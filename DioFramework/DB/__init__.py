# @Time         : 18-7-29 下午9:19
# @Author       : DioMryang
# @File         : __init__.py
# @Description  :


# inc 任务 记录
from DioCore.DB import RedisClient

from DioFramework.DB.Const import Connection, RedisKey


class RedisKey(object):
    # 增量
    IncTaskRecord = RedisClient.Hash(Connection.REDIS_DEFAULT, RedisKey.IncTaskRecordHash)

    # runner 的状态
    RunnerState = RedisClient.Hash(Connection.REDIS_DEFAULT, RedisKey.RunnerStateHash)

    # runner 的分配job
    RunnerJob = RedisClient.Hash(Connection.REDIS_DEFAULT, RedisKey.RunnerJobHash)

    # job 的进度状态 key
    # JobState = RedisClient.Hash(Connection.REDIS_DEFAULT, RedisKey.JobStateHash)

    # 去重集合
    GlobalFilter = RedisClient.Set(Connection.REDIS_DEFAULT, RedisKey.GlobalFilterSet)

    AynSeed = RedisClient.Set(Connection.REDIS_DEFAULT, RedisKey.AynSeedsSet)
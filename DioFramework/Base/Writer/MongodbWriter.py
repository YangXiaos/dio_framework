# @Time         : 18-8-22 下午10:13
# @Author       : DioMryang
# @File         : MongodbWriter.py
# @Description  :
from typing import List

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Writer.BaseWriter import BaseWriter
from DioFramework.DB.Const import Connection


class MongodbWriter(BaseWriter):
    """
    mongodb 分发
    {
        "db_name": "db",
        "collection_name": "coll"
    }
    """
    def __init__(self, **kwargs):
        super(MongodbWriter, self).__init__(**kwargs)
        self.connection = Connection.MONGODB_DEFAULT
        self.dbName = self.params.get("db_name")
        self.collectionName = self.params.get("collection_name")
        self.collection = self.connection[self.dbName][self.collectionName]

    def write(self, job: Job, message: Message):
        self.logger.info(" mongodb writer distribute {}".format(message.info))
        self.collection.insert_one(message.info)

    def writeMany(self, job: Job, messages: List[Message]):
        for message in messages:
            self.logger.info(" mongodb writer distribute {}".format(message.info))
            self.collection.insert_one(message.info)

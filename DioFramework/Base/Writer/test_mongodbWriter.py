# @Time         : 18-8-22 下午10:37
# @Author       : DioMryang
# @File         : test_mongodbWriter.py
from unittest import TestCase

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Writer.MongodbWriter import MongodbWriter
from DioFramework.Const import SeedType


class TestMongodbWriter(TestCase):
    def test_write(self):
        msg = Message(info={"name": "mryang", "age": "18"}, type=SeedType.content)
        job = Job(id="xxxxxx")

        params = {
            "job": job,
            "db_name": "dio",
            "collection_name": "person"
        }

        w = MongodbWriter(**params)
        w.write(msg)

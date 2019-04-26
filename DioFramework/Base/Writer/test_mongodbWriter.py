# @Time         : 18-8-22 下午10:37
# @Author       : DioMryang
# @File         : test_mongodbWriter.py
import logging
from unittest import TestCase

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Writer.MongodbWriter import MongodbWriter
from DioFramework.Const import SeedType


logging.basicConfig(level=logging.INFO, format="[%(asctime)s]-[%(name)s]-[%(levelname)s]: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")
def test_write():
    job = Job(id="xxxxxx")
    msg = Message(info={"name": "mryang", "age": "18"}, type=SeedType.content)

    params = {
        "db_name": "dio",
        "collection_name": "person"
    }

    w = MongodbWriter(params=params)
    w.write(job, msg)


if __name__ == '__main__':
    test_write()
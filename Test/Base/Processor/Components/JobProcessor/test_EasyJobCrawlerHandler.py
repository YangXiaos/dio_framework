import logging

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message
from DioFramework.Base.Processor.JobProcessor import EasyJobCrawlerHandler
from DioFramework.Const import MSG_FIELD


logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] : [%(asctime)s] : %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def test_EasyJobCrawlerHandler():
    jobProcessor = EasyJobCrawlerHandler(config={
        "id": "3",
        "params": {
            "spiders": [
                "DioSpider.OldSpider.Boss.BossSearchSpider.BossSearchSpider",
                "DioSpider.OldSpider.Boss.BossJobSpider.BossJobSpider"
            ],
            "writer": {
                "id": 2,
                "params": {
                    "db_name": "db",
                    "collection_name": "boss"
                }
            }
        }
    })
    msg = Message(info={MSG_FIELD.ENTER_URL: "https://www.zhipin.com/c101280100/?query=%E7%88%AC%E8%99%AB&period=3&ka=sel-scale-3"})

    job = Job(initMsgs=[msg])
    jobProcessor.execute(job)


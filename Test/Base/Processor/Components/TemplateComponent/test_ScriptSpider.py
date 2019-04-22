from DioFramework.Base.Message import Message
from DioFramework.Base.Processor.Components.TemplateComponent.ScriptSpider import ScriptSpider
from Test.Example import testJob
from Test.TestUtil import pretty


def test_ScriptSpider():
    cfg = {
        "id": 15,
        "params": {
            "spider": {             # spider 配置
                "class_name": "DioSpider.OldSpider.Boss.BossJobSpider.BossJobSpider",
                "params": {}
            }
        }
    }

    spider = ScriptSpider(config=cfg)
    for msg in spider.run(testJob, [Message(info={"enter_url": "https://www.zhipin.com/job_detail/3265d372b1182c951HR50t2-ElU~.html"})]):
        pretty(msg)



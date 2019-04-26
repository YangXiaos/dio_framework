from Test import TestUtil

from DioFramework.Base.Message import Message
from DioFramework.Base.TemplateLoader.TemplateLoader import TemplateLoader
from DioFramework.Const import MSG_FIELD
from DioFramework.DB.Dao.MysqlDao.TemplateConfigDao import TemplateConfig
from Test.Example import testJob

from DioFramework.Base.Processor.MessageProcessor.TemplateSpider import TemplateSpider


def test_run():
    testJob.setTemplateLoaderMapping({
        "-2": TemplateLoader(TemplateConfig.getById(-2))
    })
    testMsg = Message(info={MSG_FIELD.ENTER_URL: "https://www.zhipin.com/job_detail/3265d372b1182c951HR50t2-ElU~.html"})
    for msg in TemplateSpider().execute(testJob, [testMsg]):
        TestUtil.pretty(msg)


def test_TemplateSpider():
    pass
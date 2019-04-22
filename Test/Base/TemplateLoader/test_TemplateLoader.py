from Test.TestUtil import pretty

from Test.Example import testJob

from DioFramework.Base.Message import Message
from DioFramework.Const import MSG_FIELD
from DioFramework.DB.Dao.MysqlDao.TemplateConfigDao import TemplateConfig
from build.lib.DioFramework.Base.TemplateLoader.TemplateLoader import TemplateLoader


def test_TemplateLoader():
    tpConfig = TemplateConfig.getById(-2)
    tp = TemplateLoader(tpConfig)
    testMsg = Message(info={MSG_FIELD.ENTER_URL: "https://www.zhipin.com/job_detail/3265d372b1182c951HR50t2-ElU~.html"})
    print(tp.match(testMsg))
    result = tp.execute(testJob, testMsg)
    pretty(result)


def test___init__():
    pass


def test_execute():
    pass
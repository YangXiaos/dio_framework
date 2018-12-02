# @Time         : 18-11-28 下午10:39
# @Author       : DioMryang
# @File         : Example.py
# @Description  :
import uuid

from DioFramework import Const
from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Message import Message

testMsg = Message(type=Message.CONTENT)
testMsg.updateInfo({Const.MSG_FIELD.ENTER_URL: "http://dio.com", Const.MSG_FIELD.CONTENT: "la la la test Done"})


testJob = Job(id="miao_miao_test")

testMsgs = [testMsg]
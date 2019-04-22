# @Time         : 19-2-10 上午11:34
# @Author       : DioMryang
# @File         : TestUtil.py
# @Description  :
import pprint

from typing import Union, List

from DioFramework.Base.Message import Message


def pretty(msgs: Union[Message, List[Message]]):
    pp = pprint.PrettyPrinter(indent=4)
    if isinstance(msgs, list):
        for _ in msgs:
            pp.pprint(_.getInsertData())
    else:
        pp.pprint(msgs.getInsertData())

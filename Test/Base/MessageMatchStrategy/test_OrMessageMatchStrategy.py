from DioFramework.Base.Message import Message
from DioFramework.Base.MessageMatchStrategy import OrMessageMatchStrategy


def test_OrMessageMatchStrategy():
    params = {
        "enter_url": {
            "partialRegex": "http://ent.ifeng.com/a/20181128/\d+_\d+.shtml"
        },
        "spider_ids": {
            "equal": "12321"
        }
    }

    msg = Message()
    msg.info["enter_url"] = "http://ent.ifeng.com/a/20181128/43142134_0.shtml"

    strategy = OrMessageMatchStrategy(params=params)
    print(strategy.match(msg))

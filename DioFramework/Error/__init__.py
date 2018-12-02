# @Time         : 18-5-14 下午9:54
# @Author       : DioMryang
# @File         : Const.py.py
# @Description  :


class EmptySeedsError(Exception):
    """
    无种子异常
    """
    pass


class CrawlFailError(Exception):
    """
    抓取失败异常
    """
    pass


class Over(Exception):
    """
    抓取结束
    """
    pass


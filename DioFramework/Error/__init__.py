# @Time         : 18-5-14 下午9:54
# @Author       : DioMryang
# @File         : __init__.py.py
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



# @Time         : 18-3-12 下午9:31
# @Author       : DioMryang
# @File         : Message.py
# @Description  : message

from DioFramework.Base.Mixin.StandardizeMixin import StandardizeMixin
from DioFramework.Const import SeedType, MSG_FIELD


class Message(StandardizeMixin):
    """
    爬虫处理 Message。

    序列化格式：
    ```
    {
        "type" : 0,     # msg 类型
        "depth" : 3,    # msg 经过模板处理深度
        "crawlerId" : 3,# msg 模板id
        "siteId" : 3,   # msg 站点id
        "taskId" : 3,   # msg 任务id
        "info" : {      # msg 带有的数据流
            "crawlerId": 1,         # 模板id
            "siteId": 1,
            "taskId": 1,
            "toIds": [1, 2, 3]      # 处理模板的id
            ...
        }
    }
    ```

    Attribute:
        `info`: 数据流
        `depth`: 爬虫深度
        `type`: 爬虫类型, link(0), content(1),
        `crawlerId`: 模板id
        `siteId`: 站点id
        `taskId`: 任务id

    Method:
        getInfo: 获取Info
        getDepth: 获取深度
        getType: 获取类型
        setDepth: 设置爬虫种子深度
        incDepth: 种子深度 +1
        updateInfo: 更新data
    """
    LINK = "0"
    CONTENT = "1"
    LINK_AND_CONTENT = "2"

    def __init__(self, info=None, crawlerId=-1, siteId=-1, taskId=-1, depth=0, type=SeedType.link):
        self.type = type
        self.depth = depth
        self.info = {} if info is None else info

        self.crawlerId = crawlerId
        self.taskId = taskId
        self.siteId = siteId

    def getInfo(self) -> dict:
        """
        获取Info
        :return: 返回数据流
        """
        return self.info

    def getSiteId(self) -> int:
        """
        获取 站点id
        :return:
        """
        return self.siteId

    def getTaskId(self) -> int:
        """
        获取 任务id
        :return:
        """
        return self.info.get("task_id", -1)

    def getCrawlerId(self) -> int:
        """
        获取 模板id
        :return:
        """
        return self.info.get("tp_id", -1)

    def getEnterUrl(self) -> str:
        """
        获取 enter_url
        :return:
        """
        return self.info.get("enter_url", "-1")

    def getInsertData(self) -> dict:
        data = self.info.copy()
        data.update({
            MSG_FIELD.CRAWLER_ID: self.crawlerId,
            MSG_FIELD.SITE_ID: self.siteId,
            MSG_FIELD.TASK_ID: self.taskId
        })
        return data

    def incDepth(self) -> None:
        """
        种子深度 +1
        :return:
        """
        self.depth += 1

    def updateInfo(self, info: dict) -> None:
        """
        更新 info
        :param info: information
        :return: 
        """
        self.info.update(info)

    def addInfo(self, keyName: str, value: str) -> None:
        """添加info"""
        self.info[keyName] = value

    def setEnterUrl(self, enterUrl: str):
        self.info[MSG_FIELD.ENTER_URL] = enterUrl

    def toPython(self) -> dict:
        """
        返回python对象
        :return:
        """
        return {"type": self.type,
                "depth": self.depth,
                "info": self.info,
                "crawlerId": self.crawlerId,
                "taskId": self.taskId,
                "siteId": self.siteId}

    def __str__(self):
        return self.toPython().__str__()

    def __repr__(self):
        return self.toPython().__str__()


if __name__ == '__main__':
    # seed = Seed(info={"url": "http://www.baidu.com", "name": "miaomiao"}, depth=1)
    # print(seed.seedString)
    pass

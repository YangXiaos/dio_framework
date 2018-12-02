from DioFramework.Base.Message import Message
from DioFramework.Base.Processor.Components.MessageProcessor.MessageWriter import MessageMongodbWriter
from Test.Example import testJob, testMsgs


def test_MessageMongodbWriter():
    cfg = {
        "id": -1,
        "params": {
            "db_name": "test",
            "collection_name": "miao"
        }}
    writer = MessageMongodbWriter(config=cfg)
    writer.run(testJob, testMsgs)


def test_MessageMongodbWriter2():
    cfg = {
        "id": -1,
        "params": {
            "db_name": "test",
            "collection_name": "miao"
        }}
    writer = MessageMongodbWriter(config=cfg)

    testMsg1 = Message(type=Message.CONTENT)
    testMsg1.updateInfo({"_id": "dio1", "name": "dio"})

    testMsg2 = Message(type=Message.CONTENT)
    testMsg2.updateInfo({"_id": "dio2", "name": "dio的猫"})

    writer.run(testJob, [testMsg1, testMsg2])



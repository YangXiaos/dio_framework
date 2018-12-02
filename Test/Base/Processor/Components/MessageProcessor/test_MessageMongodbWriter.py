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


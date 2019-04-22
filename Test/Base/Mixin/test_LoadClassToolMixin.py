from DioFramework.Base.Mixin.LoadClassToolMixin import LoadClassToolMixin


def test_loadProcessorCls():
    processor = LoadClassToolMixin.loadProcessorCls(2)
    print(processor.__name__)

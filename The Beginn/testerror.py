class TestError(Exception):

    def __init__(self, Value):
        self.Value = Value
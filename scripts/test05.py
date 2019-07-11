import pytest
class Test01():
    def test_001(self):
        print("test001被执行")
    def test_002(self):
        print("test002被执行")
        assert False
    def test_003(self):
        print("test003被执行")
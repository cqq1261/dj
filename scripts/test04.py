import pytest


class Test01():
    @pytest.mark.run(order=1)
    def test_001(self):
        print("test001被执行")

    @pytest.mark.run(order=3)
    def test_002(self):
        print("test002被执行")

    @pytest.mark.run(order=2)
    def test_003(self):
        print("test003被执行")
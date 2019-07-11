
class Test01():
    # 函数方法级别开始
    def setup(self):
        print("setup被执行")


    # 函数方法级别结束
    def teardown(self):
        print("teardown被执行")

    # 函数类级别开始
    def setup_class(self):
        print("setup_class被执行")

    # 函数类级别结束
    def teardown_class(self):
        print("teardown_class被执行")


    # 定义测试方法
    def test_001(self):
        print("test001被执行")

    def test_002(self):
        print("test002被执行")



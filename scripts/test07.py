import pytest

# 作用：将before变成工厂函数
# 位置：在测试列外
@pytest.fixture()
def before():
    print("before被执行")
# 通过函数方式
@pytest.mark.usefixtures("before")
class Test02():
    def test01(self):
        print("test01被执行")
    # 通过函数引用工厂函数
    # @pytest.mark.usefixtures("before")
    def test02(self,before):
        print("test02被执行")
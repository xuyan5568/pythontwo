#继承于童姥类，
from lianxisan.python_Tonglao import Tonglao
class Xuzhu(Tonglao):
#定义 read方法
     def read(self):
         print("罪过罪过")
#类实例化
xuzhu=Xuzhu(100,30)
#调用类的方法
xuzhu.read()
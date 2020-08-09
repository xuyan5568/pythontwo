#coding=utf-8
import  yaml
import  pytest

from python_pytes.calc import Calculator

with open('./data_one/calc.yml')as f:
     datas = yaml.safe_load(f)['datas']
# 获取加法算式的参数
     add_one = datas["add"]["num"]
     add_two=datas["add"]["name"]
#获取除法算式的参数
     add_three=datas["div"]["num"]
     add_four=datas["div"]["name"]
class TestCacl:
      def setup_class(self):
           print("开始计算")
           self.calcu= Calculator()

      def teardown_class(self):
           print("结束计算")
#加法运算
      @pytest.mark.parametrize("a,b,exp",add_one,ids=add_two)
      def test_add(self,a,b,exp):
            #对于a，b为字母的情况
            if isinstance(a,str)or isinstance(b,str):
               raise Exception("不支持字符串的相加")
            else:
                result = self.calcu.add(a, b)
             #针对计算结果不为整数的判断处理
                if isinstance(result,float):
                   result=round(result,2)
                   assert exp == result
                else:
                   assert exp == result
      #除法运算
      @pytest.mark.parametrize("a,b,exp",add_three,ids=add_four)
      def test_add(self,a,b,exp):
           #被除数和除数为异常的处理
           if isinstance(a,str) or isinstance(b,str) or b==0:
                raise Exception("输入数据不对")
           else:
                result = self.calcu.div(a, b)
             #针对结算结果不为整数的判断处理
                if isinstance(result,float):
                   result=round(result,2)
                   assert exp == result
                else:
                    assert exp == result







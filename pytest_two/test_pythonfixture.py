#coding=utf-8
class Testcacl():
#加法运算
      def test_add(self,get_cal,get_data_add):
            #对于a，b为字母的情况
            if isinstance(get_data_add[0],str) or isinstance(get_data_add[1],str):
                raise Exception("不支持字符串的相加")
            else:
               result = get_cal.add(get_data_add[0],get_data_add[1])
             #针对计算结果不为整数的判断处理
               if isinstance(result,float):
                    result=round(result,2)
                    assert  get_data_add[2]== result
               else:
                    assert get_data_add[2] == result
      #除法运算
      def test_div(self,get_cal,get_data_div):
           #被除数和除数为异常的处理
           if isinstance(get_data_div[0],str) or isinstance(get_data_div[1],str) or get_data_div[1]==0:
                raise Exception("输入数据不对")
           else:
                result =get_cal.div(get_data_div[0], get_data_div[1])
             #针对结算结果不为整数的判断处理
                if isinstance(result,float):
                   result=round(result,2)
                   assert get_data_div[2] == result
                else:
                    assert get_data_div[2] == result
      #减法运算
      def test_sub(self,get_cal,get_data_sub):
            #对于a，b为字母的情况
            if isinstance(get_data_sub[0],str) or isinstance(get_data_sub[1],str):
                raise Exception("不支持字符串的相减")
            else:
               result = get_cal.sub(get_data_sub[0],get_data_sub[1])
             #针对计算结果不为整数的判断处理
               if isinstance(result,float):
                    result=round(result,2)
                    assert  get_data_sub[2]== result
               else:
                    assert get_data_sub[2] == result

      #乘法运算
      def check_mul(self,get_cal,get_data_mul):
            #对于a，b为字母的情况
            if isinstance(get_data_mul[0],str) or isinstance(get_data_mul[1],str):
                raise Exception("不支持字符串的相乘")
            else:
               result = get_cal.mul(get_data_mul[0],get_data_mul[1])
             #针对计算结果不为整数的判断处理
               if isinstance(result,float):
                    result=round(result,2)
                    assert  get_data_mul[2]== result
               else:
                    assert get_data_mul[2] == result



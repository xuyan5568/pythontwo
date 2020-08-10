#coding=utf-8
from pytest_two.calc import Calculator
import  yaml
import pytest

with open('./caclt.yml')as f:
    datas= yaml.safe_load(f)
    data_add = datas["add"]["num"]
    myids_add=datas["add"]["name"]
    data_div= datas["div"]["num"]
    myids_div= datas["div"]["name"]
    data_sub= datas["sub"]["num"]
    myids_sub= datas["sub"]["name"]
    data_mul= datas["mul"]["num"]
    myids_mul= datas["mul"]["name"]


@pytest.fixture(scope="class")
def get_cal():
    cacl=Calculator()
    return  cacl


#带参数传递
@pytest.fixture(params=data_add,ids=myids_add)
def get_data_add(request):
    print("开始计算")
    yield  request.param
    print("结束计算")

@pytest.fixture(params=data_div,ids=myids_div)
def get_data_div(request):
   print("开始计算")
   yield   request.param
   print("结束计算")


@pytest.fixture(params=data_sub,ids=myids_sub)
def get_data_sub(request):
     print("开始计算")
     yield   request.param
     print("结束计算")


@pytest.fixture(params=data_mul,ids=myids_mul)
def get_data_mul(request):
      print("开始计算")
      yield   request.param
      print("结束计算")

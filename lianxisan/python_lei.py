#定义dog,它能够跑，能够叫，游泳
class Dog:
    def __init__(self,height,color,weight,age,name):
     #定义属性，身高，体重，毛色，年龄
        self.height=height
        self.color=color
        self.weight=age
        self.age = age
        self.name=name
    #定义run方法
    def run(self):
         print(f"{self.name}会跑")
    # 定义cry方法
    def cry(self):
        print(f"{self.name}能够汪汪叫")
    #定义swim方法
    def swim(self):
        print(f"{self.name}会游泳")
#实例化
dog=Dog(11,'red',12,3,'lucy')
dog.run()
dog.cry()
dog.swim()
#打印空行
print("\n")



#定义desk类，它可以用来吃饭，可以用来放东西
class Desk:
        def __init__(self,shape,material,legnum):
        #属性，形状，材料,腿的数量
           self.shape=shape
           self.material=material
           self.legnum=legnum
        def eat(self):
            print("桌子能够用来吃饭和放东西 ")
#实例化
desk=Desk('road','wood',6)
#调用方法
desk.eat()
#打印空行
print("\n")

#定义Book类，他是某个作者写的，能够让人获取到知识
class Book():
    def __init__(self,page,writer,name):
    #属性，页数，作者，书名
        self.page=page
        self.writer=writer
        self.name=name
    #study方法
    def studying(self):
        print(f"我们能从{self.name}中，获取到有用知识")
    #比较两本书的厚度
    def pagenum(self,your_page):
      #若输入的页数不是整数
        if type(self.page)!= int or type(your_page)!= int:
            print("输入的不是整数，无法比较")
       #若输入的页数为整数的处理方式：
        else:
             if  self.page>your_page:
                  print("我的书厚")
             elif self.page<your_page:
                  print("你的书厚")
             else:
                  print("一样厚")

#实例化
book=Book(23,"nihao","tangshisanbaishou")
#调用study方法
book.studying()
#调用pagenum方法
book.pagenum(23)
#打印空行
print("\n")


#定义film类
class Film():
    def __init__(self,name,director,type):
     #属性，电影名字，导演，电影类型
     self.name=name
     self.director=director
     self.type=type
    def watch(self):
       print(f"由{self.director}导演的{self.type}电影{self.name},非常精彩")
#实例化
film=Film("英雄","张艺谋","武侠")
#调用watch方法
film.watch()
print("\n")

#定义天龙八部里面的段誉
class DuanYu():
    gender='male'
    height=180
    def skill(self):
        print(f"他性别{self.gender}，会凌波微步")
duanyu=DuanYu()
duanyu.skill()




 




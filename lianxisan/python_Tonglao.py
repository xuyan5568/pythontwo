class  Tonglao:
    #定义2个变量，存放血量和攻击力
     def __init__(self,hp,power):
         self.hp=hp
         self.power=power
     #定义see_people方法，根据需要输入的名字，进行相应判断
     def see_people(self,name):
         name=name
     #输入WYZ
         if  name =="WYZ":
             print("师弟！！！！！")
      #输入"李秋水"
         elif  name == "李秋水":
              print("呸，贱人")
      #输入"丁春秋"
         elif  name == "丁春秋":
              print("叛徒，我杀了你")
      #输入其他名字，提示欢迎
         else:
              print("欢迎新人")
     #定义fight_zms方法,输入他人的血量和物力值：
     def fight_zm(self,your_hp,your_power):
      #调用该方法后，自己的血量和武力值发生改变
         self.hp*=0.5
         self.power*=10
      #进行一个回合对打，双方的武力值和血量发生改变
         my_hp=self.hp-your_power
         your_hp=your_hp-self.power
      #比较血量，得出输赢值，我的血量比你的少，则你赢
         if my_hp<your_hp:
              print("我的血量是",my_hp)
              print("你的血量是",your_hp)
              print("你赢了")
      #若我的血量比你多，则我赢
         elif your_hp<my_hp:
              print("我的血量是", my_hp)
              print("你的血量是", your_hp)
              print("我赢了")
      #我两一样多，则打平
         else:
              print("打成了平分了")


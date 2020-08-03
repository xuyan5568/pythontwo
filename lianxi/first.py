def fight():
    #定义4个变量，分别代表我方和他方的血量和power
     my_hp=1000
     my_power=300
     your_hp=1000
     your_power=200
     #打斗多回合
     while True:
     #定义fight计算方式，谁的hp先为0，谁先输
         my_hp -=your_power
         your_hp-=my_power
         if my_hp <=0:
             print("我的hp是",my_hp)
             print("你的hp是",your_hp)
             print("我输了")
             break
         elif  your_hp <= 0:
             print("我的hp是", my_hp)
             print("你的hp是", your_hp)
             print("你输了")
             break
fight()

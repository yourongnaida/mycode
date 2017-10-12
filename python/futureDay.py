#计算未来多少天后是星期几
#打印数字代表星期几
print("星期一是数字1 ，星期二是数字2 ，。。。。，星期天是数字0")

Today = eval(input("Enter today is :"))
print("Do you want know day of week which is it  in the future time? input number below")
futureDay = eval(input("numer is:"))

Day = (futureDay + Today) % 7

if Day == 1:
      print("you input day of Monday")
elif Day == 2:
      print("you input day of Tuesday")
elif Day == 3:
      print("you input day of Wensday")
elif Day == 4:
      print("you input day of Thursday")
elif Day == 5:
      print("you input day of Friday")
elif Day == 6:
      print("you input day of Saturday")
else:
      print("you input  day of Sunday")
      

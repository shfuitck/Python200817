a=float(input("請輸入數學成績"))
b=float(input("請輸入應文成績"))
if (a >=0 and a <=100)and(b>=0 and b<=100):
     if a>=90 and b >=90:
         input("有獎品")
     elif a<60 or b<60:
         input("再加油")
     elif a<60 and b < 60:
         input("要處罰")          
else:
     print("ERROR")
     

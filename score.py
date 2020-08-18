score=int(input("請輸入成績"))
if score>=0 and score<=100:
    if score>=90:
       print("level A")
    elif score>80:
        print("level B")
    elif score>70:
        print("level C")
    elif score>80:
        print("level D")
    else:
        print("level E")
else:
    print("not right")
    
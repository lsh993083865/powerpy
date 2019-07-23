'''
lint = 616 #整数
lstr = "0616" #字符串
lflout = 0.616 #小数
llist = [] #列表
lbool = False #布尔值
ltuple = () #元组
ldict = {} #字典
lnone = None #空

bltype = type(lnone)
print(lnone)
print(bltype)

print("425125"+"5346534")

ltuple = (155,"456",48.485,155,"456",48.485155,"456",48.485)

print(ltuple[1])
num = ltuple.count(155)
print(num)
xxx = ltuple.index("456")
print(xxx)



llist = [1234,"heheda","黑哦哦安抚","memeda"]
llist.append("1234")
llist0 = llist.copy()
llist.extend("646iihgh")
llist.insert(2,"fsdf")
lululu = llist.pop(1)
llist.remove(1234)
llist.sort()
print(llist)
print("---------------------------------------------")

ldict = {
    "name":"张三",
    "high":"185",
    "class":"1",
}
llll = ldict.get("name")
hhhh = ldict.pop("high")
uuuu = ldict.copy()
print(uuuu)
ldict.clear
print("--------------------------------------------------------")


jine = input("请输入金额：")  # 获取输入金额，赋值给jine这个变量
print("输入的金额为：",jine)   # 打印jine

num = jine.count(".")  #  统计jine这个字符串中，有多少个小数点
if num == 0 or num == 1:  # 判断小数的个数，只有小数点数量为0或者为1个的情况，才认为是正常的数字
    hstr = "0123456789."
    for i in jine:
        if i not in hstr:  # 判断jine这个字符串中，是否存在非数字和小数点的值
            print("输入的值不合法，请输入数字！")
            exit()
    jine = float(jine)  # 强制转换数据类型为float
    if jine >= 0.01 and jine <= 200:
        print("发送红包成功！")
    else:
        print("金额超出范围！")
else:
    print("输入的金额不合法，只能输入数字！")
'''

for i in range(1,10):
    for j in range(1,10):
        print(i,"x",j,"=",i*j,end="  ")
    print()

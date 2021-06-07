#求和，平均数，最大值
a = 0
i = 0
sum = 0
while i<10:
    num = int(input("请输入数字："))
    sum = sum+num
    if a>num:
        pass
    else:
        pass
        a=num
    i = i + 1
print("和:",sum,"平均数:",sum/10,"最大值:",a)

#如何使用random产生50~150之间的数
import random
while 1:
    n = random.randint(50,151)
    print(n)
    if i:
        print("循环结束")
    break

#判断三角形
while 1:
  a=int(input("请输入边a:"))
  b=int(input("请输入边b:"))
  c=int(input("请输入边c:"))
  if a+b<c or b+c<a or a+c<b:
     print("请输入正常三角形")
     continue
  elif a==b==c:
     print("等边三角形")
  elif a==b!=c or a==c!=b or b==c!=a:
     print("等腰三角形")
  elif a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
     print("直角三角形")
  else:
     print("普通三角形")

#调换
A= int(input("请输入A:"))
B= int(input("请输入B:"))
if A>B:
    n = A - B
    A = A - n
    B = B + n
else:
    m = B - A
    B = B - m
    A = A + m
print("A=",A)
print("B=",B)

#错误锁定功能
i=0
name = "root"
password = "admin"
while 1:
    n = input("请输入用户名:")
    p = input("请输入用户密码:")
    if name==n and password==p:
        print("登陆成功")
        break
    elif name!=n or password!=p:
        print("登陆失败")
        i= i+1
    if i==3:
        print("登陆失败3次，系统锁定")
        break

#1~100的和
#for...in...
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)
#while
i = 1
sum = 0
while i<101:
    if i>0:
        sum = sum + i
        i = i + 1
print(sum)

#青蛙几天能爬出来
high = 20
a= 3
b= 2
i= 1
n= 0
while 1:
    if n+a<high:
        n= n+a-b
        i = i+1
    elif n+a==high:
        print("一共需要:",i,"天")
        break

#列表
#(1)
lst = ["北京","上海","广东"]
lst.append("济南")
lst.append("石家庄")
lst.append("长春")
lst.append("哈尔滨")
lst.append("沈阳")
print(lst)
#(2)
lst[1]=("广东")
lst[2]=("上海")
print(lst)
#(3)
sum = 0
lst1=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
for i in lst1:
    sum = i + sum
print("GDP总和:",sum)
a = sum/8
print("平均值:",a)

#5的倍数的和
sum=0
a = [1,5,21,30,15,9,30,24]
for i in a:
    if i%5==0:
        sum = sum + i
print("和为:",sum)







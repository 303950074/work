import random
m = random.randint(1,1000)
b = 0
a = 5000
while 1:
     n = input('请输入1-1000之间的一个整数：')
     if str.isdigit(n):
         n = int(n)
     else:
         print('请输入整数')
         continue
     if n<m:
        print("猜小了扣除500金币,您现在拥有金币："+str(a-500))
        a = a - 500
        b+=1
     elif n>m:
        print("猜大了扣除500金币,您现在拥有金币："+str(a-500))
        a = a - 500
        b+=1
     else:
        print("猜对了,奖励3000金币,您现在拥有金币："+str(a+3000))
        m = random.randint(1, 1000)
        a = a+3000
        b=0
     if a==0:
         print("您的余额为0，请您及时充值")
         break
     if b==15:
         print("失败了15次，恭喜您获得了散豆童子称号")
         break






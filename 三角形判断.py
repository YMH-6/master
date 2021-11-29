a=int(input("请输入第一个正整数:"))
b=int(input("请输入第二个正整数:"))
c=int(input("请输入第三个正整数:"))
if(a+b>c and a+c>b and c+b>a):
    print("可以组成三角形")
    if(a==b and a!=c) or (a==c and a!=b) or (c==b and a!=c):
        print("并且是等腰三角形!")
    elif(a==b==c):
        print("并且是等边三角形!")
    elif(a*a+b*b==c*c or b*b+c*c==a*a):
        print("并且是直角三角形!")
    else:
        print("普通的三角形")
else:
    print("不可以形成三角形")
#青蛙
#tian=0
# qi=0
# while True:
#     qi=qi+3
#     tian =tian+1
#     if qi==20 or qi>20:
#         print("第",tian,"天青蛙爬了",qi,"米")
#         break
#     else:
#         qi = qi - 2


#list=[1,2,3,4,5,6,7,8,9]
#print(list[::-1])


#foom collections import Counter
#list = [1,4,7,5,8,2,1,3,4,5,6,8,10]
#a = Counter(list )
#print(a)

# GDP=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# #     0          1       2        3         4        5        6        7
# he=0
# for i in range(1,9):
#     he=he+GDP[0]
# print('前八城市GDP和为%.2f'%he)
# print('平均GDP为：%.2f'%(he/i))


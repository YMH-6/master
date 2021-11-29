# import random
# ju=0
# while True:
#     x = input('请按1开始抽取优惠卷')
#     if x == '1':
#         a = random.randint(1, 31)
#         if a < 11:
#             ju = 0.3
#             break
#         elif a > 10 and a < 31:
#             ju = 0.9
#             break
#         else:
#             ju = 0
#             break
#
#     else:
#         print('请输入正确数字')
# if ju==0.3:
#     print('您获得签字笔3折卷')
# elif ju==0.9:
#     print('您获得格尺9折卷')
# else:
#     print('您获得免单卷')
# shopping=[
#     ["铅笔",5],
#     ["文具盒",30],
#     ["水彩笔",5],
#     ["涂改带",8],
#     ["卷笔刀",10],
#     ["签字笔",50],
#     ["格尺",12],
# ]
# mycar=[]
# money=1000
# while True:
#     for i in enumerate(shopping):
#         print(i)
#     shop=input("请输入商品：")
#     if shop.isdigit():
#         shop=int(shop)
#         if shop<len(shopping):
#             if money>shopping[shop][1]:
#                 mycar.append(shopping[shop])
#                 if ju==0.3 and shop==5:
#                     money=money-shopping[shop][1]*ju*0.8
#                 elif ju==0.9 and shop==6:
#                     money=money-shopping[shop][1]*ju*0.8
#                 elif ju==0:
#                     money=money
#                 else:
#                     money-=shopping[shop][1]*0.8
#                 print("此商品已经加入购物车，您的余额为：",money)
#             else:
#                 print("余额不足")
#         else:
#             print("请输入正确的商品编号")
#     elif shop=='q' or shop=='Q':
#         print("再见，您的商品小票为：")
#         # for i in enumerate(mycar):
#         print(mycar)
#         break
#    else:print("您输入的有误")

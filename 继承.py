# import time
# class oldphone:
#     __brand: ""
#     def setbrand(self,brand):
#         if brand == "":
#             print("不可为空")
#         else:
#             self.__brand = brand
#     def get(self):
#         return self.__brand
#
#
#
#     def set(self,call):
#         print("正在给",call,"打电话")
#
#         print(self,)
#
# o = oldphone()
# o.setbrand("诺基亚")
# o.call(18004740284)


import time
class person:
    name = ""
    sex = ""
    age = 0



class worker(person):
    def works(self,working):
        for i in range(4):
            print(".",end="")
            time.sleep(1)
        print(self.name,"性别",self.sex,"年龄",self.age,"岁,职业：工人，正在",working,"!!!")

class student(person):
    def studys(self,study,sing):
        for i in range(4):
            print(".",end="")
            time.sleep(1)
        print(self.name,"性别",self.sex,"年龄",self.age,"岁,是一名大学生，正在边",study,"边",sing,"!!!")


work = worker()
work.name = "常远"
work.sex = "男"
work.age = 27

work.works("进行赛车比赛")

study = student()
study.name = "小明同学"
study.sex = "男"
study.age = 17
study.studys("学习弹吉他","唱情歌")

"""
class Chek:
    __name = ""
    __age = 0


    def Steam(self):
        pass

    def __set_name(self,name):
        self.__name = name
    def __get_name(self):
        return self.__name

    def __set_age(self, age):
        self.__age = age
    def __get_age(self):
        return self.__age


class Cheks(Chek):
    def fried(self):
        pass

class Chekss(Cheks):
    def Steam(self):
        print()
        print("正在烤红薯")

    def fried(self):
        print()
        print("正在炒菜")

    def set_age(self, param):
        pass

    def set_name(self, param):
        pass

    def get_name(self):
        pass

    def get_age(self):
        pass


if __name__ == '__main__':

    t = Chekss()
    t.set_name('张三')
    t.set_age(20)

    print('厨师叫%s，已经%s岁大了' % (t.get_name(), t.get_age()))

    t.Steam()
    t.fried()
    
import time

class Old_Phone:
    __brand = ''

    def set_brand(self,brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def call(self, name):
        return '正在给%s打电话' % name

class New_Brand(Old_Phone):
    def call(self, name):
        print('语音拨号中')
        for i in range(3):
            print('.', end='')
            time.sleep(1)
        print(super(New_Brand, self).call(name))

    def phone_brand(self):
        print('%s手机' % self.get_brand())

if __name__ == '__main__':
    new = New_Brand()

    new.set_brand('ipone ')
    new.phone_brand()
    new.call('刘明')







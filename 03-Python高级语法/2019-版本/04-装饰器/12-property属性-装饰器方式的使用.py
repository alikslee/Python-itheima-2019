class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 0

    @property # 当对象调用age属性的时候会执行下面的方法
    def age(self):
        print("获取属性啦")
        return self.__age

    @age.setter # 当对象调用age属性设置值的时候会调用下面的方法
    def age(self, new_age):
        print("设置属性啦")
        if new_age >= 0 and new_age <= 130:
            self.__age = new_age
        else:
            print("成精啦")


# 提示: 使用装饰器方式的property属性那么方法名要保持一致

student = Student()
age = student.age
print(age)

student.age = 20

age = student.age
print(age)

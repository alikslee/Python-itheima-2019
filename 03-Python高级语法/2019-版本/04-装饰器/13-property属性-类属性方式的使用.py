class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 0

    def get_age(self):
        print("获取属性啦")
        return self.__age

    def set_age(self, new_age):
        print("设置属性啦")
        if new_age >= 0 and new_age <= 130:
            self.__age = new_age
        else:
            print("成精啦")

    # 1. get_age 表示获取age属性的时候执行的方法
    # 2. set_age 表示设置age属性的时候执行的方法
    age = property(get_age, set_age)


student = Student()
age = student.age
print(age)

student.age = 20

age = student.age
print(age)

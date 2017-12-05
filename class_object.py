#/usr/bin/python3

class Car() :
    def __init__(self) :
        print("This is class named car")

car = Car()


class ChinaCar(Car) :
    def __init__(self, name) :
        self.__name__ = name
        print("China car named ", name)


china_car = ChinaCar("byd")

class FlyCar(Car) :
    def __init__(self) :
        super().__init__()

    @property
    def color(self) :
        print("color is ", self.__color__)
        return self.__color__

    @color.setter
    def color(self, color) :
        self.__color__= color


fly_car = FlyCar()
fly_car.color = "red"
print(fly_car.color)


class A() :
    count = 0
    def __init__(self) :
      A.count += 1

    @classmethod
    def kids(cls) :
        print("There are total %s A object" % A.count)


a = A()
b = A()
A.kids()



class B() :
    def __init__(self) :
        pass

    @staticmethod
    def staticTest() :
        print("This is test for static method")


B.staticTest()

#Тренировка классов
#Считаем периметр и площадь

class Rectangle:
    def __init__(self, value_one, value_two):
        self.__side1 = value_one
        self.__side2 = value_two
        self.__perimeter = None
        self.__area = None

    @property
    def sides(self):
        return self.__side1, self.__side2

    @sides.setter
    def sides(self, values):
        self.__side1 = values[0]
        self.__side2 = values[1]
        self.__perimeter = None
        self.__area = None

    @property
    def perimeter(self):
        if self.__perimeter is None:
            print('calcilate perimeter')
            self.__perimeter = 2 * (self.__side1 + self.__side2)
        return self.__perimeter

    @property
    def area(self):
        if self.__area is None:
            print('calculate area')
            self.__area = self.__side2 * self.__side1
        return self.__area

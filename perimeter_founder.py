#Тренировка классов
#Считаем периметр

class Perimeter:
    def __init__(self, value_one, value_two):
        self.__side1 = value_one
        self.__side2 = value_two
        self.__perimeter = None

    @property
    def sides(self):
        return self.__side1
        return self.__side2

    @sides.setter
    def sides(self, value1, side2):
        self.__side1 = value1
        self.__side2 = value2
        self.__perimeter = None

    @property
    def perimeter(self):
        if self.__perimeter is None:
            print ('calcilate perimeter')
            self.__perimeter = 2 * (self.__side1 + self.__side2)
        return self.__perimeter


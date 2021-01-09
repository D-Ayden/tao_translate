class Present:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    @property
    def name(self):
        print("In a getter.")
        return self.__name

    @name.setter
    def name(self, value):
        print("In a setter.")
        self.__name = value

    @name.deleter
    def name(self):
        pass

    def set_age(self):
        self.__age = 16


class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_name(self):
        print("In a getter.")
        return self.__name

    def set_name(self, value):
        print("In a setter.")
        self.__name = value

    def del_name(self):
        del self.__name

    p = property(get_name, set_name, del_name, "John")

from abc import abstractmethod


class Foo:
    @abstractmethod
    def fun(self, n):
        pass


class Bar(Foo):
    pass


b = Bar()
b.fun(5)
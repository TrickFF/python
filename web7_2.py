from abc import ABC, abstractmethod

class MyOwnAbc(ABC):
    @abstractmethod
    def m_1(self):
        pass

    @abstractmethod
    def m_2(self):
        pass

class MyClass(MyOwnAbc):
    def m_1(self):
        pass

    def m_2(self):
        pass

    def m_3(self):
        pass


my_obj = MyClass()
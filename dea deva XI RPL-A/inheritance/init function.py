class Person:
    def __init__(self,name):
        self.name = name

        def say_hi(self):
            print("hello,my name is ",self.name)

person1 = Person("Fahmi")
person1.say_hi()
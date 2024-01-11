# class Person:
#     _age = 15
#     def __say_hello():
#         print('Privet')
# person1 = Person

# person1 = Person
# print(person1._Person__age)
# # person1.say_hello()
# person1._Person__say_hello()

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    
object = Person('Qwerty')
print(object.name)
object.name = "Sergey"
print(object.name)

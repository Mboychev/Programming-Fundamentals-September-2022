class Person:
    # инициализаторa __init__, работи със self, което всъщност трансферира данните към него
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    #say_hi e метода (функцията), която обработва обекта obj (обетка човек, които подаваме от конзолата като параметри)
    def say_hi(self):

        return f"Hello {self.first_name} {self.last_name} on {self.age}"

# към нашия obj (обект) закачаме класа Person
obj = Person('Ivan', 'Ivanov', 25)
#с оператора . достъпваме метода ли параметрите в инициализатора
print(obj.age)
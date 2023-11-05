class Person:
    number_of_ppl = 0

    def __init__(self, name) -> None:
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_ppl_(cls):
        return cls.number_of_ppl
    
    @classmethod
    def add_person(cls):
        cls.number_of_ppl += 1

p1 = Person("tim")
print(Person.number_of_ppl_())
p2 = Person("jill")
print(Person.number_of_ppl_())


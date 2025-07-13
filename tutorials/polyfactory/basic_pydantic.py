from pydantic import BaseModel
from polyfactory.factories.pydantic_factory import ModelFactory
from faker import Faker

class Person(BaseModel):
    name: str
    age: float
    height: float
    weight: float
    address: str
    date: str

class PersonFactory(ModelFactory[Person]):
    __model__ = Person
    __random_seed__ = 1
    __faker__ = Faker(locale="en_NZ")

    @classmethod
    def name(cls) -> str:
        return cls.__faker__.name()
    
    @classmethod
    def address(cls) -> str:
        return cls.__faker__.address()
    
    @classmethod
    def date(cls) -> str:
        return cls.__faker__.date()
    
def test_is_person() -> None:
    person_instance = PersonFactory.build()
    assert isinstance(person_instance, Person)
    assert isinstance(person_instance.name, str)
    assert isinstance(person_instance.age, float)
    assert isinstance(person_instance.height, float)
    assert isinstance(person_instance.weight, float)


person_instance = PersonFactory.build()
print(person_instance)
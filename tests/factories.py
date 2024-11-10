from factory import Factory, Faker, Sequence, LazyAttribute
import random

class ProductFactory(Factory):
    """Factory for creating fake Product objects."""
    
    class Meta:
        model = dict 

    id = Sequence(lambda n: n + 1)
    name = Faker("word")
    description = Faker("sentence", nb_words=10)
    price = LazyAttribute(lambda _: round(random.uniform(10.0, 100.0), 2))
    category = Faker("word")
    stock_quantity = LazyAttribute(lambda _: random.randint(0, 50))

from base_generator import BaseGenerator
import random

class AnimalGenerator(BaseGenerator):
    def __init__(self) -> None:
        super().__init__()
        self.names = ["wolve", "lion", "antelope", "beaver", "capybara",
                      "elephant", "squirrel", "horse", "goat", "cheetah", "zebra",
                      "fox", "goose", "hawk", "crab", "sealion",
                      "hedgehog", "mole", "duck", "baboon", "peacock",
                      "flamingo", "lynx", "owl", "wombat", "sheep", "bison",
                      "buffalo", "bull", "kangaroo", "bear", "camel", "rabbit",
                      "donkey", "deer", "tiger", "pig", "giraffe", "turtle"]

        self.weight_max = 2000
        self.weight_min = 0.01

        self.height_min = 10
        self.height_max = 320

        self.age_min = 1
        self.age_max = 100

    def fill_db(self, db_connection, amount_of_records):
        cursor = db_connection.cursor()
        insert_query = """INSERT INTO animals (id, aviary_id, name, weight, height, endangered, age)"""

        for i in range(amount_of_records):
            weight = random.uniform(self.weight_min, self.weight_max)
            height = weight / 0.45
            record_to_insert = (random.randint(0, amount_of_records - 1),
                                random.randint(0, amount_of_records - 1),
                                self.names[random.randint(0, len(self.names) - 1)],
                                weight,
                                height,
                                bool(random.random()),
                                random.randint(self.age_min, self.age_max))

            cursor.execute(insert_query, record_to_insert)
        return

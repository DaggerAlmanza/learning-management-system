import pytest
from app.helpers import GeneralHelpers


class Animales:
    def __init__(self, animal_1, animal_2, animal_3):
        self.animal_1 = animal_1
        self.animal_2 = animal_2
        self.animal_3 = animal_3


animales = Animales("Perro", "Gato", "Delfin")


helpers = GeneralHelpers()
keys: list = ["animal_2"]
data: dict = {
    "animal_1": "Delfin",
    "animal_2": "Avestruz",
    "animal_3": "Perro",
}


@pytest.mark.django_db
def test_get_all():
    helpers.update_object_attrs(animales, keys, data)
    assert animales.animal_1 == "Perro"
    assert animales.animal_2 == "Avestruz"
    assert animales.animal_3 == "Delfin"

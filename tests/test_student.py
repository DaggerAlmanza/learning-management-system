import pytest
from app.repositories.student_repository import StudentRepository


repository = StudentRepository()
data = {
    "address": "Calle 45 # 8373-99",
    "identification": 232323232,
    "cell_phone": 12222222,
    "guardians_name": "string",
    "guardians_phone": 111111111
}


@pytest.mark.django_db
def test_get_all():
    result = repository.get_all()
    assert isinstance(result, list)


@pytest.mark.django_db
def test_save_student():
    result = repository.save_student(data)
    assert isinstance(result, dict) or isinstance(result, str)


@pytest.mark.django_db
def test_get_by_id():
    result = repository.get_by_id(1)
    assert isinstance(result, dict)


@pytest.mark.django_db
def test_update_student():
    result = repository.update_student(data, 1)
    assert isinstance(result, bool)


@pytest.mark.django_db
def test_delete_one():
    result = repository.delete_one(1)
    assert isinstance(result, bool)

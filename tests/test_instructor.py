import pytest
from app.repositories.instructor_repository import InstructorRepository


repository = InstructorRepository()
data = {
    "address": "calle 5 numero 98-0289",
    "identification": 11111111,
    "cell_phone": 11111111111
}


@pytest.mark.django_db
def test_get_all():
    result = repository.get_all()
    assert isinstance(result, list)


@pytest.mark.django_db
def test_get_all_courses():
    result = repository.get_all_courses(1)
    assert isinstance(result, list)


@pytest.mark.django_db
def test_save_instructor():
    result = repository.save_instructor(data)
    assert isinstance(result, dict)


@pytest.mark.django_db
def test_get_by_id():
    result = repository.get_by_id(1)
    assert isinstance(result, dict)


@pytest.mark.django_db
def test_update_instructor():
    result = repository.update_instructor(data, 1)
    assert isinstance(result, bool)


@pytest.mark.django_db
def test_delete_one():
    result = repository.delete_one(1)
    assert isinstance(result, bool)

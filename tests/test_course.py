import pytest
from app.repositories.course_repository import CourseRepository


repository = CourseRepository()
data = {
    "name": "Programación Básica",
    "description": "Programa desde cero, domina Javascript, entiende HTML y aprende de algoritmos."
}


@pytest.mark.django_db
def test_get_all():
    result = repository.get_all()
    assert isinstance(result, list)


@pytest.mark.django_db
def test_save_course():
    result = repository.save_course(data)
    assert isinstance(result, dict)


@pytest.mark.django_db
def test_get_by_id():
    result = repository.get_by_id(1)
    assert isinstance(result, dict)


@pytest.mark.django_db
def test_update_course():
    result = repository.update_course(data, 1)
    assert isinstance(result, bool)


@pytest.mark.django_db
def test_delete_one():
    result = repository.delete_one(1)
    assert isinstance(result, bool)

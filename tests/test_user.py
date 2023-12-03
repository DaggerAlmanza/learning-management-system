import pytest
from app.repositories.user_repository import UserRepository


repository = UserRepository()
data = {
    "username": "rafa",
    "password": "123.",
    "email": "rafa@example.com",
    "name": "rafa",
    "last_name": "villa",
    "is_instructor": True
}


@pytest.mark.django_db
def test_get_all():
    result = repository.get_all()
    assert isinstance(result, list)


@pytest.mark.django_db
def test_save_user():
    global id
    result = repository.save_user(data)
    id = result["id"]
    assert isinstance(result, dict)


@pytest.mark.django_db
def test_get_by_id():
    result = repository.get_by_id(1)
    assert isinstance(result, dict)


@pytest.mark.django_db
def test_update_user():
    result = repository.update_user(data, 1)
    assert isinstance(result, dict)


@pytest.mark.django_db
def test_delete_one():
    result = repository.delete_one(1)
    assert isinstance(result, bool)

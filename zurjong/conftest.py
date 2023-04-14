import pytest

from zurjong.users.models import Student, Teacher, User
from zurjong.users.tests.factories import StudentFactory, TeacherFactory, UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()

@pytest.fixture
def teacher() -> Teacher:
    return TeacherFactory()

@pytest.fixture
def student() -> Student:
    return StudentFactory()

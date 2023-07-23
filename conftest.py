# Libraries
import pytest
from mixer.backend.django import mixer

from persons.models import Person
from django.contrib.auth.models import User
from django.core.management import call_command
from rest_framework.test import APIClient

@pytest.fixture
def api_client() -> APIClient:
    """
    API Client to consume services
    """
    client = APIClient()
    return client

@pytest.fixture
def create_person(db) -> Person:
    """
    Person fixture
    """
    user = mixer.blend(
        User,
        username=mixer.faker.pystr(),
        email=mixer.faker.email()
    )
    person = mixer.blend(
        Person,
        user=user,
        first_name=mixer.faker.first_name(),
        last_name=mixer.faker.last_name(),
        email=user.email,
        address=mixer.faker.address(),
        city=mixer.faker.city(),
        country=mixer.faker.country()
    )

    return person

@pytest.fixture
def load_task_status(db):
    """
    Load task status from fixtures to task_status table
    """
    call_command('loaddata', 'fixtures/task_status.json')

    
    
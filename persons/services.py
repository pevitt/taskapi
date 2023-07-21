from django.contrib.auth.models import User
from persons.models import Person
from persons import selectors as person_selector
from utils.exceptions import TaskManagerException, ErrorCode


def create_person(
        *,
        first_name: str,
        last_name: str,
        email: str,
        address: str,
        city: str,
        country: str,
)-> Person:
    
    person = person_selector.filter_person_by_email(
        email=email
    )
    if person:
        raise TaskManagerException(ErrorCode.B01)

    user = User.objects.create_user(
        username=email,
        email=email
    )
    person = Person.objects.create(
        user=user,
        first_name=first_name,
        last_name=last_name,
        email=email,
        address=address,
        city=city,
        country=country
    )
    return person

def get_person(
        *,
        email: str,
)-> Person:
    
    person = person_selector.filter_person_by_email(
        email=email
    )
    if not person:
        raise TaskManagerException(ErrorCode.B02)
    
    return person.first()
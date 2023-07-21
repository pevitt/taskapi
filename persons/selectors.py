from persons.models import Person
import uuid

def filter_person_by_email(
        *,
        email: str
)-> 'QuerySet[Person]':
    persons = Person.objects.filter(
        email=email
    )
    return persons

def filter_person_by_id(
        *,
        id: uuid
)-> 'QuerySet[Person]':
    persons = Person.objects.filter(
        pk=id
    )
    return persons



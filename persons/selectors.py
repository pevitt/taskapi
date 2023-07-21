from persons.models import Person

def filter_person_by_email(
        *,
        email: str
)-> 'QuerySet[Person]':
    persons = Person.objects.filter(
        email=email
    )
    return persons

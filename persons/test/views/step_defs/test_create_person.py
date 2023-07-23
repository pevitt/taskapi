# Libraries
from pytest_bdd import given, parsers, scenarios, then
from mixer.backend.django import mixer

escenarios = scenarios('../features/create_person.feature')
ENDPOINT = '/api/persons/'

@given(
    parsers.parse(
        'I call service to create person with email {email}'
    ),
    target_fixture='api_request'
)
def invoke_person_create_service(
        db,
        api_client,
        email: str
):
    """
    Invoke person create service
    """
    #import pdb; pdb.set_trace()
    return api_client.post(
        ENDPOINT,
        data={
            'email': email,
            'first_name': mixer.faker.first_name(),
            'last_name': mixer.faker.last_name(),
            'address': mixer.faker.address(),
            'city': mixer.faker.city(),
            'country': mixer.faker.country()
        },
        format='json'
    )

@given(
    parsers.parse(
        'I receive a response with status code {status_code:d}'
    )
)
def validate_person_create_response(
        api_request,
        status_code: int
):
    """
    Validate person create response
    """

    assert api_request.status_code == status_code

@then(
    parsers.parse(
        'I call service to get person with email {email}'
    ),
    target_fixture='api_get_request'
)
def invoke_person_get_service(
        db,
        api_client,
        email: str
):
    """
    Invoke person get service
    """

    return api_client.get(
        f'{ENDPOINT}?email={email}',
        format='json'
    )

@then(
    parsers.parse(
        'I receive a response with status code {status_code:d} and email {email}'
    )
)
def validate_person_get_response(
        api_get_request,
        status_code: int,
        email: str
):
    """
    Validate person get response
    """
    assert api_get_request.status_code == status_code
    assert api_get_request.json()['email'] == email


@then(
    parsers.parse(
        'I call service to create another person with same email {email}'
    ),
    target_fixture='api_request'
)
def invoke_another_person_create_service(
        db,
        api_client,
        email: str
):
    """
    Invoke person create service
    """
    #import pdb; pdb.set_trace()
    return api_client.post(
        ENDPOINT,
        data={
            'email': email,
            'first_name': mixer.faker.first_name(),
            'last_name': mixer.faker.last_name(),
            'address': mixer.faker.address(),
            'city': mixer.faker.city(),
            'country': mixer.faker.country()
        },
        format='json'
    )

@then(
    parsers.parse(
        'I receive a response with status code {status_code:d}'
    )
)
def validate_person_create_response(
        api_request,
        status_code: int
):
    """
    Validate person create response
    """
    #import pdb; pdb.set_trace()
    assert api_request.data.get('detail') == 'The email already exists'
    assert api_request.status_code == status_code


@given(
    parsers.parse(
        'I receive a response with status code {status_code:d} for wrong email'
    )
)
def validate_person_create_response(
        api_request,
        status_code: int
):
    """
    Validate person create response
    """
    #import pdb; pdb.set_trace()
    assert api_request.data.get('email')[0] == 'Enter a valid email address.'
    assert api_request.status_code == status_code
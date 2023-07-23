# Libraries
from pytest_bdd import given, parsers, scenarios, then
from mixer.backend.django import mixer

escenarios = scenarios('../features/create_task.feature')
ENDPOINT = '/api/tasks/'

@given(
    parsers.parse(
        'I call service to create task with title {title}'
    ),
    target_fixture='api_request'
)
def invoke_task_create_task(
        db,
        load_task_status,
        create_person,
        api_client,
        title: str
):
    """
    Invoke task create service
    """
    person = create_person
    return api_client.post(
        ENDPOINT,
        data={
            'person_id': person.id,
            'title': title,
            'description': mixer.faker.text()
        },
        format='json'
    )

@given(
    parsers.parse(
        'I receive a response with status code {status_code:d}'
    )
)
def validate_task_create_response(
        api_request,
        status_code: int
):
    """
    Validate task create response
    """

    assert api_request.status_code == status_code
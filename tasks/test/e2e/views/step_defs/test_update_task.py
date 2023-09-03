# Libraries
from pytest_bdd import given, parsers, scenarios, then
import uuid

scenarios('../features/update_task.feature')
ENDPOINT = '/api/tasks/'

@given(
    parsers.parse(
        'I call update status service to update task status to {status_id:d}'
    ),
    target_fixture='api_request'
)
def invoke_task_update_status_service(
        db,
        load_task_status,
        create_task_person,
        api_client,
        status_id: int
):
    """
    Invoke task update status service
    """
    task = create_task_person
    return api_client.put(
        f'{ENDPOINT}',
        data={
            'task_id': task.id,
            'status_id': status_id
        },
        format='json'
    )


@given(
    parsers.parse(
        'I call update status service to update task {task_id} to task status to {status_id:d}'
    ),
    target_fixture='api_request'
)
def invoke_task_update_status_service(
        db,
        load_task_status,
        api_client,
        task_id: uuid,
        status_id: int
):
    """
    Invoke task update status service
    """
    return api_client.put(
        f'{ENDPOINT}',
        data={
            'task_id': task_id,
            'status_id': status_id
        },
        format='json'
    )


@then(
    parsers.parse(
        'The task services status should be {status_code:d}'
    )
)
def validate_task_update_status_response(
        api_request,
        status_code: int
):
    """
    Validate task update status response
    """
    assert api_request.status_code == status_code


@then(
    parsers.parse(
        'The task should be updated to status name {status_name}'
    )
)
def validate_task_update_status(
        api_request,
        status_name: str
):
    """
    Validate task update status
    """
    assert api_request.data.get('status_name') == status_name

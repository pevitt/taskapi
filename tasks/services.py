import uuid
from tasks import selectors as task_status_selector
from tasks.models import Task
from persons import selectors as person_selector
from typing import Any, Dict, List, Optional, Union

from utils.exceptions import TaskManagerException, ErrorCode

def get_task_status_list()-> Dict[str, Any]:

    task_status_qry = task_status_selector.get_task_status_list()

    task_data = task_status_qry.values(
        "id",
        "name",
        "description"
    )

    return list(task_data)

def create_task(
    person_id: uuid,
    title: str,
    description: str,
)-> Dict[str, Any]:

    person_qry = person_selector.filter_person_by_id(
        id=person_id
    )
    if not person_qry.exists():
        raise TaskManagerException(ErrorCode.B03)

    task_status = task_status_selector.get_task_status_by_status(
        status_name='pending'
    )
    if not task_status:
        raise TaskManagerException(ErrorCode.E01)
    
    person = person_qry.first()
    order = task_status_selector.get_order_by_person(
        person=person
    ).count()


    task = Task.objects.create(
        person=person,
        title=title,
        description=description,
        status=task_status.first(),
        order=order
    )

    task_data = dict(
        id=task.id,
        person_id=person.id,
        title=task.title,
        description=task.description,
        status=task.status.name,
        order=task.order
    )

    return task_data

def get_task_list(
        person_id: uuid,
        status: Optional[str]=None
)->List[Dict[str, Any]]:
    person_qry = person_selector.filter_person_by_id(
        id=person_id
    )
    if not person_qry.exists():
        raise TaskManagerException(ErrorCode.B03)

    person = person_qry.first()
    
    task_list = task_status_selector.get_task_list_by_person(
        person=person,
        status=status
    )

    return list(task_list)

def update_task_status(
        task_id: uuid,
        status_id: int
)-> Dict[str, Any]:
    task_qry = Task.objects.filter(
        id=task_id
    )
    if not task_qry.exists():
        raise TaskManagerException(ErrorCode.B04)
    
    task_status_qry = task_status_selector.get_task_status_by_id(
        status_id=status_id
    )

    if not task_status_qry.exists():
        raise TaskManagerException(ErrorCode.E01)
    
    
    task = task_qry.first()
    
    task.status = task_status_qry.first()
    task.save()

    task_data = dict(
        id=task.id,
        person_name=task.person.first_name,
        person_email=task.person.email,
        title=task.title,
        description=task.description,
        status_name=task.status.name,
        order=task.order
    )

    return task_data

def get_task_person_indicator(
        person_id: uuid
)-> Dict:
    person_qry = person_selector.filter_person_by_id(
        id=person_id
    )
    if not person_qry.exists():
        raise TaskManagerException(ErrorCode.B03)
    
    person = person_qry.first()

    task_indicator = task_status_selector.get_tasks_indicator_by_person(
        person=person
    )

    return task_indicator
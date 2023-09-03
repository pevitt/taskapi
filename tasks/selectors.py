from tasks.models import TaskStatus, Task
from persons.models import Person
from typing import Any, Dict, List, Optional, Union
from django.db.models import F, Subquery, OuterRef, Count, Prefetch
from django.contrib.postgres.aggregates import ArrayAgg, JSONBAgg




def get_task_status_by_id(
        status_id: int
)-> 'QuerySet[TaskStatus]':
    task_status = TaskStatus.objects.filter(id=status_id)
    return task_status

def get_task_status_list()-> 'QuerySet[TaskStatus]':
    task_status = TaskStatus.objects.all()
    return task_status

def get_task_status_by_status(
        status_name: str
)-> 'QuerySet[TaskStatus]':
    task_status = TaskStatus.objects.filter(name=status_name)
    return task_status

def get_order_by_person(
        person: Person
)-> 'QuerySet[Task]':
    tasks = Task.objects.filter(
        person=person
    )
    return tasks

def get_task_list_by_person(
        *,
        person: Person,
        status: Optional[str]=None
)-> List[Dict[str, Any]]:
    tasks = Task.objects.filter(
        person=person
    )
    if status:
        tasks = tasks.filter(
            status__name=status
        )

    tasks = tasks.order_by(
        'order'
    )

    tasks = tasks.annotate(
        person_name=F('person__first_name'),
        person_email=F('person__email'),
        status_name=F('status__name'),
    ).values(
        "id",
        "person_name",
        "person_email",
        "title",
        "description",
        "status_name",
        "order"
    )

    return list(tasks)

def get_tasks_indicator_by_person(
        person: Person
)-> Dict[str, Any]:

    tasks = Task.objects.filter(
        person=person
    ).values(
        name=F('status__name')
    ).annotate(
        count=Count('id')
    )

    task_count_dict = {task.get('name'): task.get('count') for task in tasks}

    return task_count_dict

'''
Crear un selector que traiga la info de la persona con sus tasks usando el related_name
'''
def get_person_with_tasks(
        *,
        person_id: int
)-> Dict[str, Any]:
    person = Person.objects.filter(
        pk=person_id
    ).prefetch_related(
        Prefetch('tasks', queryset=Task.objects.all())
    )
    # import pdb; pdb.set_trace()
    return person.first()
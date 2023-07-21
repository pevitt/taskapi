from django.urls import path
from persons.views import PersonView

urlpatterns = [
    path(
        '', 
        PersonView.as_view(),
        name='person-view'
    ),
]
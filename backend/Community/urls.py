from django.urls import path
from .views import GroupListCreateView, EventListCreateView

urlpatterns = [
    path('groups/', GroupListCreateView.as_view(), name='group-list-create'),
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
]

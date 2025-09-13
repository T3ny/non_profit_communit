from django.urls import path
from .views import Register,Login_view


urlpatterns = [
    path('signup/' , Register.as_view(),  name='signup'),
    path('Login/' , Login_view.as_view(),  name='login')
]

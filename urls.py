# urls.py

from django.urls import path
from .views import course_list, course_add, course_delete, course_add_student

urlpatterns = [
    path('list/', course_list, name='course_list'),
    path('add/', course_add, name='course_add'),
    path('add_student/<str:course_id>/', course_add_student, name='course_add_student'),
]

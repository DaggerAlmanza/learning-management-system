from app.views.user_view import (
    CurrentUser,
    UserPkView,
    UserView,
)
from django.urls import path
from rest_framework import routers
from app.views.instructor_view import (
    InstructorPkView,
    InstructorView,
)
from app.views.course_view import (
    CoursePkView,
    CourseView,
)
from app.views.student_view import (
    StudentPkView,
    StudentView,
)


router = routers.DefaultRouter()


urlpatterns = [
    path(
        'api/user/',
        UserView.as_view(),
        name='user'
    ),
    path(
        'api/user/<int:pk>',
        UserPkView.as_view(),
        name='user_pk'
    ),

    path(
        'api/current_user',
        CurrentUser.as_view(),
        name='current_user'
    ),

    path(
        'api/instructor/',
        InstructorView.as_view(),
        name='instructor'
    ),
    path(
        'api/instructor/<int:pk>',
        InstructorPkView.as_view(),
        name='instructor_pk'
    ),

    path(
        'api/course/',
        CourseView.as_view(),
        name='course'
    ),
    path(
        'api/course/<int:pk>',
        CoursePkView.as_view(),
        name='course_pk'
    ),

    path(
        'api/student/',
        StudentView.as_view(),
        name='student'
    ),
    path(
        'api/student/<int:pk>',
        StudentPkView.as_view(),
        name='student_pk'
    ),
]

urlpatterns += router.urls

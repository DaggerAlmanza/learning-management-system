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
]

urlpatterns += router.urls

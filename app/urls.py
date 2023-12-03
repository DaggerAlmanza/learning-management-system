from app.views.user_view import (
    UserPkView,
    UserView,
)
from django.urls import path
from rest_framework import routers


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
]

urlpatterns += router.urls

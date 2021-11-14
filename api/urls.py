
from django.urls import path
from .views import Record

urlpatterns = [
    path('regist_login/', Record.as_view(), name="register"),
]

from django.urls import path
from userperm.views import index

urlpatterns = [
    path('', index.as_view()),
]

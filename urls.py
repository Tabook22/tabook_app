from django.urls import path
from . import views

app_name='tabook_app'

urlpatterns=[
    path('index/',views.index_view, name='index')
]
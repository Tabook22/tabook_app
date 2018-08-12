from django.urls import path
from . import views

app_name='tabook_app'

urlpatterns=[
    path('',views.index_view, name='index'),
    path('lst/',views.artlst_view, name='lst'),
]

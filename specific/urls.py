from specific.views import*
from django.urls import path
app_name='some'

urlpatterns=[
    path('lipsa/',lipsa,name='lipsa'),
    path('ranu/',ranu,name='ranu'),
]
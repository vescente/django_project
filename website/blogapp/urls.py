from django.urls import path
from blogapp.views import main_view


urlpatterns = [
    path('', main_view, name='main_view'),
     
]

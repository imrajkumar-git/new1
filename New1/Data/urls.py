from django.urls import path
from .views import Data
from .import views

urlpatterns = [
    path('',views.Data, name='Homepage'),

]
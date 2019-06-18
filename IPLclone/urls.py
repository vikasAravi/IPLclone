from django.urls import path, include
from .views import *
urlpatterns = [
    path('seasonDetails/<int:season>', seasonClassView.as_view(), name = 'matchdetails'),
    path('matchDetails/<int:id>', matchClassView.as_view(), name = 'seasonDetails'),
]
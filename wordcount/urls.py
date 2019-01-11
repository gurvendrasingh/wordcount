
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Homepage, name='home'),
    path('count',views.count),
    
]

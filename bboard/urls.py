from django.urls import path
from . import views 
from .views import by_rubric

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:rubric_id>/', by_rubric, name = 'by_rubric')
]

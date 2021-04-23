from django.urls import path
from api import views
app_name = 'api'

urlpatterns = [
    path('',views.index, name='index'),
    path('question1/testing_production_count/', views.question1, name='question1'),
    path('question2/runtime_downtime/', views.question2, name='question2'),
]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name ='home'),
    path('create_poll', views.create_poll, name='create_poll'),
    path('<int:question_id>/details', views.detail, name ='detail'),
    path('<int:question_id>/results/', views.results, name ='results'),
    path('<int:question_id>/vote/', views.vote, name ='vote'),
]
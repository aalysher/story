from django.urls import path
from . import views

urlpatterns = [
    path('all/<int:project_id>/', views.get_stories_list)

]

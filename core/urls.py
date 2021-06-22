from django.urls import path
from . import views

urlpatterns = [
    path('all/<int:project_id>/<int:subs_id>/', views.stories_list),
    # path('detail/<int:story_id>')

]

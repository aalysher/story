from django.contrib import admin

from core.models import Project, Story, StoryFile, UserStoryFile, Subscriber

admin.site.register(Project)
admin.site.register(Story)
admin.site.register(StoryFile)
admin.site.register(UserStoryFile)
admin.site.register(Subscriber)
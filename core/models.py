from django.db import models


class Project(models.Model):
    """Проект"""
    name = models.CharField("Название", max_length=255)
    description = models.CharField("Описание", max_length=255)


class Story(models.Model):
    """Истории"""
    preview = models.ImageField("Предварительный просмотр", upload_to='story/preview/')
    start_date = models.DateTimeField()
    add_date = models.DateTimeField()
    order_num = models.IntegerField()
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    end_date = models.DateTimeField()


class StoryFile(models.Model):
    """Детали историй"""
    more_detailed_url = models.URLField()
    more_detailed_text = models.CharField("Текст в сторисе", max_length=255)
    content_type = models.CharField("Тип файла", max_length=255)
    content_url = models.URLField("Контент")
    duration = models.TimeField("Длительность сториса")
    story_id = models.ForeignKey(Story, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class UserStoryFile(models.Model):
    """Детали просмотра юзером сторисы"""
    story_file = models.ForeignKey(StoryFile, on_delete=models.DO_NOTHING)
    user = models.ForeignKey("Subscriber", on_delete=models.DO_NOTHING)
    is_watched = models.BooleanField()
    watch_date = models.DateTimeField()


class Subscriber(models.Model):
    """Пользователь"""
    subs_id = models.BigIntegerField(primary_key=True)

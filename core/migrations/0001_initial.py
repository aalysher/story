# Generated by Django 3.2.4 on 2021-06-24 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.ImageField(upload_to='story/preview/', verbose_name='Предварительный просмотр')),
                ('start_date', models.DateTimeField()),
                ('add_date', models.DateTimeField()),
                ('order_num', models.IntegerField()),
                ('end_date', models.DateTimeField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.project')),
            ],
        ),
        migrations.CreateModel(
            name='StoryFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('more_detailed_url', models.URLField()),
                ('more_detailed_text', models.CharField(max_length=255, verbose_name='Текст в сторисе')),
                ('content_type', models.CharField(max_length=255, verbose_name='Тип файла')),
                ('content_url', models.URLField(verbose_name='Контент')),
                ('duration', models.TimeField(verbose_name='Длительность сториса')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('story_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.story')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('subs_id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserStoryFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_watched', models.BooleanField()),
                ('watch_date', models.DateTimeField()),
                ('story_file', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.storyfile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.subscriber')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-01 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='(пользователь)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.author', verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.ManyToManyField(through='newapp.PostCategory', to='newapp.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации (ГГГГ-ММ-ДД)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('NW', 'Новости'), ('AT', 'Статья')], default='NW', max_length=2, verbose_name='Тип'),
        ),
    ]
# Generated by Django 4.2.16 on 2024-09-05 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'บทความ',
                'verbose_name_plural': '    บทความ',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content_app.article')),
                ('created_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='comment_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ความคิดเห็น',
                'verbose_name_plural': '   ความคิดเห็น',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='category_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'หมวดหมู่',
                'verbose_name_plural': '     หมวดหมู่',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content_app.category'),
        ),
        migrations.AddField(
            model_name='article',
            name='created_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='last_updated_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, related_name='article_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]

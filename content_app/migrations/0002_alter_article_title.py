# Generated by Django 4.2.16 on 2024-09-05 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]

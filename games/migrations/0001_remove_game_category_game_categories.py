# Generated by Django 5.1.3 on 2024-12-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', 'categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='category',
        ),
        migrations.AddField(
            model_name='game',
            name='categories',
            field=models.ManyToManyField(related_name='games', to='games.category'),
        ),
    ]
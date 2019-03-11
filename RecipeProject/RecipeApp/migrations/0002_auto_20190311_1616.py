# Generated by Django 2.0.6 on 2019-03-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipemodel',
            name='DateCreated',
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='directions',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='imageURL',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='ingredients',
            field=models.TextField(default='', max_length=2000),
        ),
    ]

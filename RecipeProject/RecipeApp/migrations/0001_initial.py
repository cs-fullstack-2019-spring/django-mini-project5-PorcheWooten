# Generated by Django 2.0.6 on 2019-03-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(max_length=200)),
                ('description', models.TextField(default='', max_length=2000)),
                ('DateCreated', models.DateField()),
                ('Creator', models.CharField(max_length=200)),
            ],
        ),
    ]
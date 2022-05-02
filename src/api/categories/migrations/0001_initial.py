# Generated by Django 4.0.4 on 2022-04-29 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
    ]

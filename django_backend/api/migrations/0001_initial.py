# Generated by Django 4.1.7 on 2023-03-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('task', models.CharField(max_length=100)),
                ('time', models.TimeField()),
            ],
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('did', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=20)),
            ],
        ),
    ]

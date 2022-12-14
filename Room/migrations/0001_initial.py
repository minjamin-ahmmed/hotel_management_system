# Generated by Django 4.1.1 on 2022-10-23 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
                ('rent', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('room_no', models.IntegerField()),
                ('room_type', models.CharField(max_length=20)),
            ],
        ),
    ]
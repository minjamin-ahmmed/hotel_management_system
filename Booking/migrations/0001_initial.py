# Generated by Django 4.1.1 on 2022-10-23 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_from', models.IntegerField()),
                ('date_to', models.IntegerField()),
                ('room_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Room.room')),
            ],
        ),
    ]
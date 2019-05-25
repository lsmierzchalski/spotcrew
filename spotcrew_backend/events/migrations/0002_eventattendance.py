# Generated by Django 2.1.7 on 2019-05-25 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAttendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_id', models.OneToOneField(db_column='event_id', on_delete=django.db.models.deletion.DO_NOTHING, to='events.Event')),
                ('user_id', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
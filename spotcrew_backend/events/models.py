from django.db import models

from sports.models import Sport
from users.models import User
from venues.models import Venue


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    venue_id = models.ForeignKey(Venue, models.DO_NOTHING, db_column='venue_id')
    host_id = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id')
    sport_id = models.ForeignKey(Sport, models.DO_NOTHING, db_column='sport_id')

    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    # TODO trim seconds
    event_start = models.DateTimeField()
    event_stop = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'events'

    @property
    def owner(self):
        return self.host_id


class EventAttendance(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event, models.DO_NOTHING, db_column='event_id')
    user_id = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id')

    class Meta:
        unique_together = [['event_id', 'user_id']]


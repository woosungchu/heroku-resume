import datetime
from resume import db
"""
class Stack(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=30, required=True)
    thumbnail = db.ImageField(thumbnail_size=(60,60,True))
    description = db.StringField(max_length=100, required=True)
    section = db.StringField(max_length=100, required=True)

    def __unicode__(self):
        return self.name

    meta = {
        'indexes': ['name','-created_at'],
        'ordering': ['-created_at']
    }
"""
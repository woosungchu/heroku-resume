import datetime
from flask import url_for
from resume import db
from user.models import User

class Post(db.Document):
    id = db.ObjectIdField(primary_key=True)
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    author = db.ReferenceField(User, required=False)
    hidden = db.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['id','-created_at', 'author'],
        'ordering': ['-created_at']
    }
    
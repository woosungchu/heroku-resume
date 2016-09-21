import datetime
from flask import url_for
from resume import db
from user.models import User

class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    tags = db.StringField(max_length=255)
    body = db.StringField(required=True)
    author = db.ReferenceField(User, required=False)

    def get_absolute_url(self):
        return url_for('post', kwargs={"tags": self.tags})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'author','title'],
        'ordering': ['-created_at']
    }
    
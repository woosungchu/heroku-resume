import datetime
from flask import url_for
from resume import db

class User(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    email = db.EmailField(max_length=50,  primary_key=True)
    name = db.StringField(max_length=30, default="guest", required=True)
    password = db.StringField(min_length=4 ,max_length=255, required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={"email": self.email})

    def __unicode__(self):
        return self.name

    meta = {
        'indexes': ['-created_at','email','name'],
        'ordering': ['-created_at']
    }
    
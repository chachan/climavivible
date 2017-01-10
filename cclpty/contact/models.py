from google.appengine.ext import ndb


class Greeting(ndb.Model):
    content = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class Contact(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    subject = ndb.StringProperty()
    message = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)



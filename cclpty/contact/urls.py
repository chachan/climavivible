from django.conf.urls import patterns, url
from contact.views import ContactView

urlpatterns = patterns('',)

urlpatterns += [
    url(regex=r'^contact/$', view=ContactView.as_view(), name='contact_form'),
]

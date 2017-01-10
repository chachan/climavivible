from django.conf.urls import patterns, url
from main.views import IndexView, VolunteersView, TariffView, JoinUpView

urlpatterns = patterns('',)

urlpatterns += [
    url(r'^$', IndexView.as_view()),
    url(r'^voluntarios/$', VolunteersView.as_view()),
    url(r'^tarifas/$', TariffView.as_view()),
    url(r'^unete/$', JoinUpView.as_view()),
]

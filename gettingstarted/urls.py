from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^create_account', hello.views.create_chequing, name='create_chequing'),
    url(r'^pay_day', hello.views.pay_day, name='pay_day'),
    url(r'^shopping', hello.views.shopping, name='shopping'),
    url(r'^init', hello.views.init, name='init'),
    url(r'^save', hello.views.save, name='save'),
    url(r'^delete_goal', hello.views.deleteGoal, name='deleteGoal'),
    url(r'^admin/', include(admin.site.urls)),
]

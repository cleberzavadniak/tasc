from django.conf.urls import url

import core.views

urlpatterns = [
    url(r'^$', core.views.index),
    url(r'^index/?$', core.views.index),
    url(r'^cells/?$', core.views.cells),
]

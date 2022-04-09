from django.urls import path

from contact.views import   ContactUs
urlpatterns = [
    path('', ContactUs, name='contact'),

]

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^submit/post$', views.submit_post, name='submit_post'),
    url(r'^submit/Purchaseinq$', views.submit_Purchaseinq, name='submit_Purchaseinq'),

]
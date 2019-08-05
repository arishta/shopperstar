from django.urls import path
from . import views


urlpatterns=[
path('',views.PaymentView.as_view(),name='payment'),
]
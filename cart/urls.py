from django.urls import path
from .views import CartRemoveView,CartAddView,CartDisplay


urlpatterns=[path('add',CartAddView.as_view(),name='add to cart'),
path('remove',CartRemoveView.as_view(),name='remove from cart'),
path('display',CartDisplay.as_view(),name='cart display'),
]
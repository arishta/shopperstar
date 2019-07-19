from django.urls import path
from .views import CategoryView,SubcategoryView

app_name='category'

urlpatterns=[
path('category',CategoryView.as_view(),name='category'),
path('subcategory',SubcategoryView.as_view(),name='subcategory')
]
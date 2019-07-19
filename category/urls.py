from django.urls import path
from .views import CategoryView,SubcategoryView,ProductView

app_name='category'

urlpatterns=[
path('category',CategoryView.as_view(),name='category'),
path('subcategory',SubcategoryView.as_view(),name='subcategory'),
path('product',ProductView.as_view(),name='product'),
]
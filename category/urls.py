from django.urls import path
from .views import CategoryView,SubcategoryView,ProductView,SearchView

app_name='category'

urlpatterns=[
path('category',CategoryView.as_view(),name='category'),
path('subcategory',SubcategoryView.as_view(),name='subcategory'),
path('product',ProductView.as_view(),name='product'),
path('search',SearchView.as_view(),name='search'),
]
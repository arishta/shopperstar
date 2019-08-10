from django.urls import path
from . import views
app_name='login_signup'

urlpatterns=[
	path('login',views.login,name='login'),
	path('signup',views.signup,name='signup'),
	path('profile',views.ProfileView.as_view(),name='profile')
]
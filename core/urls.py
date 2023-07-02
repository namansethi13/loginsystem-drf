from django.contrib import admin
from django.urls import path
from knox import views as knox_views
from django.urls import path
from accounts.views import LoginAPI , RegisterAPI , profile
from drf_spectacular.views import SpectacularAPIView , SpectacularSwaggerView
urlpatterns = [
    path('admin/', admin.site.urls), #admin panel with all the user objects
    path('register', RegisterAPI.as_view(), name='register'), # register user Method is POST
    path('login', LoginAPI.as_view(), name='login'), # login user Method is POST
    path('logout', knox_views.LogoutView.as_view(), name='logout'), # Logout the user Method id POSR
    path('profile', profile, name='profile'), # Update or view the profile Method is PUT for updation and GET for creation
]

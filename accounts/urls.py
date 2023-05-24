from django.urls import path
from . import views
urlpatterns = [
        path('register/',views.register,name='register'),     
        path('login/',views.login_as_assamese,name='login'),
        path('login/',views.login_as_bodo,name='login-bd'),
        path('logout/',views.logout_as,name='logout'),  
]
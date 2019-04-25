from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', obtain_jwt_token),
    path('token/refresh/', refresh_jwt_token),
    path('info/', views.user_info),
]

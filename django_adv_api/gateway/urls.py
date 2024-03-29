from django.urls import path
from .views import LoginView,RegisterView,RefreshView,GetSecureInfo


urlpatterns = [
    path('login',LoginView.as_view()),
    path('register/',RegisterView.as_view()),
    path('refresh/',RefreshView.as_view()),
    path('secure-info/',GetSecureInfo.as_view()),
]
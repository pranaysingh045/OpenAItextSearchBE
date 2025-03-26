from django.urls import path
from llmapp.views import *
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('search-text/',SearchTextApi.as_view(),name='Search-text'),
    path('register/', RegisterView.as_view(), name='register'),
]
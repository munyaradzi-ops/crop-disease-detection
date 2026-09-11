from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict_disease, name='predict_disease'),
     # 📱 Mobile Mobile Application API Endpoint
    path('api/predict/', views.api_predict_disease, name='api_predict_disease'),
     path('api/login/', views.api_login, name='api_login'),
]

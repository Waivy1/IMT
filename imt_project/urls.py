from django.urls import path
from core import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index_page'),
    path('login', views.Login.as_view(), name='login'),
    path('sign_up', views.SignUp.as_view(), name='sign_up'),
    path('history', views.History.as_view(), name='history')
]



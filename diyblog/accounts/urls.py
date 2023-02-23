from django.urls import include, path
from accounts import views



urlpatterns = [
    path('signup/', views.SignUpCreateView.as_view(), name='signup')
]

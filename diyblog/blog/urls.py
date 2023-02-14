from django.urls import path
# from . import views
from blog import views



urlpatterns = [
    # TODO: fill
    path('', views.index, name='index'),
    # path('blogs/'),
    # path('blog/<int:pk>'),
    # path('blog/<int:pk>/comments'),
    # path('blogger/'),
    # path('blogger/<int:pk>'),
]
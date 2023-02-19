from django.urls import path
from blog import views
from blog import views



urlpatterns = [
    # TODO: fill
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blog_list'),
    # path('blog/<int:pk>'),
    # path('blog/<int:pk>/comments'),
    path('bloggers/', views.BloggersListView.as_view(), name='bloggers_list'),
    # path('blogger/<int:pk>'),
]

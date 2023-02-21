from django.urls import path
from blog import views



urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blog_list'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('<int:pk>/comments', views.BlogCommentCreate.as_view(), name='blog-detail-comments'),
    path('bloggers/', views.BloggersListView.as_view(), name='bloggers_list'),
    path('blogger/<int:pk>', views.BloggersDetailView.as_view(), name='bloger-detail'),
]

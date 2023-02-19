from django.urls import path
from blog import views



urlpatterns = [
    # TODO: fill
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blog_list'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    # path('blog/<int:pk>/comments', ***, name='blog-detail-comment'),
    path('bloggers/', views.BloggersListView.as_view(), name='bloggers_list'),
    # path('blogger/<int:pk>', views.BloggersDetailView.as_view(), name='bloger-detail'),
]

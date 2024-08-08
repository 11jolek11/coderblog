from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>', views.post_detail_by_id, name='post_detail_by_id'),
    path('posts/<slug:post_slug>', views.post_detail_by_slug, name='post_detail_by_slug'),
]

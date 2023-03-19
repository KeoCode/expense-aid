from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add/', views.AuthorCreateView.as_view(), name='add_post'),
    path('post/<slug:slug>/update',
         views.AuthorUpdateView.as_view(),
         name='update_post'),
    path('post/<slug:slug>/delete',
         views.AuthorDeleteView.as_view(),
         name='delete_post'),
]

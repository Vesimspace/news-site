from django.urls import path
from news.API import views as api_views

urlpatterns = [
    path('writers/', api_views.AppUserListCreateAPIView.as_view(), name='writer-list'),
    path('articles/', api_views.ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>', api_views.ArticleDetailAPIView.as_view(), name='article-detail'),
    path('articles/<int:article_pk>/comment', api_views.CommentCreateAPIView.as_view(), name='comment'),
    path('comments/<int:pk>', api_views.CommentDetailAPIView.as_view(), name='comment-detail'),
]
from rest_framework import status, generics
from rest_framework.response import Response # Redirect, Render
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from news.models import Article, AppUser, Comment
from news.API.serializers import ArticleSerializer, AppUserSerializer, CommentSerializer
from news.API.permissions import IsAdminUserOrReadOnly

class AppUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
  
class ArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        article_pk = self.kwargs.get('article_pk')
        article = get_object_or_404(Article, pk=article_pk)
        user = self.request.user
        comments = Comment.objects.filter(article=article, commenter=user)
        if comments.exists:
            raise ValidationError('You can only write 1 comments for a article.')
        serializer.save(article=article, commenter=user)

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

  


from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post,Comment,Like
from .serializer import PostSerializer,CommentSerializer,LikeSerializer

#saving the  users info
class Postlistcreateview(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class =  PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create_or_perform(self, serializer):
        serializer.save(author=self.request.user)

#  Comments View
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(author=self.request.user, post_id=post_id)

# Likes View
class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(user=self.request.user, post_id=post_id)
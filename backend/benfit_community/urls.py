from django.urls import path
from .views import Postlistcreateview,CommentListCreateView,LikeCreateView

urlpatterns = [
    path('posts/', Postlistcreateview.as_view(),  name='post-lcreated-list'),
    path('<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('<int:post_id>/like/', LikeCreateView.as_view(), name='like-create'),
]

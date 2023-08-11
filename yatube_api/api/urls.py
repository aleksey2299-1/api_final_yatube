from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('follow/', FollowViewSet.as_view()),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

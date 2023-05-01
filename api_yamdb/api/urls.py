from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet, users_get_token,
                    users_signup)

app_name = 'api'

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('genres', GenreViewSet, basename='genre')
router.register('categories', CategoryViewSet, basename='category')
router.register('titles', TitleViewSet, basename='title')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', users_signup),
    path('v1/auth/token/', users_get_token),
]

import uuid

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from reviews.models import Title, User

from api_yamdb.settings import ADMIN_EMAIL


class TitleFilter(filters.FilterSet):
    category = filters.CharFilter(
        field_name='category__slug',
        lookup_expr='icontains',
    )
    genre = filters.CharFilter(
        field_name='genre__slug',
        lookup_expr='icontains',
    )
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
    )
    year = filters.NumberFilter(
        field_name='year',
        lookup_expr='icontains',
    )

    class Meta:
        model = Title
        fields = '__all__'


def send_confirmation_code(username):
    user = get_object_or_404(User, username=username)
    confirmation_code = str(uuid.uuid4)
    user.confirmation_code = confirmation_code
    send_mail(
        'Код подтвержения для завершения регистрации',
        f'Ваш код для получения JWT токена {user.confirmation_code}',
        ADMIN_EMAIL,
        [user.email],
        fail_silently=False,
    )

from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import (SET_NULL, CharField, EmailField, ForeignKey,
                              ManyToManyField, PositiveSmallIntegerField,
                              SlugField, TextField)

from .validators import validate_username, validate_year


class User(AbstractUser):

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    USER_ROLE_CHOICES = (
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Админ'),
    )

    role = models.CharField(
        'Роль',
        max_length=50,
        choices=USER_ROLE_CHOICES,
        default=USER,
        blank=True,
        null=True
    )
    username = models.CharField(
        'Никнейм',
        validators=(validate_username,),
        max_length=150,
        unique=True,
        blank=False,
        null=False
    )

    email = EmailField(
        'Почт@',
        max_length=254,
        null=False,
        blank=False,
        unique=True,
    )

    first_name = CharField(
        'Имя',
        max_length=150,
        blank=True
    )

    middle_name = CharField(
        'Отчество',
        max_length=20,
        null=True,
        blank=True,
    )

    last_name = CharField(
        'Фамилия',
        max_length=150,
        blank=True
        # интересный факт самая длинная
        # фамилия в мире состоит из 35 букв
    )

    bio = models.TextField(
        'Биография',
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=254,
        null=True,
        blank=False,
        default='XXXX'
    )

    @property
    def is_user(self):
        return self.role == User.USER

    @property
    def is_admin(self):
        return self.role == User.ADMIN

    @property
    def is_moderator(self):
        return self.role == User.MODERATOR

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email'
            )
        ]

    def __str__(self):
        return self.username


class Genre(models.Model):
    name = CharField(max_length=70)
    slug = SlugField(unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = CharField(max_length=70)
    slug = SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = TextField(max_length=255, verbose_name='Название тайтла')
    year = PositiveSmallIntegerField(
        verbose_name='год создания',
        validators=(validate_year,),
    )
    description = TextField(verbose_name='Описание')
    genre = ManyToManyField(Genre,
                            verbose_name='Жанр',
                            blank=True,
                            )
    category = ForeignKey(Category,
                          verbose_name='Категория',
                          on_delete=SET_NULL,
                          blank=True,
                          null=True)

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    text = models.TextField(
        max_length=200
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    score = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(1, 'Оценка не может быть ниже 1!'),
            MaxValueValidator(10, 'Оценка не может быть выше 10!')
        ),
        verbose_name='Оценка'
    )
    pub_date = models.DateTimeField(
        'дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author', ),
                name='unique review'
            )]
        ordering = ('pub_date',)

    def __str__(self):
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='отзыв'
    )
    text = models.CharField(
        'текст комментария',
        max_length=200
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='автор'
    )
    pub_date = models.DateTimeField(
        'дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text


import csv
import os

from django.conf import settings
from django.core.management import BaseCommand
from reviews.models import (Category, Comment, Genre, GenreTitle, Review,
                            Title, User)

encoding = 'utf-8'


path = f'{settings.BASE_DIR}/static/data'
os.chdir(path)


class Command(BaseCommand):
    help = 'Загрузка данных в БД'

    def handle(self, *args, **kwargs):

        with open('users.csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = User(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    bio=row['bio']
                )
                p.save()

        with open('category.csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Category(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug']
                )
                p.save()

        with open('genre.csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Genre(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug']
                )
                p.save()

        with open('titles.csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Title(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category=Category.objects.get(id=row['category'])
                )
                p.save()

        with open('genre_title.csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = GenreTitle(
                    id=row['id'],
                    title=Title.objects.get(id=row['title_id']),
                    genre=Genre.objects.get(id=row['genre_id'])
                )
                p.save()

        with open('review.csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Review(
                    id=row['id'],
                    title=Title.objects.get(id=row['title_id']),
                    text=row['text'],
                    author=User.objects.get(id=row['author']),
                    score=row['score'], pub_date=row['pub_date']
                )
                p.save()

        with open('comments.csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Comment(
                    id=row['id'],
                    review=Review.objects.get(id=row['review_id']),
                    text=row['text'],
                    author=User.objects.get(id=row['author']),
                    pub_date=row['pub_date']
                )
                p.save()

        self.stdout.write(self.style.SUCCESS('Загрузка данных в'
                                             ' БД успешно выполнена!'))

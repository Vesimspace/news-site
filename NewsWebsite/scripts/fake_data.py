import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsWebsite.settings')
import django
django.setup()
from django.contrib.auth.models import User
import requests


from faker import Faker
def set_user():
    fake = Faker(['en_US'])

    first_name = fake.first_name()
    last_name = fake.last_name()
    user_name = f'{first_name.lower()}_{last_name.lower()}'
    email = f'{user_name}@{fake.domain_name()}'
    print(first_name, last_name, email)

    user_check = User.objects.filter(username=user_name)

    if user_check.exists():
        username = user_name + str(random.randrange(1, 99))
        user_check = User.objects.filter(username=user_name)

    user = User(
        username = user_name, 
        first_name = first_name,
        last_name = last_name,
        email = email,
        is_staff = fake.boolean(chance_of_getting_true=50),
    )

    user.set_password('vesimspace123,')
    user.save()
    print('User is saved, hello', {user_name})

from pprint import pprint
from news.API.serializers import ArticleSerializer, CommentSerializer, AppUserSerializer

def add_article(subject):
    fake = Faker(['en_US'])
    url = 'https://openlibrary.org/search.json'
    payload = {'q': subject}
    response = requests.get(url, params=payload)

    if response.status_code != 200:
        print('Not succesfull', response.status_code)
        return

    jsn = response.json()
    articles = jsn.get('docs')

    for article in articles:
        article_name = article.get('title')
        data = dict(
            name = article_name,
            writer = article.get('author_name')[0],
            description = '-'.join(article.get('text')),
 #           publication_date = fake.date_time_between(start_date='-20y', end_date='now', tzinfo=None),
        )
        
        serializer = AppUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('article is saved: ', article_name)
        else:
            continue
from django.core.management.base import BaseCommand
from task_4_5_app.models import Author, Post, Comment
from random import sample, randint, choices
from datetime import date, datetime

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. " \
        "Accusamus accusantium aut beatae consequatur consequuntur cumque, " \
        "delectus et illo iste maxime nihil non nostrum odio officia, perferendis " \
        "placeat quasi quibusdam quisquam quod sunt tempore temporibus ut voluptatum? " \
        "A aliquam culpa ducimus, eaque eum illo mollitia nemo " \
        "tempore unde vero! Blanditiis deleniti ex hic, laboriosam maiores odit officia praesentium " \
        "quae quisquam ratione, reiciendis, veniam. Accusantium assumenda consectetur consequatur " \
        "consequuntur corporis dignissimos ducimus eius est eum expedita illo in, inventore " \
        "ipsum iusto maiores minus mollitia necessitatibus neque nisi optio quasi quo quod, " \
        "quos rem repellendus temporibus totam unde vel velit vero vitae voluptates."

catejory = ['sports', 'cooking', 'art', 'fantasy', 'prose', 'classic', 'novel', 'documentation', 'study', 'humor']
comments = ['like', 'dislike']


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}',
                            lastname=f'Egorof_{i}',
                            email=f'mail{i}@mail.ru',
                            bmography=f'{" ".join(sample(text, 30))}',
                            date_of_birth=date(randint(1980, 2000), randint(1, 12), randint(1, 28))
                            )
            author.save()

            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=64)),
                    data_publication=datetime(randint(2010, 2024), randint(1, 12), randint(1, 28),
                                              randint(0, 23), randint(10, 59), randint(10, 59)),
                    author=author,
                    category=choices(catejory),
                    count_of_views=0,
                    flag_publicaton=True
                )
                post.save()

        for i in range(1, count + 1):
            comment = Comment(
                author=Author.objects.filter(pk=i).first(),
                post=Post.objects.filter(pk=randint(1, count)).first(),
                comment=choices(comments),
                data_comment=datetime(randint(2010, 2024), randint(1, 12), randint(1, 28),
                                      randint(0, 24), randint(10, 59), randint(10, 59)),
                data_comment_remuve=datetime.now()
            )
            comment.save()


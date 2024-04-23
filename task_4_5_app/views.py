import logging
from django.shortcuts import render, get_object_or_404
from .models import Author, Post, Comment
from .forms import AuthorForm, PostForm
from datetime import date

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'сработало представление index ')
    return render(request, 'task_4_5_app/index.html')


def author_posts(request, author_id):
    logger.info(f'сработало представление author_posts ')
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('id')
    return render(request, 'task_4_5_app/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    logger.info(f'сработало представление post_full')
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'task_4_5_app/post_full.html', {'post': post})


def info_post(request, post_id):
    logger.info(f'сработало представление info_post')
    posts = get_object_or_404(Post, pk=post_id)
    posts.count_of_views += 1
    posts.save()
    comment = Comment.objects.filter(post_id=post_id)
    content = {'posts': posts, 'comment': comment}
    return render(request, 'task_4_5_app/info_post.html', content)


def author_form(request):
    if request.method == 'POST':
        logger.info('**********start author_form_create_db')
        form = AuthorForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            bmography = form.cleaned_data['beography']
            date_of_birth = form.cleaned_data['date_of_birth']
            author = Author(
                name=name,
                lastname=lastname,
                email=email,
                bmography=bmography,
                date_of_birth=date_of_birth.__str__(),
            )
            author.save()
            message = 'Автор сохранён'
    else:
        form = AuthorForm()
        message = 'Заполните форму'
    return render(request, 'task_4_5_app/author_create_form.html', {'form': form, 'message': message})


def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            data_publication = form.cleaned_data['data_publication']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            flag_publicaton = form.cleaned_data['flag_publicaton']
            logger.info(f'{title = } {content = }'
                        f'{data_publication = } {author = } {category = } {flag_publicaton = }')
            post = Post(
                title=title,
                content=content,
                data_publication=data_publication,
                author=Author.objects.filter(pk=author).first(),
                category=category,
                flag_publicaton=flag_publicaton
            )
            post.save()
            message = 'Статья сохранена'
    else:
        form = PostForm()
        message = 'Создайте статью'
        title = 'Post create'
    return render(request, 'task_4_5_app/post_create_form.html', {'form': form, 'message': message, 'title': title})

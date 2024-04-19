from django.urls import path
from .views import author_posts, post_full, index, info_post, author_form, post_form


urlpatterns = [
    path('', index, name='index'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full'),
    path('info_post/<int:post_id>/', info_post, name='info_post'),
    path('authorcreate/', author_form, name='author_form'),
    path('postcreate/', post_form, name='post_form')
]

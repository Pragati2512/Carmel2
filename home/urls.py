from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [

    path("", views.index, name='index'),
    path("about/", views.about1, name='about'),
    path("admin123/", views.admin_page, name='admn'),
    path("contact/", views.contact, name='contact'),
    path("facilities/", views.facility, name='facility'),

    path("gallery/", views.gallery1, name='gallery'),
    path("gallery/add", views.gallery_add, name='gal-add'),
    path('gallery/<int:pk>', views.gallery2 , name='gal-sec'),
    path("gallery/section/add", views.gallery_type_add, name='gal-sec-add'),
    path('gallery/list', views.gallery_list , name='gal-list'),
    path('delete/<int:pk>', views.del_img , name='img-del'),
    path('delete/section/<int:pk>', views.del_gal , name='sect-del'),

    path("article/add", views.article_form, name='article-add'),
    path("articles", views.article_page, name='article-all'),
    path("article/list", views.article_list, name='article-list'),
    path("article/<int:pk>", views.articles, name='article'),
    path("article/del/<int:pk>", views.article_delete, name='article-del'),

    path("news/", views.news_page, name='news-all'),
    path("news/add", views.news_form, name='news-add'),
    path("news/list", views.news_list, name='news-list'),
    path("news/del/<int:pk>", views.news_delete, name='news-del'),

    path("teacher/", views.teacher_page, name='tech'),
    path("teacher/add", views.teacher_form, name='tech-add'),
    path("teacher/list", views.teacher_list, name='tech-list'),
    path("teacher/del/<int:pk>", views.teacher_delete, name='tech-del'),

]


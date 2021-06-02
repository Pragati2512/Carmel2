from django import forms
from .models import  gallery, gallery_type, article, news, teacher


class GalleryForm(forms.ModelForm):
    class Meta:
        model = gallery
        fields = ('name', 'category', 'image' )


class GalleryTypeForm(forms.ModelForm):
    class Meta:
        model = gallery_type
        fields = ('name',  'description', 'type_image'  )


class ArticleForm(forms.ModelForm):
    class Meta:
        model = article
        fields = ('title', 'description','author','author_post', 'image' )


class NewsForm(forms.ModelForm):
    class Meta:
        model = news
        fields = ('title', 'description', 'news_image',  'news_file' )


class TeacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ('name', 'subject', 'tech_img' )

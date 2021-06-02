from django.db import models
import datetime


class gallery_type(models.Model):
    name = models.CharField(max_length=  40)
    description = models.TextField(blank=True)
    type_image = models.FileField(upload_to='gallery/' , blank=True, null=True)

    def __str__(self):
        return self.name


class gallery (models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(gallery_type , on_delete=models.CASCADE)
    dated_on = models.DateField(default=datetime.date.today)
    image = models.FileField(upload_to='gallery/' , blank=True, null=True)

    def __str__(self):
        return self.name


class article (models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=40)
    author_post = models.CharField(max_length=40)
    dated_on = models.DateField(default=datetime.date.today)
    image = models.FileField(upload_to='article/' , blank=True, null=True)

    def __str__(self):
        return self.title


class news(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    date = models.DateField(default=datetime.date.today)
    news_image = models.FileField(upload_to='news/')
    news_file = models.FileField(upload_to='news/', blank=True)

    def __str__(self):
        return self.title


class teacher(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    tech_img = models.FileField(upload_to='news/')

    def __str__(self):
        return self.name

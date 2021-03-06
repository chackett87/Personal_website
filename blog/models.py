from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Entry(models.Model):
    author = models.ForeignKey(User, related_name='entries')
    body = models.TextField()
    title = models.CharField(max_length=45, null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if self.title:
            return self.title
        else:
            return '{}...'.format(self.body[:20])


class Author(models.Model):
    name = models.CharField(max_length=120)
    bio = models.TextField()

    def __unicode__(self):
        return u"{}".format(self.name)


class Post(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey(Author, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __unicode__(self):
        return u"{}".format(self.title)
from django.db import models

# class Author(models.Model):
#   name = models.CharField(max_length=80)
#   bio= models.TextField()

#   def __unicode__(self):
#     return u"{}".format(self.name)

# class Tag(models.Model):
#   name = model.CharField(max_length=20)

#   def __unicode__(self):
#     return u"{}".format(self.name)

# class Post(models.Model):
#   created = models.DateField(auto_now_add=True)
#   title = models.CharField(max_length=120)
#   body = models.TextField()
#   author = models.ForeignKey(Author, related_name="posts")
#   tags = models.ManyToManyField(Tag, related_name="posts")

#   def __unicode__(self):
#     return u"{}".format(self.title)

    
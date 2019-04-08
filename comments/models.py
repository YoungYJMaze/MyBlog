from django.db import models


# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post', on_delete="DESC")

    def __str__(self):
        return self.text[:20]

    def get_belong_post(self):
        return self.post


class Essay_Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    essay = models.ForeignKey('blog.Essay', on_delete="DESC")

    def __str__(self):
        return self.text[:20]

    def get_belong_essay(self):
        return self.essay


class leave_messages():
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text[:20]
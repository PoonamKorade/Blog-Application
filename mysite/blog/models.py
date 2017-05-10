from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
#Model for post class
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #List of comments approved by the author
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    #After the post has been created and published the user will be directed to the details page of the post
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

#Model for comments class
class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    #After the comment has been posted user will be directed to the list of all posts since comment has not been approved yet.
    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text

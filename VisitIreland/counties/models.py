from django.db import models
from django.contrib.auth.models import User


class County(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    paragraph = models.TextField(max_length=1000)

    def __str__(self):
        return self.name



class Attraction(models.Model):
    subject = models.CharField(max_length=255)
    paragraph1 = models.TextField(max_length=4000)
    paragraph2 = models.TextField(max_length=4000)
    title =  models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    county = models.ForeignKey(County, related_name='attractions')
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.subject


class Comment(models.Model):
    message = models.TextField(max_length=4000)
    attraction = models.ForeignKey(Attraction, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='comments')
    updated_by = models.ForeignKey(User, null=True, related_name='+')

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)# using the Truncator utility class to truncate long strings into an arbitrary string size (here we are using 30).
    def get_comment_count(self):
        return Comment.objects.filter(attraction__county=self).count()

    def get_last_comments(self):
        return Comment.objects.filter(attraction__county=self).order_by('-created_at').first()
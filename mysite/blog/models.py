from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.



class Post(models.Model):
    post_text = models.TextField()
    post_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    photo = models.ImageField(upload_to='post_images/', null=True, blank=True)
    
    def __str__(self):
        return self.post_title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_date = models.DateTimeField()
    like = models.BooleanField()
    
    def __str__(self):
        return self.comment_text
    
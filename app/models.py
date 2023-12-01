from django.db import models

# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=250, help_text="This is the title bitch")
    body= models.TextField()
    category=models.TextField(null=True,blank=True)
    picture=models.ImageField(upload_to='blog')
    date_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
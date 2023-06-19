from django.db import models

# Create your models here.
class CreateBlog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    metaTitle = models.CharField(max_length=1000)
    slug = models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    metaDescription = models.CharField(max_length=1000)
    body = models.TextField()
    image = models.TextField()
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + self.author
from django.db import models

# Create your models here.
# profile/models.py

class Resume(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    
    def __str__(self):
        return self.name
    
from django.db import models
from cloudinary.models import CloudinaryField

class Event(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')


    def __str__(self):
        """
        string title
        """
        return str(self.title)
        
    

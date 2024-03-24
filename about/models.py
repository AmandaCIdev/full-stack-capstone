from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


from django.db import models
# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=100, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SubmitDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    phone_number = models.IntegerField()

    def __str__(self):
        return f"Submit your details - request from {self.name}"

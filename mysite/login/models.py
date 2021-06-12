from django.db import models

from django.utils.text import slugify


# Create your models here.
class Person(models.Model):
    GENDER_CHOICES = {
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    }
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=20,
                              choices=GENDER_CHOICES,
                              default='male')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('last_name', )

    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

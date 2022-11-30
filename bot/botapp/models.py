from django.db import models

# Create your models here.
class Words(models.Model):

    GENDERS = [
        ('Male', 'male'),
        ('Female', 'female'),
        ('Med', 'med'),

    ]

    word = models.CharField(verbose_name='Word', max_length=100)
    gender = models.CharField(verbose_name='Gender',max_length=7, choices=GENDERS)


    def __str__(self):
        return self.gender + ' ' + self.word



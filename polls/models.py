from django.db import models
from django.utils import timezone
# Create your models here.
class Queastion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Queastion)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
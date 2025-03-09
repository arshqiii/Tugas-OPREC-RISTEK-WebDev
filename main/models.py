from django.db import models

# Create your models here.
class Tryout(models.Model) :
    STATUS_CHOICES = [
        (True, "Submitted"),
        (False, "Draft")
    ]
    CATEGORY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, choices=STATUS_CHOICES)


class Question(models.Model):
    tryout = models.ForeignKey(Tryout, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    answer = models.BooleanField()
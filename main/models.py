from django.db import models

# Create your models here.

class Tryout(models.Model) :
    STATUS_CHOICES = [
        (True, "Submitted"),
        (False, "Draft")
    ]
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, choices=STATUS_CHOICES)

class Question(models.Model):
    tryout = models.ForeignKey(Tryout, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    answer = models.BooleanField()
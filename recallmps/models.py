from django.db import models

class recall(models.Model):
    name = models.CharField(max_length=200)
    constituency = models.CharField(max_length=200)
    VOTE_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
        ('abstain', 'Abstain'),
        ('absent', 'Absent'),
    )
    vote = models.CharField(max_length=10, choices=VOTE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.constituency})"
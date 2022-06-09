from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """Theme, which user learns"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        """Returns string model representation"""
        return self.text


class Entry(models.Model):
    """Info, which user learns by topic"""
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns string model representation"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text

from django.db import models
from django.utils import timezone


class Baslik(models.Model):
    auth = models.ForeignKey('auth.User', on_delete='CASCADE')
    kelime = models.CharField(max_length=50)
    anlami = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.kelime
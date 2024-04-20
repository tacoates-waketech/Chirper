from django.db import models
from django.urls import reverse


class Chirp(models.Model):
    title = models.CharField(max_length=50)
    chirper = models.ForeignKey( "auth.User", on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("chirp_detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    chirper = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    chirp = models.ForeignKey("Chirp", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body
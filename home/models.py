from django.db import models

class Informations(models.Model):
    information_name = models.CharField(max_length=100)
    json_text_field = models.TextField(default="{}")

    created_at = models.DateTimeField(auto_now_add=True)
    updatet_at = models.DateTimeField(auto_now=True)


class Images(models.Model):
    information = models.ForeignKey(Informations, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")

from django.db import models

from django.db import models

class Description(models.Model):
    Album = models.CharField(max_length=100)
    pic_description = models.TextField(default="{}")

class Images(models.Model):
    pic_description = models.ForeignKey(Description, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")

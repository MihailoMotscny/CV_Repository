from django.db import models

class Imagess(models.Model):
    image = models.ImageField(upload_to="images/", default=0)
    idcheckimg = models.CharField('ID:', max_length=230, blank=True)

    def __str__(self):
        return self.idcheckimg

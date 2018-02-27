from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=250)
    productLogo=models.CharField(max_length=550)

    def get_absolute_url(self):
        return reverse('contact:productpage',kwargs={'pk':self.pk})

    def __str__(self):
        return self.productName
class Versions(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    versionName = models.CharField(max_length=250)
    is_purchased=models.BooleanField(default=False)
    def __str__(self):
        return self.versionName
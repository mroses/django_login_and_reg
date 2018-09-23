from __future__ import unicode_literals

from django.db import models
from ..main.models import User
#from ..main.models import User
    #this is usually 'from models import *' or from models import all. This says ..main.models because we have 2 seperate apps - main(user) and products. Note the 2 dots .. before main in order to go up a directory and then into the products app file.

# Create your models here.
class ProductManager(models.Manager):
    pass

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    creator = models.ForeignKey(User, related_name='created_products')
    users = models.ManyToManyField(User, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()

    def __str__(self):
        output = "Product: {}".format(self.name)
        return output
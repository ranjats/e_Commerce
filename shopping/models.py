from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name =  models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    pro_Date = models.DateField()
    image = models.ImageField(upload_to="shopping/images", default="")

    def __str__(self):
        return self.product_name

# create Model or Class Contact by column name qury_id, name, email


class Contact(models.Model):
    qury_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80, default="")
    phone = models.CharField(max_length=80, default="")
    desc = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


from django.db import models

class customer(models.Model):
    username = models.CharField(max_length=101,primary_key=True)
    useraddress = models.CharField(max_length=300)

class fooditem(models.Model):
    foodname = models.CharField(max_length=300)
    picture = models.ImageField()
    foodprice = models.DecimalField(max_digits=10, decimal_places=2)
    foodtype = models.CharField(max_length=300)

class reviews(models.Model):
    foodid = models.ForeignKey(fooditem, on_delete=models.CASCADE)
    reviewername = models.ForeignKey(customer, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return str(self.reviewername)

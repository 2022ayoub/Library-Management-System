from django.db import models
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):

    book_status=[
        ('available','available'),
        ('rental','rental'),
        ('sold','sold')
    ]

    title=models.CharField(max_length=150)
    author=models.CharField(max_length=50)
    bookImg=models.ImageField(upload_to='uploads/',null=True , blank=True)
    authorImg=models.ImageField(upload_to='uploads/',null=True , blank=True)
    pages=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    rental_price_day=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    rental_period=models.IntegerField(null=True,blank=True)
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=50,choices=book_status,null=True,blank=True)

    category=models.ForeignKey(Category , on_delete=models.PROTECT ,null=True,blank=True)

    def __str__(self):
        return self.title
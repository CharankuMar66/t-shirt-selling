from django.db import models
from django.contrib.auth.models import User

class Catagory(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Tshirts(models.Model):
    TYPE=[('t-shirt','T-SHIRT'),('pants','PANTS')]
    SIZE=[('S','small'),('M','medium'),('L','large'),('XL','XL'),('XXL','XXL'),('XXXL','XXXL')]
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=15)
    catagory=models.ForeignKey(Catagory,max_length=2,on_delete=models.CASCADE)
    color=models.CharField(max_length=10)
    size=models.CharField(max_length=2,choices=SIZE)
    description=models.CharField()
    type=models.CharField(choices=TYPE,max_length=10)
   

    def __str__(self):
        return self.name
    

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Tshirt=models.ForeignKey(Tshirts,on_delete=models.CASCADE)
    size=models.ForeignKey(Tshirts,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    orderDate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}-{self.Tshirt.name}'



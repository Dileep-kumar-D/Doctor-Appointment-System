from django.db import models

class registration(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=25)
    age=models.IntegerField()
    dep=models.CharField(max_length=20)
    password=models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name

class patients(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=30)
    pin = models.IntegerField()
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    doctor = models.ForeignKey(registration, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name



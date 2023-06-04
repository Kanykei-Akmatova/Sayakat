from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Flight(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.CharField(max_length=255)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

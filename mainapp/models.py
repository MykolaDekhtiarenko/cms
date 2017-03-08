from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    edrpou = models.CharField(max_length=20, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.is_staff = False
    contactPersone = models.CharField(max_length=300)
    phone = models.CharField(max_length=45)
    address = models.CharField(max_length=100)
    activity = models.CharField(max_length=300, null=True)


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.is_staff = True
    phone = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    role = models.CharField(max_length=20)

class RTVResource(models.Model):
    SKU = models.CharField(max_length=100)
    owner =models.CharField(max_length=100)
    creationDate = models.DateField()
    duaration = models.IntegerField()
    campaign = models.ForeignKey(Campaign)

class NonTVResource(models.Model):
    SKU = models.CharField(max_length=100)
    owner =models.CharField(max_length=100)
    type = models.CharField(max_length=200)
    formfactor = models.CharField(max_length=60)
    campaign = models.ForeignKey(Campaign)

class Channel(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    morningTimePrice = models.DecimalField(max_digits=12, decimal_places=2)
    afternoonTimePrice = models.DecimalField(max_digits=12, decimal_places=2)
    eveningTimePrice = models.DecimalField(max_digits=12, decimal_places=2)
    nightTimePrice = models.DecimalField(max_digits=12, decimal_places=2)
    primeTimePrice = models.DecimalField(max_digits=12, decimal_places=2)

class AdvertisingPlace(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    type = models.CharField(max_length=45)
    town = models.CharField(max_length=45)
    avrPrice = models.CharField(max_length=45)

class Broadcast(models.Model):
    period = models.CharField(max_length=100)
    times = models.CharField(max_length=45)
    startDate = models.DateField()
    endDate = models.DateField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    channel = models.ForeignKey(Channel)
    tvResource = models.ForeignKey(RTVResource)

class Published(models.Model):
    month = models.CharField(max_length=45)
    year = models.CharField(max_length=45)
    amount = models.CharField(max_length=45)
    avrPrice = models.DecimalField(max_digits=12, decimal_places=2)
    nonTVResourse = models.ForeignKey(NonTVResource)
    advertisingPlace = models.ForeignKey(AdvertisingPlace)

class Campaign(models.Model):
    subject = models.TextField()
    paymentDetails = models.TextField()
    signDate = models.DateField()
    startDate = models.DateField()
    plannedEndDate = models.DateField()
    endDate = models.DateField(null=True)
    plannedPrice = models.DecimalField(max_digits=12, decimal_places=2)
    moneySpent = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    plannedBudget = models.DecimalField(max_digits=12, decimal_places=2)
    state = models.CharField(max_length=45)
    lastUpdateDate = models.DateField()
    client = models.ForeignKey(Client)
    employee = models.ForeignKey(Employee)

class Report(models.Model):
    report = models.TextField()
    date = models.DateField()
    campaign = models.ForeignKey(Campaign)
    employee = models.ForeignKey(Employee)
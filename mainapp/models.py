from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class Client(models.Model):
    edrpou = models.CharField(max_length=20, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contactPersone = models.CharField(max_length=300)
    phone = models.CharField(max_length=45)
    address = models.CharField(max_length=100)
    activity = models.CharField(max_length=300, null=True)
    def __str__(self):
        return str(self.edrpou+" "+self.user.first_name+" "+self.user.last_name)



class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    role = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        print(self.role)
        if self.role == "manager":
            manager = Group.objects.get(name="Manager")
            manager.user_set.add(self.user)
            self.user.is_staff = True
        elif self.role == "analyst":
            analyst = Group.objects.get(name="Analyst")
            analyst.user_set.add(self.user)
            self.user.is_staff=False
        else: raise "Unexpected role error!"
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user.first_name.__str__() + " " + self.user.last_name.__str__())

class Channel(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    morningTimePrice = models.DecimalField(max_digits=12, decimal_places=2)
    afternoonTimePrice = models.DecimalField(max_digits=12, decimal_places=2)
    eveningTimePrice = models.DecimalField(max_digits=12, decimal_places=2)
    nightTimePrice = models.DecimalField(max_digits=12, decimal_places=2)
    primeTimePrice = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.name

class AdvertisingPlace(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    type = models.CharField(max_length=45)
    town = models.CharField(max_length=45)
    avrPrice = models.CharField(max_length=45)
    def __str__(self):
        return self.name

class Campaign(models.Model):
    # FRESHMAN = 'FR'
    # SOPHOMORE = 'SO'
    # JUNIOR = 'JR'
    # SENIOR = 'SR'
    # YEAR_IN_SCHOOL_CHOICES = (
    #     (FRESHMAN, 'Freshman'),
    #     (SOPHOMORE, 'Sophomore'),
    #     (JUNIOR, 'Junior'),
    #     (SENIOR, 'Senior'),
    # )
    subject = models.CharField(max_length=100)
    description = models.TextField(null=True)
    paymentDetails = models.TextField()
    signDate = models.DateField(null=True)
    startDate = models.DateField()
    endDate = models.DateField(null=True)
    moneySpent = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    plannedBudget = models.DecimalField(max_digits=12, decimal_places=2)
    state = models.CharField(max_length=45)
    lastUpdateDate = models.DateField()
    client = models.ForeignKey(Client)
    employee = models.ForeignKey(Employee, null=True)
    service = models.ManyToManyField(Service)
    def __str__(self):
        return self.subject

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
    def __str__(self):
        return str(self.SKU+" "+self.type+" "+self.formfactor)

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
    price = models.DecimalField(max_digits=12, decimal_places=2)
    nonTVResourse = models.ForeignKey(NonTVResource)
    advertisingPlace = models.ForeignKey(AdvertisingPlace)
    def __str__(self):
        return str(self.nonTVResourse.SKU+" нa/у "+self.advertisingPlace.__str__()+" "+self.month+"/"+self.year)

class Report(models.Model):
    report = models.TextField()
    date = models.DateField()
    campaign = models.ForeignKey(Campaign)
    employee = models.ForeignKey(Employee)
    def __str__(self):
        return str(self.date.__str__()+" "+self.employee.user.first_name.__str__()+" "+self.employee.user.last_name.__str__())

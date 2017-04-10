# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-09 10:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisingPlace',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=45)),
                ('town', models.CharField(max_length=45)),
                ('avrPrice', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=100)),
                ('times', models.CharField(max_length=45)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('paymentDetails', models.TextField()),
                ('signDate', models.DateField()),
                ('startDate', models.DateField()),
                ('plannedEndDate', models.DateField()),
                ('endDate', models.DateField(null=True)),
                ('plannedPrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('moneySpent', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('plannedBudget', models.DecimalField(decimal_places=2, max_digits=12)),
                ('state', models.CharField(max_length=45)),
                ('lastUpdateDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('morningTimePrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('afternoonTimePrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('eveningTimePrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('nightTimePrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('primeTimePrice', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('edrpou', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('contactPersone', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=100)),
                ('activity', models.CharField(max_length=300, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=12)),
                ('role', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NonTVResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=200)),
                ('formfactor', models.CharField(max_length=60)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Published',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=45)),
                ('year', models.CharField(max_length=45)),
                ('amount', models.CharField(max_length=45)),
                ('avrPrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('advertisingPlace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.AdvertisingPlace')),
                ('nonTVResourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.NonTVResource')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.TextField()),
                ('date', models.DateField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Campaign')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='RTVResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('creationDate', models.DateField()),
                ('duaration', models.IntegerField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Client'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Employee'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='service',
            field=models.ManyToManyField(to='mainapp.Service'),
        ),
        migrations.AddField(
            model_name='broadcast',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Channel'),
        ),
        migrations.AddField(
            model_name='broadcast',
            name='tvResource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.RTVResource'),
        ),
    ]

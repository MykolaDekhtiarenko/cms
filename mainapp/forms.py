from django import forms
from mainapp.models import *

class CampaignForm(forms.Form):
    subject = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    paymentDetails = forms.CharField(widget=forms.Textarea)
    # startDate = forms.CharField(widget=forms.DateField())
    # endDate = forms.CharField(widget=forms.DateField())
    plannedBudget = forms.DecimalField(max_digits=12, decimal_places=2)







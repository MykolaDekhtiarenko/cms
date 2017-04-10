from django.template import RequestContext
from rest_framework.generics import ListAPIView, GenericAPIView
from mainapp.serializers import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from mainapp.forms import *
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.db import connection



# Create your views here.

@login_required()
def redirectUser(request):
    if  Client.objects.filter(user=request.user).exists():
        return client(request)
    elif Employee.objects.filter(user=request.user).exists():
        if request.user.employee.role=="analyst":
            return analyst(request)
        elif request.user.employee.role == "manager":
            return manager(request)
        elif request.user.employee.role == "accounter":
            return accounter(request)
    elif request.user.is_superuser:
        return redirect("/admin")
    else: raise ValueError('A very specific bad thing happened')

def client(request):
    campains = Campaign.objects.filter(client=request.user.client).values()
    overallBudget = getClientCampaignsBudget(request.user.client.edrpou)
    return render(request, 'mainapp/Client.html', {'client': request.user.client, 'campains': campains, 'budget': overallBudget})

def analyst(request):
    campains = Campaign.objects.filter(state="Active").values()
    return render(request, 'mainapp/Analyst.html', {'user': request.user, 'campains': campains,})

def manager(request):
    clients = getClientsBudgetsForEmployee(request.user.employee.id)
    campains = Campaign.objects.filter(employee=request.user.employee).values()
    return render(request, 'mainapp/Manager.html', {'user': request.user, 'campains': campains, 'clients': clients})

def accounter(request):
    rData = reportForPrint()
    return render(request, 'mainapp/Accounter.html', {'report': rData})


def order(request):
    services = Service.objects.all()
    return render(request, 'mainapp/OrderCampaign.html', {'services': services}, RequestContext(request))

def report(request, pk):
    return render(request, 'mainapp/NewReport.html', {'employee': request.user.employee.id, 'campaign': pk})



class ServiceViewSet(GenericAPIView):
    serializer_class =  ServiceSerializer
    queryset = Service.objects.all()

class EmployeeViewSet(ListAPIView):
    serializer_class =  EmployeeSerializer
    queryset = Employee.objects.all()

class CampaignViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()



class ClientCampaignDetailView(LoginRequiredMixin, DetailView):
    model = Campaign
    template_name = "mainapp/CampaignForClient.html"

    def get_queryset(self):
        queryset = super(ClientCampaignDetailView, self).get_queryset()
        # print(str("ID кампанії: "+self.kwargs['pk']))
        return queryset.filter(client=self.request.user.client)

    def get_context_data(self, **kwargs):
        # reports will be available in the template as the related objects
        context = super(ClientCampaignDetailView, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.filter(campaign=self.get_object())
        context['broadcasts'] = Broadcast.objects.raw("Select mainapp_broadcast.id, period, times, startDate, endDate, price, channel_id, mainapp_rtvresource.SKU, mainapp_rtvresource.duaration From mainapp_broadcast INNER JOIN mainapp_rtvresource ON mainapp_broadcast.tvResource_id = mainapp_rtvresource.id Where tvResource_id in (Select id From mainapp_rtvresource Where mainapp_rtvresource.campaign_id = " + self.kwargs['pk'] + ")")
        context['publications'] = Published.objects.raw("Select mainapp_published.id, month, year, amount, price, mainapp_nontvresource.SKU, mainapp_nontvresource.type, mainapp_nontvresource.formfactor, mainapp_advertisingplace.name, mainapp_advertisingplace.town, mainapp_advertisingplace.type From (mainapp_published INNER JOIN mainapp_nontvresource ON mainapp_published.nonTVResourse_id = mainapp_nontvresource.id) INNER JOIN mainapp_advertisingplace ON mainapp_published.advertisingPlace_id = mainapp_advertisingplace.name  Where nonTVResourse_id in (Select id From mainapp_nontvresource Where mainapp_nontvresource.campaign_id = " + self.kwargs['pk'] + ")")
        context['tvresourses'] = RTVResource.objects.filter(campaign=self.get_object())
        context['nontvresourses'] = NonTVResource.objects.filter(campaign=self.get_object())
        return context

class ManagerCampaignDetailView(LoginRequiredMixin, DetailView):
    model = Campaign
    template_name = "mainapp/CampaignForManager.html"

    def get_queryset(self):
        queryset = super(ManagerCampaignDetailView, self).get_queryset()
        return queryset.filter(employee=self.request.user.employee)

    def get_context_data(self, **kwargs):
        context = super(ManagerCampaignDetailView, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.filter(campaign=self.get_object())
        context['broadcasts'] = Broadcast.objects.raw("Select mainapp_broadcast.id, period, times, startDate, endDate, price, channel_id, mainapp_rtvresource.SKU, mainapp_rtvresource.duaration From mainapp_broadcast INNER JOIN mainapp_rtvresource ON mainapp_broadcast.tvResource_id = mainapp_rtvresource.id Where tvResource_id in (Select id From mainapp_rtvresource Where mainapp_rtvresource.campaign_id = " + self.kwargs['pk'] + ")")
        context['publications'] = Published.objects.raw("Select mainapp_published.id, month, year, amount, price, mainapp_nontvresource.SKU, mainapp_nontvresource.type, mainapp_nontvresource.formfactor, mainapp_advertisingplace.name, mainapp_advertisingplace.town, mainapp_advertisingplace.type From (mainapp_published INNER JOIN mainapp_nontvresource ON mainapp_published.nonTVResourse_id = mainapp_nontvresource.id) INNER JOIN mainapp_advertisingplace ON mainapp_published.advertisingPlace_id = mainapp_advertisingplace.name  Where nonTVResourse_id in (Select id From mainapp_nontvresource Where mainapp_nontvresource.campaign_id = " + self.kwargs['pk'] + ")")
        context['tvresourses'] = RTVResource.objects.filter(campaign=self.get_object())
        context['nontvresourses'] = NonTVResource.objects.filter(campaign=self.get_object())
        return context

class AnalystCampaignDetailView(LoginRequiredMixin, DetailView):
    model = Campaign
    template_name = "mainapp/CampaignForAnalist.html"

    def get_queryset(self):
        queryset = super(AnalystCampaignDetailView, self).get_queryset()
        return queryset.filter(state="Active")

    def get_context_data(self, **kwargs):
        context = super(AnalystCampaignDetailView, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.filter(campaign=self.get_object())
        context['broadcasts'] = Broadcast.objects.raw(
            "Select mainapp_broadcast.id, period, times, startDate, endDate, price, channel_id, mainapp_rtvresource.SKU, mainapp_rtvresource.duaration From mainapp_broadcast INNER JOIN mainapp_rtvresource ON mainapp_broadcast.tvResource_id = mainapp_rtvresource.id Where tvResource_id in (Select id From mainapp_rtvresource Where mainapp_rtvresource.campaign_id = " +
            self.kwargs['pk'] + ")")
        context['publications'] = Published.objects.raw(
            "Select mainapp_published.id, month, year, amount, price, mainapp_nontvresource.SKU, mainapp_nontvresource.type, mainapp_nontvresource.formfactor, mainapp_advertisingplace.name, mainapp_advertisingplace.town, mainapp_advertisingplace.type From (mainapp_published INNER JOIN mainapp_nontvresource ON mainapp_published.nonTVResourse_id = mainapp_nontvresource.id) INNER JOIN mainapp_advertisingplace ON mainapp_published.advertisingPlace_id = mainapp_advertisingplace.name  Where nonTVResourse_id in (Select id From mainapp_nontvresource Where mainapp_nontvresource.campaign_id = " +
            self.kwargs['pk'] + ")")
        context['tvresourses'] = RTVResource.objects.filter(campaign=self.get_object())
        context['nontvresourses'] = NonTVResource.objects.filter(campaign=self.get_object())
        return context



def getClientCampaignsBudget(client_id):
    cursor = connection.cursor()
    query = 'SELECT SUM(plannedBudget) FROM mainapp_campaign WHERE client_id="'+client_id+'"'
    cursor.execute(query)
    row = [item[0] for item in cursor.fetchall()]
    return row[0]

def getClientsBudgetsForEmployee(employee_id):
    cursor = connection.cursor()
    query = 'SELECT  last_name, first_name, SUM(plannedBudget) AS money FROM mainapp_campaign, auth_user u WHERE employee_id='+str(employee_id)+' AND mainapp_campaign.client_id IN (SELECT c.edrpou FROM mainapp_client c WHERE c.user_id = u.id) GROUP BY mainapp_campaign.client_id'
    cursor.execute(query)
    row = dictfetchall(cursor)
    print(row)
    return row

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    # print(desc)
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def reportForPrint():
    cursor = connection.cursor()
    query = 'SELECT SUM(plannedBudget) AS budget, first_name, last_name, salary FROM auth_user INNER JOIN mainapp_employee ON auth_user.id = mainapp_employee.user_id, mainapp_campaign c WHERE c.employee_id IN(SELECT mainapp_employee.id FROM mainapp_employee WHERE user_id=auth_user.id) GROUP BY c.employee_id'
    cursor.execute(query)
    row = dictfetchall(cursor)
    return row


# def getClientCampaignsBudget(client_id):
#     cursor = connection.cursor()
#     query = 'SELECT SUM(plannedBudget) FROM mainapp_campaign WHERE client_id="'+client_id+'"'
#     cursor.execute(query)
#     row = [item[0] for item in cursor.fetchall()]
#     return row[0]

# загальний бюджет кампаній клієнта
# SELECT SUM(mainapp_campaign.plannedBudget)
# FROM mainapp_campaign
# WHERE client_id="RRR1212GG";

# керівник-його сумарний бюджет
# SELECT employee_id, SUM(plannedBudget)
# FROM mainapp_campaign
# GROUP BY employee_id;




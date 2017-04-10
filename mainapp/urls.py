from django.conf.urls import url, include
from rest_framework import routers
from mainapp.views import *


router = routers.DefaultRouter()
router.register(r'campaign', CampaignViewSet)
router.register(r'report', ReportViewSet)
router.register(r'client', ClientViewSet)


urlpatterns = [
    url(r'^campaign/(?P<pk>[0-9]+)/$', ClientCampaignDetailView.as_view()),
    url(r'^campaign/order', order),
    url(r'^report/new/(?P<pk>[0-9]+)/$', report),
    url(r'^manager/campaign/(?P<pk>[0-9]+)/$', ManagerCampaignDetailView.as_view()),
    url(r'^analyst/campaign/(?P<pk>[0-9]+)/$', AnalystCampaignDetailView.as_view()),
    url(r'^', include(router.urls)),


]
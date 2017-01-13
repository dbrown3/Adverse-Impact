__author__ = 'dbrown3'
from django.conf.urls import patterns, url, include

from adverseimpact import views
from adverseimpact import AdverseImpactReportExport

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^adverse_impact_export/$', AdverseImpactReportExport.adverse_impact_export_report, name='adverse_impact_export_report'),
                       )
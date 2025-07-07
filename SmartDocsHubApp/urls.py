from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'SmartDocsHubApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('certificates/', views.certificate_list, name='certificate_list'),
    path('certificates/download/', views.download_certificates, name='download_certificates'),
    path('templates/', views.template_list, name='template_list'),
    path('templates/create/', views.template_create, name='template_create'),
    path('templates/<int:pk>/edit/', views.template_edit, name='template_edit'),
    path('templates/<int:pk>/delete/', views.template_delete, name='template_delete'),
    path('invitations/', TemplateView.as_view(template_name='SmartDocsHubApp/invitation.html'), name='invitation_generator'),
    path('reports/', TemplateView.as_view(template_name='SmartDocsHubApp/report.html'), name='report_generator'),
    path('letters/', TemplateView.as_view(template_name='SmartDocsHubApp/letter.html'), name='letter_generator'),
] 
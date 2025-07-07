from django.contrib import admin
from .models import CertificateTemplate, GeneratedCertificate

@admin.register(CertificateTemplate)
class CertificateTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

@admin.register(GeneratedCertificate)
class GeneratedCertificateAdmin(admin.ModelAdmin):
    list_display = ('participant_name', 'course_name', 'email', 'created_at', 'is_sent')
    search_fields = ('participant_name', 'course_name', 'email')
    list_filter = ('is_sent', 'created_at', 'template')

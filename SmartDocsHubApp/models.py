from django.db import models
from django.utils import timezone

class CertificateTemplate(models.Model):
    name = models.CharField(max_length=100)
    template_image = models.ImageField(upload_to='templates/')
    name_x = models.IntegerField(default=0, help_text='X coordinate for name placement')
    name_y = models.IntegerField(default=0, help_text='Y coordinate for name placement')
    course_x = models.IntegerField(default=0, help_text='X coordinate for course placement')
    course_y = models.IntegerField(default=0, help_text='Y coordinate for course placement')
    date_x = models.IntegerField(default=0, help_text='X coordinate for date placement')
    date_y = models.IntegerField(default=0, help_text='Y coordinate for date placement')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class GeneratedCertificate(models.Model):
    template = models.ForeignKey(CertificateTemplate, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=200)
    email = models.EmailField()
    certificate_pdf = models.FileField(upload_to='certificates/')
    is_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.participant_name} - {self.course_name}"

    def mark_as_sent(self):
        self.is_sent = True
        self.sent_at = timezone.now()
        self.save()

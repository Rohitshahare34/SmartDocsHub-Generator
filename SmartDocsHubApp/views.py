from django.shortcuts import render, redirect
import os
import zipfile
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from .models import CertificateTemplate, GeneratedCertificate
from .forms import CertificateGenerationForm, CertificateTemplateForm

# Create your views here.

def home(request):
    """Home page with certificate generation form."""
    if request.method == 'POST':
        form = CertificateGenerationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                excel_file = request.FILES['excel_file']
                template = form.cleaned_data['template']
                send_email = form.cleaned_data['send_email']
                
                certificates = generate_certificates_from_excel(
                    excel_file=excel_file,
                    template=template,
                    send_email=send_email
                )
                
                messages.success(request, f'Successfully generated {len(certificates)} certificates!')
                return redirect('SmartDocsHubApp:certificate_list')
            
            except Exception as e:
                messages.error(request, f'Error generating certificates: {str(e)}')
    else:
        form = CertificateGenerationForm()
    
    return render(request, 'SmartDocsHubApp/home.html', {'form': form})

def certificate_list(request):
    """List all generated certificates."""
    certificates = GeneratedCertificate.objects.all().order_by('-created_at')
    return render(request, 'SmartDocsHubApp/certificate_page.html', {'certificates': certificates})

def download_certificates(request):
    """Download all certificates as a ZIP file."""
    certificates = GeneratedCertificate.objects.all()
    
    if not certificates:
        messages.error(request, 'No certificates available for download.')
        return redirect('SmartDocsHubApp:certificate_list')
    
    # Create ZIP file
    zip_filename = 'certificates.zip'
    zip_path = os.path.join(settings.MEDIA_ROOT, zip_filename)
    
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        for certificate in certificates:
            if os.path.exists(certificate.certificate_pdf.path):
                arcname = f"{certificate.participant_name}_{certificate.course_name}.pdf"
                zip_file.write(certificate.certificate_pdf.path, arcname)
    
    # Read ZIP file and send response
    with open(zip_path, 'rb') as zip_file:
        response = HttpResponse(zip_file.read(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'
        return response

def template_list(request):
    """List all certificate templates."""
    templates = CertificateTemplate.objects.all()
    return render(request, 'SmartDocsHubApp/template_list.html', {'templates': templates})

def template_create(request):
    """Create a new certificate template."""
    if request.method == 'POST':
        form = CertificateTemplateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Template created successfully!')
            return redirect('SmartDocsHubApp:template_list')
    else:
        form = CertificateTemplateForm()
    
    return render(request, 'SmartDocsHubApp/template_form.html', {'form': form})

def template_edit(request, pk):
    """Edit an existing certificate template."""
    template = CertificateTemplate.objects.get(pk=pk)
    if request.method == 'POST':
        form = CertificateTemplateForm(request.POST, request.FILES, instance=template)
        if form.is_valid():
            form.save()
            messages.success(request, 'Template updated successfully!')
            return redirect('SmartDocsHubApp:template_list')
    else:
        form = CertificateTemplateForm(instance=template)
    
    return render(request, 'SmartDocsHubApp/template_form.html', {'form': form})

def template_delete(request, pk):
    """Delete a certificate template."""
    template = CertificateTemplate.objects.get(pk=pk)
    if request.method == 'POST':
        template.delete()
        messages.success(request, 'Template deleted successfully!')
        return redirect('SmartDocsHubApp:template_list')
    
    return render(request, 'SmartDocsHubApp/template_confirm_delete.html', {'template': template})

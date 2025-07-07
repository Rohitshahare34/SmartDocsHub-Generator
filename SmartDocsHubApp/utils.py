import os
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import GeneratedCertificate

def process_excel_file(excel_file):
    """Process the uploaded Excel file and return a DataFrame."""
    if excel_file.name.endswith('.csv'):
        df = pd.read_csv(excel_file)
    else:
        df = pd.read_excel(excel_file)
    
    required_columns = ['Name', 'Email', 'Course']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    
    return df

def generate_certificate(template, participant_name, course_name, output_path):
    """Generate a PDF certificate using the template and participant details."""
    # Create PDF
    c = canvas.Canvas(output_path, pagesize=A4)
    
    # Draw template image
    img = Image.open(template.template_image.path)
    img_width, img_height = img.size
    aspect = img_height / float(img_width)
    
    # Scale image to fit A4 width while maintaining aspect ratio
    width = A4[0]
    height = width * aspect
    
    # Center the image on the page
    x = 0
    y = A4[1] - height
    
    c.drawImage(template.template_image.path, x, y, width=width, height=height)
    
    # Add text
    c.setFont("Helvetica-Bold", 24)
    c.drawString(template.name_x, template.name_y, participant_name)
    
    c.setFont("Helvetica", 18)
    c.drawString(template.course_x, template.course_y, course_name)
    
    c.setFont("Helvetica", 12)
    current_date = datetime.now().strftime("%B %d, %Y")
    c.drawString(template.date_x, template.date_y, current_date)
    
    c.save()

def send_certificate_email(certificate):
    """Send the certificate via email to the participant."""
    subject = f'Your Certificate for {certificate.course_name}'
    
    # Create email content
    context = {
        'participant_name': certificate.participant_name,
        'course_name': certificate.course_name,
        'date': certificate.created_at.strftime("%B %d, %Y")
    }
    
    html_message = render_to_string('SmartDocsHubApp/email_template.html', context)
    
    # Send email
    send_mail(
        subject=subject,
        message='',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[certificate.email],
        html_message=html_message,
        fail_silently=False,
    )
    
    # Mark certificate as sent
    certificate.mark_as_sent()

def generate_certificates_from_excel(excel_file, template, send_email=False):
    """Generate certificates for all participants in the Excel file."""
    try:
        df = process_excel_file(excel_file)
        generated_certificates = []
        
        for _, row in df.iterrows():
            # Create certificate
            certificate = GeneratedCertificate(
                template=template,
                participant_name=row['Name'],
                course_name=row['Course'],
                email=row['Email']
            )
            
            # Generate PDF
            output_filename = f"certificate_{row['Name'].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            output_path = os.path.join(settings.MEDIA_ROOT, 'certificates', output_filename)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            generate_certificate(template, row['Name'], row['Course'], output_path)
            certificate.certificate_pdf.name = f'certificates/{output_filename}'
            certificate.save()
            
            # Send email if requested
            if send_email:
                send_certificate_email(certificate)
            
            generated_certificates.append(certificate)
        
        return generated_certificates
    
    except Exception as e:
        # Clean up any generated files if there's an error
        for cert in generated_certificates:
            if os.path.exists(cert.certificate_pdf.path):
                os.remove(cert.certificate_pdf.path)
        raise e 
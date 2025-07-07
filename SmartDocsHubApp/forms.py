from django import forms
from django.core.validators import FileExtensionValidator
from .models import CertificateTemplate

class CertificateGenerationForm(forms.Form):
    excel_file = forms.FileField(
        label='Excel File',
        help_text='Upload an Excel file (.xlsx or .csv) containing participant details',
        validators=[FileExtensionValidator(allowed_extensions=['xlsx', 'csv'])],
        widget=forms.FileInput(attrs={
            'accept': '.xlsx,.csv',
            'class': 'form-control'
        })
    )
    template = forms.ModelChoiceField(
        queryset=CertificateTemplate.objects.all(),
        label='Certificate Template',
        help_text='Select a template for the certificates',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    send_email = forms.BooleanField(
        required=False,
        label='Send Certificates via Email',
        help_text='Check this to automatically send certificates to participants',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    def clean_excel_file(self):
        excel_file = self.cleaned_data.get('excel_file')
        if excel_file:
            if not excel_file.name.endswith(('.xlsx', '.csv')):
                raise forms.ValidationError('Please upload a valid Excel (.xlsx) or CSV file.')
        return excel_file

class CertificateTemplateForm(forms.ModelForm):
    class Meta:
        model = CertificateTemplate
        fields = ['name', 'template_image', 'name_x', 'name_y', 'course_x', 'course_y', 'date_x', 'date_y']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'template_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'name_x': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'name_y': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'course_x': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'course_y': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'date_x': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'date_y': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
        }

    def clean_template_image(self):
        image = self.cleaned_data.get('template_image')
        if image:
            if not image.content_type.startswith('image/'):
                raise forms.ValidationError('Please upload a valid image file.')
        return image 
from django import forms
from .models import enquir_form,student_info,invoice



class enquiry_form(forms.ModelForm):
    class Meta:
        model = enquir_form
        fields = '__all__'
        
        
class student_info_form(forms.ModelForm):
    class Meta:
        model = student_info
        fields = '__all__'
        
        
class invoice_form(forms.ModelForm):
    class Meta:
        model = invoice
        fields = '__all__'
        
        
        
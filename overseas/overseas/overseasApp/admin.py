from django.contrib import admin
from .models import enquir_form,student_info,invoice


class student_info_admin(admin.ModelAdmin):
    model = student_info
    list_display = [
                    'Name',
                    'Email',
                    'Phone',
                    'Location',
                    'Country_Looking_For',
                    'Ielts_score',
                    'Which_Degree_Pursue',
                    'Planning_Apply_In_Year',
                    'Whats_highest_Education',
                    'Expected_Or_Gained_Percentage',
                    'Year_Of_Gruduation',
                    'Status_Of_IELTS_TOEFL_Exam',
                ]

class enquiry_admin(admin.ModelAdmin):
    model  = enquir_form
    list_display = [
                    'Name',
                    'Email',
                    'Phone',
                    'Location'
                    ]
    
class invoiceAdmin(admin.ModelAdmin):
    model  = invoice
    list_display = [
                    'id',
                    'Order_No',
                    'Student_name',
                    'Address',
                    'Phone',
                    'Email',
                    'Date',
                    'Description',
                    'Total_Payment',
                    'Advance_Payment',
                    'Due_Payment',
    ]
    
admin.site.register(enquir_form,enquiry_admin)
admin.site.register(student_info,student_info_admin)
admin.site.register(invoice,invoiceAdmin)
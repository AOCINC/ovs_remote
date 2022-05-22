from django.urls import path
from overseasApp import views


urlpatterns = [
    path('',views.index,name='home'),
    path('get-enquiry',views.enquiry_view,name='get_enquiry'),
    path('admin-login',views.tempLogin, name='admin_login'),
    path('admin-control',views.admin_console, name='admin_control'),
    path('enquired-data',views.enquiry_data, name="enquired_data"),
    path('get-student-info',views.student_info_view,name="get_student_info"),
    path('student-data',views.student_info_data,name = 'students_data'),
    path('New-Invoice',views.invoice_view,name="New-Invoice"),
    path('Invoices',views.Invoice_Data_View,name="Invoices"),
    path('DetailInvoice/<int:id>/',views.Invoice_Detail,name="DetailInvoice"),
    path('SendInvoice/<int:id>/',views.Invoice_Details_Send,name="SendInvoice"),
    path('about-us',views.aboutus,name="about_us")
]

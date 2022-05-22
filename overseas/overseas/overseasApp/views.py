from django.shortcuts import render,redirect,get_object_or_404
from overseasApp.forms import enquiry_form,student_info_form,invoice_form
from overseasApp.models import enquir_form,student_info,invoice
from django.http import HttpResponseRedirect
from django.contrib import messages
from .Email_Config import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .secuirty_creds import *
import nanoid
import datetime
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse
from .util import link_callback



def index(request):
    template = 'overseasApp/home.html'
    
    Data = 'Something'
    context = {
        'data':Data,
    }
    return render(request,template,context)

def admin_console(request):
    template = 'overseasApp/adminconsole.html'
    
    Data = 'Something'
    context = {
        'data':Data,
    }
    return render(request,template,context)

def student_info_view(request):
    template = 'overseasApp/student_info.html'
    if request.method == 'POST':
        form = student_info_form(request.POST)
        if form.is_valid():
            # fetching data to send MAIL
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            phone = form.cleaned_data['Phone']
            location = form.cleaned_data['Location']
            country = form.cleaned_data['Country_Looking_For']
            Ielts_Score = form.cleaned_data['Ielts_score']
            Degree = form.cleaned_data['Which_Degree_Pursue']
            Planning_ApplyIn = form.cleaned_data['Planning_Apply_In_Year']
            highest_Education = form.cleaned_data['Whats_highest_Education']
            Gained_Percentage = form.cleaned_data['Expected_Or_Gained_Percentage']
            Gruduation = form.cleaned_data['Year_Of_Gruduation']
            Status_IELTS_TOEFL = form.cleaned_data['Status_Of_IELTS_TOEFL_Exam']
            # Mail Sending to superlative admin 
            subject = 'STUDENT INFORAMATION OF  \t'+ name + '\tFOR ' + country 
            context = {
                    'name':name,
                    'email':email, 
                    'phone':phone,
                    'location':location,
                    'country':country,
                    'Ielts_Score':Ielts_Score,
                    'Degree':Degree,
                    'Planning_ApplyIn':Planning_ApplyIn,
                    'highest_Education':highest_Education,
                    'Gained_Percentage':Gained_Percentage,
                    'Gruduation':Gruduation,
                    'Status_IELTS_TOEFL' :Status_IELTS_TOEFL,             
                }
            from_email = EMAIL_HOST_USER
            to   = [EMAIL_HOST_USER]
            message = get_template('overseasApp/student_info_email.html').render(context)
            msg = EmailMessage(subject, message, to=to,from_email = from_email)
            msg.content_subtype  = 'html'
            msg.send()
            # mail end
            form.save()
            msg = 'student info stored successfully!'
            messages.success(request,msg)
            return redirect('students_data')
    else:
        form = student_info_form()
    
    context = {
        'form':form,        
    }
    return render(request,template,context)



def student_info_data(request):
    ''' this method will render the student information stored by admin'''
    template = 'overseasApp/student_data.html'
    students = student_info.objects.all().order_by('-id') 
    datacount = students.count() # this is count of all enquiries landed
    context  = {
        'students':students,
        'datacount':datacount,
    }
    return render(request,template,context)

    

def invoice_view(request):
    ''' this method will store the data of student invoice'''
    template = 'overseasApp/invoice.html'
    if request.method == 'POST':
        form = invoice_form(request.POST)
        if form.is_valid():
            # order = form.cleaned_data['Order_No']
            name  = form.cleaned_data['Student_name']
            address = form.cleaned_data['Address']
            phone   = form.cleaned_data['Phone']
            email   = form.cleaned_data['Email']
            date    = form.cleaned_data['Date']
            description = form.cleaned_data['Description']
            totalpayment= form.cleaned_data['Total_Payment']
            advance_payment=form.cleaned_data['Advance_Payment']
            due = int(totalpayment) - int(advance_payment)
            # NANO ID FOR ORDER NO FOR UINQUE
            Uniq_order = nano_id()
            #todays date for storing date
            current_date  = datetime.date.today()  # Returns 2018-01-15
            store_Data = invoice(Order_No =Uniq_order,
                                Student_name = name,
                                Address = address,
                                Phone = phone,
                                Email = email,
                                Date  = current_date,
                                Description = description,
                                Total_Payment = totalpayment,
                                Advance_Payment = advance_payment,
                                Due_Payment   = due
                                )
            store_Data.save()
            return redirect('admin_control')
            
    else:
        form = invoice_form()
    context  = {
        'form':form,
    }
    return render(request,template,context)


def Invoice_Data_View(request):
    template = 'overseasApp/Invoices_data.html'
    invoice_data    = invoice.objects.all().order_by('-id')
    datacount = invoice_data.count() # this is count of all enquiries landed
    context  = {
        'invoice_data':invoice_data,
        'datacount':datacount,
    }
    return render(request,template,context)


def nano_id():
    nanoIdStr = nanoid.generate()
    nanoIdStr = nanoid.generate('0123456789', 6)
    return nanoIdStr


def Invoice_Detail(request, id = None):
    detail_invoice = get_object_or_404(invoice, id = id) 
    order = detail_invoice.Order_No
    name  = detail_invoice.Student_name
    address = detail_invoice.Address
    phone   = detail_invoice.Phone
    email   = detail_invoice.Email
    date    = detail_invoice.Date
    description = detail_invoice.Description
    totalpayment = detail_invoice.Total_Payment
    AdvPayment  = detail_invoice.Advance_Payment
    duePayment  = detail_invoice.Due_Payment
    # Mail Sending to superlative admin 
    subject = 'INVOICE ODRER  \t'+ order 
    context = {
                'order':order,
                'name':name,
                'address':address,
                'phone':phone,
                'email':email,
                'date':date,
                'description':description,
                'totalpayment':totalpayment,
                'AdvPayment':AdvPayment,
                'duePayment':duePayment,             
    }
    from_email = EMAIL_HOST_USER
    to   = [EMAIL_HOST_USER,email]
    message = get_template('overseasApp/invoice_info_email.html').render(context)
    msg = EmailMessage(subject, message, to=to,from_email = from_email)
    msg.content_subtype  = 'html'
    msg.send()
    # mail end
    context = {
        'detail_invoice':detail_invoice,
    }
    template = 'overseasApp/invoice_details.html'

    return render(request,template,context)


def Invoice_Details_Send(request, id = None):
    template_path = 'overseasApp/Bill_PDF.html'
    detail_invoice = get_object_or_404(invoice, id = id) 
    order = detail_invoice.Order_No
    name  = detail_invoice.Student_name
    address = detail_invoice.Address
    phone   = detail_invoice.Phone
    email   = detail_invoice.Email
    date    = detail_invoice.Date
    description = detail_invoice.Description
    totalpayment = detail_invoice.Total_Payment
    AdvPayment  = detail_invoice.Advance_Payment
    duePayment  = detail_invoice.Due_Payment
    # Mail Sending to superlative admin 
    # subject = 'INVOICE ODRER  \t'+ order 
    context = {
                'order':order,
                'name':name,
                'address':address,
                'phone':phone,
                'email':email,
                'date':date,
                'description':description,
                'totalpayment':totalpayment,
                'AdvPayment':AdvPayment,
                'duePayment':duePayment,             
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Bill_PDF.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render((context))
    # create a pdf
    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

    # return render(request,template,context)


def enquiry_view(request):
    if request.method == 'POST':
        form = enquiry_form(request.POST)
        if form.is_valid():
            # fetching data to send MAIL
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            phone = form.cleaned_data['Phone']
            location = form.cleaned_data['Location']
            # Mail Sending to superlative admin 
            subject = 'New Enquiry Request Submitted By\t' + name 
            context = {
                    'name':name,
                    'email':email, 
                    'phone':phone,
                    'location':location,                
                }
            from_email = EMAIL_HOST_USER
            to   = [EMAIL_HOST_USER]
            message = get_template('overseasApp/enquiry_email.html').render(context)
            msg = EmailMessage(subject, message, to=to,from_email = from_email)
            msg.content_subtype  = 'html'
            msg.send()
            # mail end
            form.save()
            msg = 'Submitted,We Will Call You Soon..'
            messages.success(request,msg)
            return redirect('get_enquiry')
    else:
        form = enquiry_form()
    template = 'overseasApp/inquiry_Form.html'
    context ={
        'form':form
    }
    return render(request, template,context )


def enquiry_data(request):
    template = 'overseasApp/enquiry_data.html'
    edata    = enquir_form.objects.all().order_by('-id')
    datacount = edata.count() # this is count of all enquiries landed
    context  = {
        'edata':edata,
        'datacount':datacount,
    }
    return render(request,template,context)


def tempLogin(request):
    template = 'overseasApp/templogin.html'
    if request.method == 'POST':
        login_data = request.POST.dict()  # this is form data from request and saving to dict
        name = login_data.get('admin_name')
        password = login_data.get('passcode')
        if name == Admin_Name and password == Pass_Code:
            return redirect('admin_control')
        else:
            msg = 'Invalid Username Or Password Entered'
            messages.success(request,msg)
            return redirect("admin_login")
    return render(request, template)



def aboutus(request):
    template = 'overseasApp/about.html'
    return render(request,template)
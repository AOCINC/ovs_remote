from django.db import models





class enquir_form(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone = models.CharField(max_length=12)
    Location = models.CharField(max_length=255)


class student_info(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone = models.CharField(max_length=12)
    Location = models.CharField(max_length=255)
    Country_Looking_For = models.CharField(max_length=255)
    Ielts_score = models.CharField(max_length=255)
    Which_Degree_Pursue = models.CharField(max_length=255)
    Planning_Apply_In_Year = models.CharField(max_length=255)
    Whats_highest_Education = models.CharField(max_length=255)
    Expected_Or_Gained_Percentage = models.CharField(max_length=20) 
    Year_Of_Gruduation = models.CharField(max_length=12)
    Status_Of_IELTS_TOEFL_Exam = models.CharField(max_length=25)
    
    
class invoice(models.Model):
    Order_No  = models.CharField(max_length=10,null=True,blank=True)
    Student_name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Phone   = models.CharField(max_length=12)
    Email   = models.CharField(max_length=255)
    Date    = models.CharField(max_length=35,null=True, blank=True)
    Description = models.CharField(max_length=255)
    Total_Payment  = models.CharField(max_length=45)
    Advance_Payment = models.CharField(max_length=45)
    Due_Payment    = models.CharField(max_length=45,null=True, blank=True)
    
    
    
from django.db import models
from googletrans import Translator
translator = Translator()

# # Create your models here.

def translate_me():
    return ""

  

STATES = (
    ('en', 'ENGLISH'),
    ('kn', 'KARNATAKA'),
    ('te', 'ANDRA_TELANGANA'),
    ('tn', 'TAMILNADU'),
    ('mr', 'MAHARASTRA'),
    ('gu', 'GUJARATH'),
    ('pa', 'PANJAB'),
    ('ml', 'KERALA'),
    ('ur', 'URDU'),
    ('bl', 'WESTBENGAL'),
    ('hi', 'HINDI')
)

BOOKS = (
    ('Question Papers','1 Question Papers'),
    ('Syllabus','2 Syllabus'),
    ('How to Prepare','3 How to Prepare'),
    ('Books','4 Books'),
    )



class Job(models.Model):
    JobId = models.AutoField(primary_key=True)
    Language = models.CharField(max_length=12, choices=STATES, default='ENGLISH')

    Name = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Notification_Date = models.CharField(max_length=100)
    Number_Of_Posts = models.CharField(max_length=100)
    LastDate = models.CharField(max_length=100)
    Education = models.CharField(max_length=100)
    Age_Limit = models.CharField(max_length=100)
    Salary = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Application_Fees = models.CharField(max_length=100)
    
    Selection_Process = models.TextField()
    How_To_Apply = models.TextField()
    

    Pdf_link = models.CharField(max_length=100)
    Official_Notification = models.CharField(max_length=100)
    
    Selection_Process_KN  = models.TextField(default="Dont Fill",blank=True, null=True)
    Selection_Process_TE  = models.TextField(default="Dont Fill",blank=True, null=True)
    Selection_Process_TA  = models.TextField(default="Dont Fill",blank=True, null=True)
    Selection_Process_MR  = models.TextField(default="Dont Fill",blank=True, null=True)
    Selection_Process_GU  = models.TextField(default="Dont Fill",blank=True, null=True)
    Selection_Process_PA  = models.TextField(default="Dont Fill",blank=True, null=True)
    Selection_Process_ML  = models.TextField(default="Dont Fill",blank=True, null=True)
    Selection_Process_UR  = models.TextField(default="Dont Fill",blank=True, null=True)
    Selection_Process_BN  = models.TextField(default="Dont Fill",blank=True, null=True)
    Selection_Process_OR  = models.TextField(default="Dont Fill",blank=True, null=True)

    How_To_Apply_KN  = models.TextField(default="Dont Fill",blank=True, null=True)
    How_To_Apply_TE  = models.TextField(default="Dont Fill",blank=True, null=True)
    How_To_Apply_TA  = models.TextField(default="Dont Fill",blank=True, null=True)
    How_To_Apply_MR  = models.TextField(default="Dont Fill",blank=True, null=True)
    How_To_Apply_GU  = models.TextField(default="Dont Fill",blank=True, null=True)
    How_To_Apply_PA  = models.TextField(default="Dont Fill",blank=True, null=True)
    How_To_Apply_ML  = models.TextField(default="Dont Fill",blank=True, null=True)
    How_To_Apply_UR  = models.TextField(default="Dont Fill",blank=True, null=True)
    How_To_Apply_BN  = models.TextField(default="Dont Fill",blank=True, null=True)
    How_To_Apply_OR  = models.TextField(default="Dont Fill",blank=True, null=True)
    How_To_Apply_HI  = models.TextField(default="Dont Fill",blank=True, null=True)


    Name_KN  = models.TextField(default="Dont Fill",blank=True, null=True)
    Name_TE  = models.TextField(default="Dont Fill",blank=True, null=True)
    Name_TA  = models.TextField(default="Dont Fill",blank=True, null=True)
    Name_MR  = models.TextField(default="Dont Fill",blank=True, null=True)
    Name_GU  = models.TextField(default="Dont Fill",blank=True, null=True)
    Name_PA  = models.TextField(default="Dont Fill",blank=True, null=True)
    Name_ML  = models.TextField(default="Dont Fill",blank=True, null=True)
    Name_UR  = models.TextField(default="Dont Fill",blank=True, null=True)
    Name_BN  = models.TextField(default="Dont Fill",blank=True, null=True)
    Name_OR  = models.TextField(default="Dont Fill",blank=True, null=True)
    Name_HI  = models.TextField(default="Dont Fill",blank=True, null=True)

    Department_KN  = models.TextField(default="Dont Fill",blank=True, null=True)
    Department_TE  = models.TextField(default="Dont Fill",blank=True, null=True)
    Department_TA  = models.TextField(default="Dont Fill",blank=True, null=True)
    Department_MR  = models.TextField(default="Dont Fill",blank=True, null=True)
    Department_GU  = models.TextField(default="Dont Fill",blank=True, null=True)
    Department_PA  = models.TextField(default="Dont Fill",blank=True, null=True)
    Department_ML  = models.TextField(default="Dont Fill",blank=True, null=True)
    Department_UR  = models.TextField(default="Dont Fill",blank=True, null=True)
    Department_BN  = models.TextField(default="Dont Fill",blank=True, null=True)
    Department_OR  = models.TextField(default="Dont Fill",blank=True, null=True)
    Department_HI  = models.TextField(default="Dont Fill",blank=True, null=True)

    Location_TE  = models.TextField(default="Dont Fill",blank=True, null=True)
    Location_TA  = models.TextField(default="Dont Fill",blank=True, null=True)
    Location_MR  = models.TextField(default="Dont Fill",blank=True, null=True)
    Location_GU  = models.TextField(default="Dont Fill",blank=True, null=True)
    Location_PA  = models.TextField(default="Dont Fill",blank=True, null=True)
    Location_ML  = models.TextField(default="Dont Fill",blank=True, null=True)
    Location_UR  = models.TextField(default="Dont Fill",blank=True, null=True)
    Location_BN  = models.TextField(default="Dont Fill",blank=True, null=True)
    Location_OR  = models.TextField(default="Dont Fill",blank=True, null=True)
    Location_HI  = models.TextField(default="Dont Fill",blank=True, null=True)
    Location_KN  = models.TextField(default="Dont Fill",blank=True, null=True)

    def save(instance, *args, **kwargs):
        instance.Selection_Process_KN  = translator.translate(instance.Selection_Process, src='en', dest='kn').text
        instance.Selection_Process_TE  = translator.translate(instance.Selection_Process, src='en', dest='te').text
        instance.Selection_Process_TA  = translator.translate(instance.Selection_Process, src='en', dest='ta').text
        instance.Selection_Process_MR  = translator.translate(instance.Selection_Process, src='en', dest='mr').text
        instance.Selection_Process_GU  = translator.translate(instance.Selection_Process, src='en', dest='gu').text
        instance.Selection_Process_PA  = translator.translate(instance.Selection_Process, src='en', dest='pa').text
        instance.Selection_Process_ML  = translator.translate(instance.Selection_Process, src='en', dest='ml').text
        instance.Selection_Process_UR  = translator.translate(instance.Selection_Process, src='en', dest='ur').text
        instance.Selection_Process_BN  = translator.translate(instance.Selection_Process, src='en', dest='bn').text
        #instance.Selection_Process_OR  = translator.translate(instance.Selection_Process, src='en', dest='or').text
        instance.Selection_Process_HI  = translator.translate(instance.Selection_Process, src='en', dest='hi').text
        instance.How_To_Apply_KN       = translator.translate(instance.How_To_Apply, src='en', dest='kn').text
        instance.How_To_Apply_TE       = translator.translate(instance.How_To_Apply, src='en', dest='te').text
        instance.How_To_Apply_TA       = translator.translate(instance.How_To_Apply, src='en', dest='ta').text
        instance.How_To_Apply_MR       = translator.translate(instance.How_To_Apply, src='en', dest='mr').text
        instance.How_To_Apply_GU       = translator.translate(instance.How_To_Apply, src='en', dest='gu').text
        instance.How_To_Apply_PA       = translator.translate(instance.How_To_Apply, src='en', dest='pa').text
        instance.How_To_Apply_ML       = translator.translate(instance.How_To_Apply, src='en', dest='ml').text
        instance.How_To_Apply_UR       = translator.translate(instance.How_To_Apply, src='en', dest='ur').text
        instance.How_To_Apply_BN       = translator.translate(instance.How_To_Apply, src='en', dest='bn').text
        #instance.How_To_Apply_OR       = translator.translate(instance.How_To_Apply, src='en', dest='or').text
        instance.How_To_Apply_HI       = translator.translate(instance.How_To_Apply, src='en', dest='hi').text
        instance.Name_KN               = translator.translate(instance.Name, src='en', dest='kn').text
        instance.Name_TE               = translator.translate(instance.Name, src='en', dest='te').text
        instance.Name_TA               = translator.translate(instance.Name, src='en', dest='ta').text
        instance.Name_MR               = translator.translate(instance.Name, src='en', dest='mr').text
        instance.Name_GU               = translator.translate(instance.Name, src='en', dest='gu').text
        instance.Name_PA               = translator.translate(instance.Name, src='en', dest='pa').text
        instance.Name_ML               = translator.translate(instance.Name, src='en', dest='ml').text
        instance.Name_UR               = translator.translate(instance.Name, src='en', dest='ur').text
        instance.Name_BN               = translator.translate(instance.Name, src='en', dest='bn').text
        #instance.Name_OR               = translator.translate(instance.Name, src='en', dest='or').text
        instance.Name_HI               = translator.translate(instance.Name, src='en', dest='hi').text
        instance.Department_KN         = translator.translate(instance.Department, src='en', dest='kn').text
        instance.Department_TE         = translator.translate(instance.Department, src='en', dest='te').text
        instance.Department_TA         = translator.translate(instance.Department, src='en', dest='ta').text
        instance.Department_MR         = translator.translate(instance.Department, src='en', dest='mr').text
        instance.Department_GU         = translator.translate(instance.Department, src='en', dest='gu').text
        instance.Department_PA         = translator.translate(instance.Department, src='en', dest='pa').text
        instance.Department_ML         = translator.translate(instance.Department, src='en', dest='ml').text
        instance.Department_UR         = translator.translate(instance.Department, src='en', dest='ur').text
        instance.Department_BN         = translator.translate(instance.Department, src='en', dest='bn').text
        #instance.Department_OR         = translator.translate(instance.Department, src='en', dest='or').text
        instance.Department_HI         = translator.translate(instance.Department, src='en', dest='hi').text
        instance.Location_KN           = translator.translate(instance.Location, src='en', dest='kn').text
        instance.Location_TE           = translator.translate(instance.Location, src='en', dest='te').text
        instance.Location_TA           = translator.translate(instance.Location, src='en', dest='ta').text
        instance.Location_MR           = translator.translate(instance.Location, src='en', dest='mr').text
        instance.Location_GU           = translator.translate(instance.Location, src='en', dest='gu').text
        instance.Location_PA           = translator.translate(instance.Location, src='en', dest='pa').text
        instance.Location_ML           = translator.translate(instance.Location, src='en', dest='ml').text
        instance.Location_UR           = translator.translate(instance.Location, src='en', dest='ur').text
        instance.Location_BN           = translator.translate(instance.Location, src='en', dest='bn').text
        #instance.Location_OR           = translator.translate(instance.Location, src='en', dest='or').text
        instance.Location_HI           = translator.translate(instance.Location, src='en', dest='hi').text

        super().save(*args, **kwargs)

    
    class Meta:
      db_table = "jobs"


class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    Name       = models.CharField(max_length=500)
    State      = models.CharField(max_length=12, choices=STATES, default='ENGLISH')
    Logo       = models.CharField(max_length=500)

    def save(instance, *args, **kwargs):
        instance.Logo = "Logo_"+str(instance.DepartmentId).zfill(3)+'.png'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Name


    class Meta:
        db_table = "department"

class Material(models.Model):
    MaterialId = models.AutoField(primary_key=True)
    Language   = models.CharField(max_length=12, choices=STATES, default='ENGLISH')
    Dept_Name  = models.ForeignKey(Department, on_delete=models.CASCADE)
    JobName    = models.CharField(max_length=500)
    SubCategory = models.CharField(max_length=500, default="NA", blank=True, null=True)
    Books      = models.CharField(max_length=50, choices=BOOKS, default='1 Question Papers')
    Year       = models.CharField(max_length=500)
    Images     = models.CharField(max_length=500)
    Link       = models.CharField(max_length=500)

    def save(instance, *args, **kwargs):
        instance.Images = str(instance.MaterialId)+'.png'
        super().save(*args, **kwargs)

    class Meta:
        db_table = "material"


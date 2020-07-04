from django.shortcuts import render
from .models import Job
from .models import Material
from .models import Department
from django.db.models import Q

# Create your views here.


def getlists(request):
   qs = Job.objects.all()   
   return render(request, "list.html", {'qs':list(qs)})


def detail(request,Id):
   qs = Job.objects.filter(JobId=Id)   
   return render(request, "detail.html", {'qs':list(qs)})


def getlists_ta(request):
   qs = Job.objects.filter(Q(Language="ta")|Q(Language="en"))   
   return render(request, "list_ta.html", {'qs':list(qs)})

def detail_ta(request,Id):
   qs = Job.objects.filter(JobId=Id)   
   return render(request, "detail_ta.html", {'qs':list(qs)})

def getlists_te(request):
   qs = Job.objects.filter(Q(Language="te")|Q(Language="en"))   
   return render(request, "list_te.html", {'qs':list(qs)})

def detail_te(request,Id):
   qs = Job.objects.filter(JobId=Id)   
   return render(request, "detail_te.html", {'qs':list(qs)})

def getlists_ml(request):
   qs = Job.objects.filter(Q(Language="ml")|Q(Language="en"))   
   return render(request, "list_ml.html", {'qs':list(qs)})

def detail_ml(request,Id):
   qs = Job.objects.filter(JobId=Id)   
   return render(request, "detail_ml.html", {'qs':list(qs)})

def getlists_gu(request):
   qs = Job.objects.filter(Q(Language="gu")|Q(Language="en"))   
   return render(request, "list_gu.html", {'qs':list(qs)})

def detail_gu(request,Id):
   qs = Job.objects.filter(JobId=Id)   
   return render(request, "detail_gu.html", {'qs':list(qs)})


def getlists_pa(request):
   qs = Job.objects.filter(Q(Language="pa")|Q(Language="en"))   
   return render(request, "list_pa.html", {'qs':list(qs)})


def detail_pa(request,Id):
   qs = Job.objects.filter(JobId=Id)   
   return render(request, "detail_pa.html", {'qs':list(qs)})


def getlists_or(request):
   qs = Job.objects.filter(Q(Language="or")|Q(Language="en"))   
   return render(request, "list_or.html", {'qs':list(qs)})


def detail_or(request,Id):
   qs = Job.objects.filter(JobId=Id)   
   return render(request, "detail_or.html", {'qs':list(qs)})

def getlists_ur(request):
   qs = Job.objects.filter(Q(Language="ur")|Q(Language="en"))   
   return render(request, "list_ur.html", {'qs':list(qs)})


def detail_ur(request,Id):
   qs = Job.objects.filter(JobId=Id)   
   return render(request, "detail_ur.html", {'qs':list(qs)})


def getlists_mr(request):
   qs = Job.objects.filter(Q(Language="mr")|Q(Language="en"))   
   return render(request, "list_mr.html", {'qs':list(qs)})

def detail_mr(request,Id):
   qs = Job.objects.filter(JobId=Id)   
   return render(request, "detail_mr.html", {'qs':list(qs)})


def getlists_kn(request):
   qs = Job.objects.filter(Q(Language="kn")|Q(Language="en"))   
   return render(request, "list_kn.html", {'qs':list(qs)})

def detail_kn(request,Id):
   qs = Job.objects.filter(JobId=Id)   
   return render(request, "detail_kn.html", {'qs':list(qs)})


def getlists_hi(request):
   qs = Job.objects.filter(Q(Language="hi")|Q(Language="en"))   
   return render(request, "list_hi.html", {'qs':list(qs)})

def detail_hi(request,Id):
   qs = Job.objects.filter(JobId=Id)   
   return render(request, "detail_hi.html", {'qs':list(qs)})





def getDept(request,st):
   qs = Department.objects.filter(State=st)
   return render(request, "material/dept.html", {'qs':list(qs)})

def getMaterial(request, dept):
   qs = Material.objects.filter(Dept_Name=dept)   
   return render(request, "material/materials.html", {'qs':list(qs)})

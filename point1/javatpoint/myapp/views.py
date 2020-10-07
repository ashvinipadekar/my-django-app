from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import datetime
from myapp.functions.functions import handle_uploaded_file
# from myapp.form import EmployeeForm
#from myapp.form import StudentForm
import csv
from myapp.models import  Employee


from django.http import HttpResponse
from javatpoint import settings
from django.core.mail import send_mail


def mail(request):
    subject = "Greetings"
    msg = "Congratulations for your success"
    to = "ashbhatkal@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if (res == 1):
        msg = "Mail Sent Successfuly"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)
def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    employees = Employee.objects.all()
    writer = csv.writer(response)
    for employee in employees:
        writer.writerow([employee.eid,employee.ename,employee.econtact])
    return response

# for pdf output
from reportlab.pdfgen import canvas



def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100, 700, "Hello, Javatpoint.")
    p.showPage()
    p.save()
    return response
@require_http_methods(["GET"])
def hello(request):
    return HttpResponse("<h2>This is the HTTP GET request!</h2>")


# session function set and get
def setsession(request):
    request.session['sname'] = 'irfan'
    request.session['semail'] = 'irfan.sssit@gmail.com'
    return HttpResponse("session is set")


def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname + " " + studentemail);


## cookies fn
def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial', 'javatpoint.com')
    return response


def getcookie(request):
    tutorial = request.COOKIES['java-tutorial']
    return HttpResponse("java tutorial @: " + tutorial);

# csv file for static
#def getfile(request):
 #   response = HttpResponse(content_type='text/csv')
  #  response['Content-Disposition'] = 'attachment; filename="file.csv"'
   # writer = csv.writer(response)
    #writer.writerow(['1001', 'John', 'Domil', 'CA'])
    #writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])
    #return response

# def index(request):
#  student = StudentForm()
#  return render(request, "index.html", {'form': student})


# def index(request):
#   stu = StuForm()
#  return render(request, "index.html", {'form': stu})
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


def index(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
        return render(request, "index.html", {'form': student})

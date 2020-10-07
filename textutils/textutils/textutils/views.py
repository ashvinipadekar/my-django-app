# i have created this file ashvini padekar code upto video 6
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   return HttpResponse("hello")
def about(request):
     return HttpResponse("ashvini datta padekar")
def navigator(request):
  s="<h2>Navigation Bar</br></h2><a href=https://www.codewithharry.com/>django code with harry</a></br><a href=https://www.facebook.com/>facebook</a></br><a href=https://mail.google.com/mail/u/0/#inbox>gmail.com</a><br>"

# return HttpResponse(s)

def index(request):
    # params={'name':'datta','age':31}
    return render(request, 'index.html')


# return HttpResponse("home")


"""
def removepun(request):
    return HttpResponse("remove pun ")


def capitalizefirst(request):
    return HttpResponse("capitalize first")


def newlineremove(request):
    return HttpResponse("new line remove")


def spaceremove(request):
    djtext=request.GET.get('text','default')
    print(djtext)
    return HttpResponse(" space remove")



def charcount(request):
    return HttpResponse("char count")
"""


def analyze(request):
    djtext = request.GET.get('text', 'default')
    spaceremove = request.GET.get('spaceremove', 'off')
    print(spaceremove)
    print(djtext)
    if spaceremove== 'on':
   # analyzed=djtext
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
             if char  not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'remove punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse('error')

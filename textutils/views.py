
from django.http import HttpResponse

from django.shortcuts import render



def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    spaceremove=request.POST.get('spaceremove','off')
    newlineremove=request.POST.get('newlineremove','off')
    capatalize=request.POST.get('capatalize','off')
    charcount=request.POST.get('charcount','off')

    #analyze the text

    analyzed=djtext
    flag=0
    if removepunc=="on":
        temp=""
        flag=1
        punctuations='''<>:;'"[]{}()-*&^%$#@!~_'''
        for i in analyzed:
            if i not in punctuations:
                temp+=i
        analyzed=temp

    if spaceremove=="on":
            temp=""
            flag=1
            for i,j in enumerate(analyzed):
                if not (analyzed[i]==" " and analyzed[i+1]==" "):
                    temp+=j
            analyzed=temp

    if newlineremove=="on":
            temp=""
            flag=1
            for i in analyzed:
                if i !='\n' and i !='\r':
                    temp+=i
            analyzed=temp

    if capatalize=="on":
            analyzed=analyzed.upper()
            flag=1

    if charcount=="on":
            length=len(analyzed)
            analyzed=analyzed+'\n'+'length of string is '+str(length)
            flag=1

    if flag:
        params={'purpose':'Analysed text','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error,please choose atleast one of the features")


def about(request):
    return render(request,'about.html')

def help(request):
    return render(request,'help.html')


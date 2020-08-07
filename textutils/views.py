# I have created this file - Abhishekcd
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index2.html')
    #return HttpResponse('<h1>Hello Abhishek</h1> <a href = "https://www.youtube.com/">YouTube Home</a>')

def ex1(request):
    sites = ['''<h3>For Entertainment </h3><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h3>For Interaction </h3><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h3>For Insight   </h3><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h3>For Internship   </h3><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse(sites)

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    #Check checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        params = {'analyzed_text': analyzed}
        #return render(request, 'analyze2.html', params)

    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        djtext = analyzed
        params = {'analyzed_text': analyzed}
        #return render(request, 'analyze2.html', params)

    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed + char
        djtext = analyzed
        params = {'analyzed_text': analyzed}
       # return render(request, 'analyze2.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        djtext = analyzed
        params = {'analyzed_text': analyzed}
        #return render(request, 'analyze2.html', params)

    if charcount=="on":
        analyzed = "Number of characters: " + str(len(djtext))
        djtext = analyzed
        params = {'analyzed_text': analyzed}
        #return render(request, 'analyze2.html', params)

    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' and charcount!='on'):
        return HttpResponse('Error')
    
    return render(request,'analyze2.html',params)




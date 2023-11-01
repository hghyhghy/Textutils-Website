
from django.http import HttpResponse

from django.core.files import File

from django.shortcuts import render

def index(request):

    # giving an html tag to that 

    return HttpResponse('''<h1> Subham </h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Django By Subham</a>''')

def about(request):
 
    return HttpResponse("About Django")

def geeks(request):

    return HttpResponse('''<h1> Geeks For Geeks </h1> <a href="https://www.geeksforgeeks.org/chainmap-in-python/?ref=lbp"> Python </a>''')

def text(response):

    file=open("textutils/textutils/t.txt","r")

    if file.mode=="r":

        contents=file.read()

        print(contents)

    return HttpResponse()


def home(request):

    # creating a dictionary 


    return render(request,"index.html")

     # render takes  total three argument of request and html file


    # return HttpResponse("<h1> Home </h1>")


def ex1(request):

    nav='''<h1> Navigation Bar </h1>

    <a href="https://www.bing.com/search?pglt=131&q=facebook&cvid=90518eb28fa84ef9b30987882720e816&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDI0NDdqMGoxqAIAsAIA&FORM=ANNTA1&
    PC=U531"> Facebook</a> <br>
    
    <a href="https://www.bing.com/search?pglt=131&q=instagram&cvid=2c91348d3828405a89c4a404e57aef6e&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDMyNzhqMGoxqAIAsAIA&FORM=ANNTA1&PC=U531"> Instagram </a>

    '''

    return HttpResponse(nav)
    



def analyze(request):
    # accessing the data in that

    djtext=request.POST.get('text','default')

    removepunc=request.POST.get('removepunc','off')

    fullcaps=request.POST.get('fullcaps','off')

    newlineremover=request.POST.get('newlineremover','off')

    extraspaceremover=request.POST.get('extraspaceremover','off')

    charcounter=request.POST.get('charcounter','off')




    if removepunc=="on":

    # creating a variable  dictionary


        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

        analyzed=""

        # using for loop 

        for chars in djtext:

            if chars not in punctuations:

                analyzed=analyzed+chars
                
        param={"purpose":"Remove Punctuations","analyzed_text":analyzed}

        # rendering the analyze.html 

        djtext=analyzed

        # return render(request,'analyze.html',param)
    
    if(fullcaps=="on"):

        analyzed=" "

        for chars in djtext:

            analyzed=analyzed+chars.upper()

        param={"purpose":"Changed to Upper","analyzed_text":analyzed}

        # rendering the analyze.html 
        
        djtext=analyzed

    

    if(charcounter=="on"):

        analyzed=len(djtext)

        
        param={"purpose":"Counting the characters","analyzed_text":analyzed}


        # rendering the analyze.html 

        djtext=analyzed
        

    
    if(extraspaceremover=="on"):

        analyzed=" "

        for index,chars in enumerate(djtext):

            if not(djtext[index]==" " and djtext[index+1]==" "):

                
                analyzed=analyzed+chars


        param={"purpose":"Removing Extra Space","analyzed_text":analyzed}

        # rendering the analyze.html 
        
        djtext=analyzed

    
    if(newlineremover=="on"):

        analyzed=" "

        for chars in djtext:

            if chars!="\n" and chars!="\r":

                analyzed=analyzed+chars

        param={"purpose":"New line remover","analyzed_text":analyzed}

        # rendering the analyze.html 

    if(removepunc!="on" and charcounter!="on" and extraspaceremover!="on" and fullcaps!="on" and newlineremover!="on"):

        return HttpResponse("Error !")
    
    return render(request,'analyze.html',param)



 
def capitalfirst(request):

    return HttpResponse("<h1>Capitalfirst</h1>")


def removenewline(request):

    return HttpResponse("<h1>removenewline</h1>")

def spaceremove(request):

    return HttpResponse("<h1>spaceremove</h1>  <a href='/'> Back </a>")

def charcount(request):

    return HttpResponse("<h1>charcount</h1>")

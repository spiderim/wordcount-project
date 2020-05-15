from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return HttpResponse('hi i am sonu sharma \n i created this website')

def count(request):
    fulltext=request.GET['fulltext']
    wordsplit=fulltext.split()
    worddict=dict()
    for word in wordsplit:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1


    return render(request,'count.html',{'fulltext':fulltext,'number':len(wordsplit),'worddict':worddict.items()})

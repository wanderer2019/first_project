from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def main_page(request):
    # contextnamepage = {'pagename':'mypage'}
    return render(request, 'index.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    # print(fulltext)
    return render(request,'count.html',{'fulltext':fulltext,'count': len(wordlist)})

def about(request):
    return render(request, 'about.html')

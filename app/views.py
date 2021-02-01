from django.shortcuts import render,redirect
import get_text
from .models import urls,top_words
# Create your views here.

def frequency(request):
    if request.method=='POST':
        
        input_url=request.POST.get('input_url')
        return redirect('result',input_url=input_url)

    return render(request,'frequency.html')

def result(request):
    if request.method=='POST':
        url=request.POST.get('input_url')
        is_urls_available=urls.objects.get_or_create(url=url)
        
        if is_urls_available[1]:
            print('created')
            print(request.POST.get('input_url'))
            top10wods=get_text.top10_word(request.POST.get('input_url'))
            for i in top10wods:
                top_words.objects.create(url=is_urls_available[0],word=i[0],frequency=i[1])
            
            massege='Here\'s your newly searched url result'
            return render(request,'result.html',{'words':top10wods,'massege':massege,'url':url})
        else:
            massege='You already searched this url, so this result showing from database'
            top10wods=top_words.objects.filter(url=is_urls_available[0])
            return render(request,'result.html',{'wordsfrmdatabase':top10wods,'massege':massege,'url':url})
    
    massege='You have not searched anything, go to frequency page'
    return render(request,'result.html',{'massege':massege})

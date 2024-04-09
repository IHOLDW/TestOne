from django.shortcuts import render,HttpResponse
# views.py

from django.http import JsonResponse
from django.middleware.csrf import get_token

def get_csrf_token_view(request):
    # Generate CSRF token
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

# Create your views here.
def data(request):
    if request.method=='post':
        http_response_code = request.POST.get('httpResponseCode') 
        return render(request,'data.html',{'code':http_response_code})
    return render(request,'data.html',{'code':"error"})
    